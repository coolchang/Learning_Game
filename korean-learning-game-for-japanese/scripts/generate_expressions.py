#!/usr/bin/env python3
"""
韓国語表現データ生成スクリプト
状況別の実用的な表現50個を生成
"""

import json
import os

def generate_expressions_data():
    """状況別表現データを生成"""

    expressions = [
        # 挨拶・出会い
        {
            "id": 1,
            "situation": "初対面",
            "korean": "처음 뵙겠습니다",
            "reading": "チョウム ペプケッスムニダ",
            "japanese": "初めてお目にかかります",
            "level": "初級",
            "formality": "丁寧",
            "usage": "ビジネスや公式な場面での初対面の挨拶",
            "relatedExpressions": ["만나서 반갑습니다", "잘 부탁드립니다"]
        },
        {
            "id": 2,
            "situation": "初対面",
            "korean": "만나서 반갑습니다",
            "reading": "マンナソ パンガプスムニダ",
            "japanese": "お会いできて嬉しいです",
            "level": "初級",
            "formality": "丁寧",
            "usage": "初めて会った人への挨拶",
            "relatedExpressions": ["처음 뵙겠습니다", "반가워요"]
        },
        {
            "id": 3,
            "situation": "別れ",
            "korean": "또 만나요",
            "reading": "ット マンナヨ",
            "japanese": "また会いましょう",
            "level": "初級",
            "formality": "普通",
            "usage": "友達との別れ際",
            "relatedExpressions": ["다음에 봐요", "나중에 봐요"]
        },
        {
            "id": 4,
            "situation": "別れ",
            "korean": "조심해서 가세요",
            "reading": "チョシメソ カセヨ",
            "japanese": "気をつけて行ってください",
            "level": "初級",
            "formality": "丁寧",
            "usage": "相手を見送るとき",
            "relatedExpressions": ["안녕히 가세요", "잘 가요"]
        },

        # 感謝・謝罪
        {
            "id": 5,
            "situation": "感謝",
            "korean": "정말 감사합니다",
            "reading": "チョンマル カムサハムニダ",
            "japanese": "本当にありがとうございます",
            "level": "初級",
            "formality": "丁寧",
            "usage": "深い感謝を表現するとき",
            "relatedExpressions": ["고맙습니다", "감사드립니다"]
        },
        {
            "id": 6,
            "situation": "感謝",
            "korean": "덕분에 잘 됐어요",
            "reading": "トクプネ チャル ドェッソヨ",
            "japanese": "おかげでうまくいきました",
            "level": "中級",
            "formality": "普通",
            "usage": "相手の助けで物事がうまくいったとき",
            "relatedExpressions": ["도와주셔서 감사해요", "덕분이에요"]
        },
        {
            "id": 7,
            "situation": "謝罪",
            "korean": "정말 죄송합니다",
            "reading": "チョンマル チェソンハムニダ",
            "japanese": "本当に申し訳ございません",
            "level": "初級",
            "formality": "丁寧",
            "usage": "深く謝罪するとき",
            "relatedExpressions": ["죄송해요", "미안합니다"]
        },
        {
            "id": 8,
            "situation": "謝罪",
            "korean": "제 잘못이에요",
            "reading": "チェ チャルモシエヨ",
            "japanese": "私のミスです",
            "level": "初級",
            "formality": "普通",
            "usage": "自分の過ちを認めるとき",
            "relatedExpressions": ["제 실수예요", "제가 잘못했어요"]
        },

        # 依頼・お願い
        {
            "id": 9,
            "situation": "依頼",
            "korean": "도와주실 수 있으세요?",
            "reading": "トワジュシル ス イッスセヨ?",
            "japanese": "助けていただけますか?",
            "level": "中級",
            "formality": "丁寧",
            "usage": "丁寧に助けを求めるとき",
            "relatedExpressions": ["도와주세요", "부탁드립니다"]
        },
        {
            "id": 10,
            "situation": "依頼",
            "korean": "부탁 하나만 들어주세요",
            "reading": "プタク ハナマン トゥロジュセヨ",
            "japanese": "お願いを一つ聞いてください",
            "level": "中級",
            "formality": "丁寧",
            "usage": "特別なお願いをするとき",
            "relatedExpressions": ["부탁이 있어요", "도와주세요"]
        },

        # レストラン・食事
        {
            "id": 11,
            "situation": "注文",
            "korean": "주문하시겠어요?",
            "reading": "チュムナシゲッソヨ?",
            "japanese": "ご注文されますか?",
            "level": "初級",
            "formality": "丁寧",
            "usage": "レストランでウェイターが使う表現",
            "relatedExpressions": ["뭐 드시겠어요?", "메뉴 정하셨어요?"]
        },
        {
            "id": 12,
            "situation": "注文",
            "korean": "이거 주세요",
            "reading": "イゴ ジュセヨ",
            "japanese": "これください",
            "level": "初級",
            "formality": "丁寧",
            "usage": "メニューを指して注文するとき",
            "relatedExpressions": ["이거로 할게요", "이거 하나요"]
        },
        {
            "id": 13,
            "situation": "食事",
            "korean": "잘 먹겠습니다",
            "reading": "チャル モッケッスムニダ",
            "japanese": "いただきます",
            "level": "初級",
            "formality": "丁寧",
            "usage": "食事の前に言う挨拶",
            "relatedExpressions": ["맛있게 먹을게요"]
        },
        {
            "id": 14,
            "situation": "食事",
            "korean": "잘 먹었습니다",
            "reading": "チャル モゴッスムニダ",
            "japanese": "ごちそうさまでした",
            "level": "初級",
            "formality": "丁寧",
            "usage": "食事の後に言う挨拶",
            "relatedExpressions": ["맛있었어요"]
        },
        {
            "id": 15,
            "situation": "食事",
            "korean": "맛있어요",
            "reading": "マシッソヨ",
            "japanese": "美味しいです",
            "level": "初級",
            "formality": "普通",
            "usage": "料理が美味しいとき",
            "relatedExpressions": ["정말 맛있네요", "너무 맛있어요"]
        },

        # ショッピング
        {
            "id": 16,
            "situation": "買い物",
            "korean": "얼마예요?",
            "reading": "オルマエヨ?",
            "japanese": "いくらですか?",
            "level": "初級",
            "formality": "普通",
            "usage": "値段を尋ねるとき",
            "relatedExpressions": ["가격이 어떻게 돼요?", "얼마입니까?"]
        },
        {
            "id": 17,
            "situation": "買い物",
            "korean": "깎아주세요",
            "reading": "カッカジュセヨ",
            "japanese": "値引きしてください",
            "level": "中級",
            "formality": "丁寧",
            "usage": "値切るとき",
            "relatedExpressions": ["좀 싸게 해주세요", "할인 안 돼요?"]
        },
        {
            "id": 18,
            "situation": "買い物",
            "korean": "입어봐도 돼요?",
            "reading": "イボバド ドェヨ?",
            "japanese": "試着してもいいですか?",
            "level": "中級",
            "formality": "普通",
            "usage": "服を試着したいとき",
            "relatedExpressions": ["입어볼 수 있어요?", "입어봐도 괜찮아요?"]
        },
        {
            "id": 19,
            "situation": "買い物",
            "korean": "카드 되나요?",
            "reading": "カドゥ ドェナヨ?",
            "japanese": "カード使えますか?",
            "level": "初級",
            "formality": "普通",
            "usage": "カード決済が可能か尋ねるとき",
            "relatedExpressions": ["카드 결제 가능해요?", "신용카드 돼요?"]
        },
        {
            "id": 20,
            "situation": "買い物",
            "korean": "영수증 주세요",
            "reading": "ヨンスジュン ジュセヨ",
            "japanese": "レシートください",
            "level": "初級",
            "formality": "丁寧",
            "usage": "レシートをもらうとき",
            "relatedExpressions": ["영수증 주실 수 있어요?", "영수증 부탁합니다"]
        },

        # 道案内
        {
            "id": 21,
            "situation": "道案内",
            "korean": "길을 잃었어요",
            "reading": "キルル イロッソヨ",
            "japanese": "道に迷いました",
            "level": "初級",
            "formality": "普通",
            "usage": "道に迷ったとき",
            "relatedExpressions": ["길을 몰라요", "어디로 가야 해요?"]
        },
        {
            "id": 22,
            "situation": "道案内",
            "korean": "여기가 어디예요?",
            "reading": "ヨギガ オディエヨ?",
            "japanese": "ここはどこですか?",
            "level": "初級",
            "formality": "普通",
            "usage": "現在地を尋ねるとき",
            "relatedExpressions": ["여기가 어디죠?", "이 근처가 어디예요?"]
        },
        {
            "id": 23,
            "situation": "道案内",
            "korean": "어떻게 가요?",
            "reading": "オットケ カヨ?",
            "japanese": "どうやって行きますか?",
            "level": "初級",
            "formality": "普通",
            "usage": "行き方を尋ねるとき",
            "relatedExpressions": ["어디로 가면 돼요?", "가는 길 좀 알려주세요"]
        },
        {
            "id": 24,
            "situation": "道案内",
            "korean": "멀어요?",
            "reading": "モロヨ?",
            "japanese": "遠いですか?",
            "level": "初級",
            "formality": "普通",
            "usage": "距離を尋ねるとき",
            "relatedExpressions": ["가까워요?", "얼마나 걸려요?"]
        },
        {
            "id": 25,
            "situation": "道案内",
            "korean": "여기서 가까워요",
            "reading": "ヨギソ カッカウォヨ",
            "japanese": "ここから近いです",
            "level": "初級",
            "formality": "普通",
            "usage": "近いことを伝えるとき",
            "relatedExpressions": ["가까워요", "걸어갈 수 있어요"]
        },

        # 電話
        {
            "id": 26,
            "situation": "電話",
            "korean": "여보세요",
            "reading": "ヨボセヨ",
            "japanese": "もしもし",
            "level": "初級",
            "formality": "普通",
            "usage": "電話に出るとき",
            "relatedExpressions": ["네, 여보세요"]
        },
        {
            "id": 27,
            "situation": "電話",
            "korean": "저 지금 바빠요",
            "reading": "チョ チグム パッパヨ",
            "japanese": "私今忙しいです",
            "level": "初級",
            "formality": "普通",
            "usage": "電話で忙しいことを伝えるとき",
            "relatedExpressions": ["나중에 전화할게요", "다시 전화해도 돼요?"]
        },
        {
            "id": 28,
            "situation": "電話",
            "korean": "다시 한번 말씀해 주세요",
            "reading": "タシ ハンボン マルスメ ジュセヨ",
            "japanese": "もう一度おっしゃってください",
            "level": "中級",
            "formality": "丁寧",
            "usage": "聞き取れなかったとき",
            "relatedExpressions": ["잘 안 들려요", "다시 말해주세요"]
        },

        # 天気
        {
            "id": 29,
            "situation": "天気",
            "korean": "날씨가 좋네요",
            "reading": "ナルシガ チョンネヨ",
            "japanese": "天気がいいですね",
            "level": "初級",
            "formality": "普通",
            "usage": "良い天気のとき",
            "relatedExpressions": ["날씨가 맑아요", "날씨가 화창해요"]
        },
        {
            "id": 30,
            "situation": "天気",
            "korean": "비가 올 것 같아요",
            "reading": "ピガ オル コッ カタヨ",
            "japanese": "雨が降りそうです",
            "level": "中級",
            "formality": "普通",
            "usage": "雨が降りそうなとき",
            "relatedExpressions": ["비 올까봐요", "우산 챙기세요"]
        },

        # 病院
        {
            "id": 31,
            "situation": "病院",
            "korean": "어디가 아프세요?",
            "reading": "オディガ アプセヨ?",
            "japanese": "どこが痛いですか?",
            "level": "初級",
            "formality": "丁寧",
            "usage": "医者が患者に尋ねるとき",
            "relatedExpressions": ["어디 불편하세요?", "증상이 어떠세요?"]
        },
        {
            "id": 32,
            "situation": "病院",
            "korean": "머리가 아파요",
            "reading": "モリガ アパヨ",
            "japanese": "頭が痛いです",
            "level": "初級",
            "formality": "普通",
            "usage": "頭痛を伝えるとき",
            "relatedExpressions": ["두통이 있어요", "머리가 너무 아파요"]
        },
        {
            "id": 33,
            "situation": "病院",
            "korean": "약을 처방해 주세요",
            "reading": "ヤグル チョバンヘ ジュセヨ",
            "japanese": "薬を処方してください",
            "level": "中級",
            "formality": "丁寧",
            "usage": "薬の処方を求めるとき",
            "relatedExpressions": ["약 좀 주세요", "처방전 주세요"]
        },

        # 感情表現
        {
            "id": 34,
            "situation": "喜び",
            "korean": "너무 기뻐요",
            "reading": "ノム キッポヨ",
            "japanese": "とても嬉しいです",
            "level": "初級",
            "formality": "普通",
            "usage": "喜びを表現するとき",
            "relatedExpressions": ["정말 좋아요", "행복해요"]
        },
        {
            "id": 35,
            "situation": "驚き",
            "korean": "정말이에요?",
            "reading": "チョンマリエヨ?",
            "japanese": "本当ですか?",
            "level": "初級",
            "formality": "普通",
            "usage": "驚いたとき",
            "relatedExpressions": ["진짜요?", "믿을 수 없어요"]
        },
        {
            "id": 36,
            "situation": "悲しみ",
            "korean": "너무 슬퍼요",
            "reading": "ノム スルポヨ",
            "japanese": "とても悲しいです",
            "level": "初級",
            "formality": "普通",
            "usage": "悲しみを表現するとき",
            "relatedExpressions": ["마음이 아파요", "슬프네요"]
        },
        {
            "id": 37,
            "situation": "励まし",
            "korean": "힘내세요",
            "reading": "ヒムネセヨ",
            "japanese": "頑張ってください",
            "level": "初級",
            "formality": "丁寧",
            "usage": "相手を励ますとき",
            "relatedExpressions": ["힘내요", "파이팅"]
        },
        {
            "id": 38,
            "situation": "励まし",
            "korean": "괜찮을 거예요",
            "reading": "クェンチャヌル コエヨ",
            "japanese": "大丈夫でしょう",
            "level": "初級",
            "formality": "普通",
            "usage": "安心させるとき",
            "relatedExpressions": ["잘 될 거예요", "걱정 마세요"]
        },

        # 意見・同意
        {
            "id": 39,
            "situation": "同意",
            "korean": "저도 그렇게 생각해요",
            "reading": "チョド クロケ センガケヨ",
            "japanese": "私もそう思います",
            "level": "中級",
            "formality": "普通",
            "usage": "相手の意見に同意するとき",
            "relatedExpressions": ["동의해요", "맞아요"]
        },
        {
            "id": 40,
            "situation": "反対",
            "korean": "그건 아닌 것 같아요",
            "reading": "クゴン アニン ゴッ カタヨ",
            "japanese": "それは違うと思います",
            "level": "中級",
            "formality": "普通",
            "usage": "柔らかく反対するとき",
            "relatedExpressions": ["좀 다르게 생각해요", "제 생각은 달라요"]
        },

        # 提案
        {
            "id": 41,
            "situation": "提案",
            "korean": "같이 갈래요?",
            "reading": "カチ カルレヨ?",
            "japanese": "一緒に行きませんか?",
            "level": "初級",
            "formality": "普通",
            "usage": "友達を誘うとき",
            "relatedExpressions": ["같이 가요", "함께 가실래요?"]
        },
        {
            "id": 42,
            "situation": "提案",
            "korean": "어떠세요?",
            "reading": "オットセヨ?",
            "japanese": "いかがですか?",
            "level": "初級",
            "formality": "丁寧",
            "usage": "提案や意見を求めるとき",
            "relatedExpressions": ["어때요?", "괜찮으세요?"]
        },

        # ビジネス
        {
            "id": 43,
            "situation": "会議",
            "korean": "회의를 시작하겠습니다",
            "reading": "フェウィルル シジャカゲッスムニダ",
            "japanese": "会議を始めます",
            "level": "中級",
            "formality": "丁寧",
            "usage": "会議を開始するとき",
            "relatedExpressions": ["회의 시작할게요", "시작하도록 하겠습니다"]
        },
        {
            "id": 44,
            "situation": "報告",
            "korean": "보고드립니다",
            "reading": "ポゴドゥリムニダ",
            "japanese": "報告いたします",
            "level": "上級",
            "formality": "丁寧",
            "usage": "上司に報告するとき",
            "relatedExpressions": ["말씀드립니다", "알려드립니다"]
        },
        {
            "id": 45,
            "situation": "確認",
            "korean": "확인하셨나요?",
            "reading": "ファギナショッナヨ?",
            "japanese": "確認されましたか?",
            "level": "中級",
            "formality": "丁寧",
            "usage": "確認を求めるとき",
            "relatedExpressions": ["확인해 보셨어요?", "체크하셨어요?"]
        },

        # 時間
        {
            "id": 46,
            "situation": "時間",
            "korean": "몇 시예요?",
            "reading": "ミョッ シエヨ?",
            "japanese": "何時ですか?",
            "level": "初級",
            "formality": "普通",
            "usage": "時間を尋ねるとき",
            "relatedExpressions": ["지금 몇 시죠?", "시간이 어떻게 돼요?"]
        },
        {
            "id": 47,
            "situation": "時間",
            "korean": "늦어서 죄송해요",
            "reading": "ヌジョソ チェソンヘヨ",
            "japanese": "遅れてすみません",
            "level": "初級",
            "formality": "普通",
            "usage": "遅刻したとき",
            "relatedExpressions": ["늦었어요, 미안해요", "죄송합니다"]
        },

        # その他実用表現
        {
            "id": 48,
            "situation": "確認",
            "korean": "정말 그래요?",
            "reading": "チョンマル クレヨ?",
            "japanese": "本当にそうですか?",
            "level": "初級",
            "formality": "普通",
            "usage": "確認するとき",
            "relatedExpressions": ["진짜예요?", "확실해요?"]
        },
        {
            "id": 49,
            "situation": "理解",
            "korean": "무슨 뜻이에요?",
            "reading": "ムスン ットゥシエヨ?",
            "japanese": "どういう意味ですか?",
            "level": "初級",
            "formality": "普通",
            "usage": "意味を尋ねるとき",
            "relatedExpressions": ["이게 뭐예요?", "무슨 말이에요?"]
        },
        {
            "id": 50,
            "situation": "許可",
            "korean": "해도 돼요?",
            "reading": "ヘド ドェヨ?",
            "japanese": "してもいいですか?",
            "level": "初級",
            "formality": "普通",
            "usage": "許可を求めるとき",
            "relatedExpressions": ["해도 괜찮아요?", "괜찮을까요?"]
        }
    ]

    return expressions

def main():
    """メイン関数"""
    print("💬 韓国語表現データ生成スクリプト")
    print("=" * 50)

    # データ生成
    expressions = generate_expressions_data()

    # ファイル保存
    output_path = "../data/expressions/expressions-data.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(expressions, f, ensure_ascii=False, indent=2)

    print(f"✅ 表現データを生成しました: {output_path}")
    print(f"   総数: {len(expressions)}表現")

    # 状況別集計
    situations = {}
    for expr in expressions:
        sit = expr['situation']
        situations[sit] = situations.get(sit, 0) + 1

    print("\n📊 状況別内訳:")
    for sit, count in sorted(situations.items()):
        print(f"   {sit}: {count}個")

    print("\n✨ データ生成完了!")

if __name__ == "__main__":
    main()
