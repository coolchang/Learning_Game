#!/usr/bin/env python3
"""
SuperMemo SM-2 기반 간격 반복 학습(SRS) 알고리즘

이 스크립트는 독립 실행 및 임포트 가능한 SRS 알고리즘을 제공합니다.
일본어 학습 게임에서 최적의 복습 타이밍을 계산하는 데 사용됩니다.

Reference: https://www.supermemo.com/en/archives1990-2015/english/ol/sm2
"""

from datetime import datetime, timedelta
from typing import TypedDict, Literal, Optional
from dataclasses import dataclass
import json


# 타입 정의
CardStatus = Literal['new', 'learning', 'review', 'lapsed', 'mastered']


@dataclass
class SRSCard:
    """SRS 카드 데이터 구조"""
    card_id: str
    status: CardStatus = 'new'
    easiness: float = 2.5  # 난이도 계수 (1.3-2.5)
    interval: int = 0  # 다음 복습까지 일수
    repetitions: int = 0  # 연속 정답 횟수
    next_review: Optional[datetime] = None
    last_review: Optional[datetime] = None


def calculate_next_review(
    quality: int,
    card: SRSCard,
    current_time: Optional[datetime] = None
) -> SRSCard:
    """
    다음 복습 일정 계산 (SuperMemo SM-2 알고리즘)

    Args:
        quality: 응답 품질 (0-5)
            5: 완벽 - 즉시 정답, 확신함
            4: 정답 - 약간 고민 후 정답
            3: 어렵게 정답 - 고민 많이 했지만 정답
            2: 오답 (알 것 같음) - 틀렸지만 답을 보니 알 것 같음
            1: 오답 (어려움) - 틀렸고 어려웠음
            0: 오답 (전혀 모름) - 완전히 몰랐음

        card: 현재 SRS 카드 상태
        current_time: 현재 시간 (테스트용, 기본값은 현재 시간)

    Returns:
        업데이트된 SRS 카드 상태
    """
    if current_time is None:
        current_time = datetime.now()

    # 복사본 생성
    new_card = SRSCard(
        card_id=card.card_id,
        status=card.status,
        easiness=card.easiness,
        interval=card.interval,
        repetitions=card.repetitions,
        next_review=card.next_review,
        last_review=current_time
    )

    # Quality가 3 미만이면 다시 학습 (Lapsed)
    if quality < 3:
        new_card.repetitions = 0
        new_card.interval = 1
        new_card.status = 'lapsed'
    else:
        # 정답인 경우
        if new_card.repetitions == 0:
            # 첫 번째 정답
            new_card.interval = 1
            new_card.status = 'learning'
        elif new_card.repetitions == 1:
            # 두 번째 정답
            new_card.interval = 6
            new_card.status = 'review'
        else:
            # 세 번째 이상 정답
            new_card.interval = round(new_card.interval * new_card.easiness)

            # Mastered 상태 체크 (90일 이상 간격)
            if new_card.interval >= 90:
                new_card.status = 'mastered'
            else:
                new_card.status = 'review'

        new_card.repetitions += 1

    # 난이도 계수(easiness) 조정
    # EF' = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    new_card.easiness = new_card.easiness + (
        0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)
    )

    # 난이도 계수는 1.3 ~ 2.5 범위로 제한
    new_card.easiness = max(1.3, min(2.5, new_card.easiness))

    # 다음 복습 시간 설정
    new_card.next_review = current_time + timedelta(days=new_card.interval)

    return new_card


def get_due_cards(
    cards: list[SRSCard],
    current_time: Optional[datetime] = None
) -> list[SRSCard]:
    """
    복습 시간이 된 카드 반환

    Args:
        cards: SRS 카드 리스트
        current_time: 현재 시간 (기본값은 현재 시간)

    Returns:
        복습할 카드 리스트 (우선순위 순으로 정렬)
    """
    if current_time is None:
        current_time = datetime.now()

    due_cards = []
    overdue_cards = []
    new_cards = []

    for card in cards:
        if card.status == 'new':
            new_cards.append(card)
        elif card.next_review and card.next_review <= current_time:
            # 기한이 지난 정도 계산
            days_overdue = (current_time - card.next_review).days
            if days_overdue > 0:
                overdue_cards.append((days_overdue, card))
            else:
                due_cards.append(card)

    # 우선순위: 기한 지난 카드 > 오늘 복습할 카드 > 신규 카드
    # 기한 지난 카드는 지난 정도가 큰 순서로 정렬
    overdue_cards.sort(key=lambda x: x[0], reverse=True)
    result = [card for _, card in overdue_cards] + due_cards + new_cards

    return result


def get_daily_queue(
    cards: list[SRSCard],
    new_cards_limit: int = 20,
    review_cards_limit: int = 100,
    current_time: Optional[datetime] = None
) -> dict:
    """
    일일 학습 큐 생성

    Args:
        cards: 전체 SRS 카드 리스트
        new_cards_limit: 하루 신규 카드 최대 개수
        review_cards_limit: 하루 복습 카드 최대 개수
        current_time: 현재 시간

    Returns:
        일일 학습 큐 (new_cards, review_cards, overdue_cards)
    """
    if current_time is None:
        current_time = datetime.now()

    new_cards = []
    review_cards = []
    overdue_cards = []

    for card in cards:
        if card.status == 'new':
            if len(new_cards) < new_cards_limit:
                new_cards.append(card)
        elif card.next_review and card.next_review <= current_time:
            days_overdue = (current_time - card.next_review).days
            if days_overdue > 0:
                overdue_cards.append((days_overdue, card))
            elif len(review_cards) < review_cards_limit:
                review_cards.append(card)

    # 기한 지난 카드는 우선순위가 높으므로 제한 없음
    overdue_cards.sort(key=lambda x: x[0], reverse=True)
    overdue_cards_list = [card for _, card in overdue_cards]

    return {
        'overdue_cards': overdue_cards_list,
        'review_cards': review_cards,
        'new_cards': new_cards,
        'total_cards': len(overdue_cards_list) + len(review_cards) + len(new_cards),
        'priority_queue': overdue_cards_list + review_cards + new_cards
    }


def card_to_dict(card: SRSCard) -> dict:
    """SRS 카드를 딕셔너리로 변환 (JSON 직렬화용)"""
    return {
        'card_id': card.card_id,
        'status': card.status,
        'easiness': card.easiness,
        'interval': card.interval,
        'repetitions': card.repetitions,
        'next_review': card.next_review.isoformat() if card.next_review else None,
        'last_review': card.last_review.isoformat() if card.last_review else None,
    }


def dict_to_card(data: dict) -> SRSCard:
    """딕셔너리를 SRS 카드로 변환"""
    return SRSCard(
        card_id=data['card_id'],
        status=data['status'],
        easiness=data['easiness'],
        interval=data['interval'],
        repetitions=data['repetitions'],
        next_review=datetime.fromisoformat(data['next_review']) if data['next_review'] else None,
        last_review=datetime.fromisoformat(data['last_review']) if data['last_review'] else None,
    )


# CLI 인터페이스
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="SRS 알고리즘 테스트 및 시뮬레이션"
    )
    parser.add_argument(
        '--demo',
        action='store_true',
        help='SRS 알고리즘 데모 실행'
    )
    parser.add_argument(
        '--quality',
        type=int,
        choices=[0, 1, 2, 3, 4, 5],
        help='응답 품질 (0-5)'
    )
    parser.add_argument(
        '--card-id',
        type=str,
        help='카드 ID'
    )

    args = parser.parse_args()

    if args.demo:
        print("=" * 60)
        print("SRS 알고리즘 데모")
        print("=" * 60)
        print()

        # 새 카드 생성
        card = SRSCard(card_id="demo-001", status='new')
        print(f"초기 카드: {card}")
        print()

        # 시뮬레이션: 5번 정답
        qualities = [5, 4, 5, 3, 5]
        current_time = datetime.now()

        for i, quality in enumerate(qualities, 1):
            card = calculate_next_review(quality, card, current_time)
            print(f"복습 {i} (품질: {quality})")
            print(f"  상태: {card.status}")
            print(f"  난이도: {card.easiness:.2f}")
            print(f"  간격: {card.interval}일")
            print(f"  다음 복습: {card.next_review.strftime('%Y-%m-%d')}")
            print()

            # 다음 복습 시간으로 이동
            current_time = card.next_review

        print("=" * 60)
        print("데모 완료!")
        print(f"최종 상태: {card.status}")
        print(f"숙달까지 {max(0, 90 - card.interval)}일 남음")

    elif args.quality is not None and args.card_id:
        # 개별 카드 업데이트
        card = SRSCard(card_id=args.card_id, status='new')
        updated_card = calculate_next_review(args.quality, card)
        print(json.dumps(card_to_dict(updated_card), indent=2, ensure_ascii=False))

    else:
        parser.print_help()
