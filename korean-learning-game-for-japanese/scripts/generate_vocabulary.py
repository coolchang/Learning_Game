#!/usr/bin/env python3
"""
韓国語学習ゲーム - 語彙データ生成スクリプト

このスクリプトは、レベル別の韓国語語彙データを生成します。
日本人学習者向けに、読み方（カタカナ）と例文を含みます。
"""

import json
import os

def generate_vocabulary_by_level():
    """
    レベル別語彙データを生成する

    Returns:
        dict: レベル別の語彙データ
    """

    # 初級語彙データ
    beginner_words = [
        {
            "korean": "안녕하세요",
            "reading": "アンニョンハセヨ",
            "meaning": "こんにちは",
            "type": "挨拶",
            "example": "안녕하세요, 만나서 반갑습니다",
            "exampleTranslation": "こんにちは、お会いできて嬉しいです"
        },
        {
            "korean": "감사합니다",
            "reading": "カムサハムニダ",
            "meaning": "ありがとうございます",
            "type": "挨拶",
            "example": "도와주셔서 감사합니다",
            "exampleTranslation": "助けていただきありがとうございます"
        },
        {
            "korean": "네",
            "reading": "ネ",
            "meaning": "はい",
            "type": "返事",
            "example": "네, 알겠습니다",
            "exampleTranslation": "はい、わかりました"
        },
        {
            "korean": "아니요",
            "reading": "アニヨ",
            "meaning": "いいえ",
            "type": "返事",
            "example": "아니요, 괜찮아요",
            "exampleTranslation": "いいえ、大丈夫です"
        },
        {
            "korean": "사랑",
            "reading": "サラン",
            "meaning": "愛",
            "type": "名詞",
            "example": "사랑이 필요해요",
            "exampleTranslation": "愛が必要です"
        }
    ]

    # 中級語彙データ
    intermediate_words = [
        {
            "korean": "행복",
            "reading": "ヘンボク",
            "meaning": "幸せ",
            "type": "名詞",
            "example": "행복한 하루 보내세요",
            "exampleTranslation": "幸せな一日をお過ごしください"
        },
        {
            "korean": "노력",
            "reading": "ノリョク",
            "meaning": "努力",
            "type": "名詞",
            "example": "노력하면 성공할 수 있어요",
            "exampleTranslation": "努力すれば成功できます"
        },
        {
            "korean": "여행",
            "reading": "ヨヘン",
            "meaning": "旅行",
            "type": "名詞",
            "example": "한국 여행을 갔어요",
            "exampleTranslation": "韓国旅行に行きました"
        },
        {
            "korean": "문화",
            "reading": "ムンファ",
            "meaning": "文化",
            "type": "名詞",
            "example": "한국 문화를 배워요",
            "exampleTranslation": "韓国文化を学びます"
        },
        {
            "korean": "경험",
            "reading": "キョンホム",
            "meaning": "経験",
            "type": "名詞",
            "example": "좋은 경験이었어요",
            "exampleTranslation": "良い経験でした"
        }
    ]

    # 上級語彙データ
    advanced_words = [
        {
            "korean": "성취감",
            "reading": "ソンチュィガム",
            "meaning": "達成感",
            "type": "名詞",
            "example": "큰 성취감을 느꼈어요",
            "exampleTranslation": "大きな達成感を感じました"
        },
        {
            "korean": "인내심",
            "reading": "インネシム",
            "meaning": "忍耐力",
            "type": "名詞",
            "example": "인내심이 필요합니다",
            "exampleTranslation": "忍耐力が必要です"
        },
        {
            "korean": "협력",
            "reading": "ヒョプリョク",
            "meaning": "協力",
            "type": "名詞",
            "example": "팀워크와 협력이 중요해요",
            "exampleTranslation": "チームワークと協力が重要です"
        },
        {
            "korean": "창의성",
            "reading": "チャンウィソン",
            "meaning": "創造性",
            "type": "名詞",
            "example": "창의성을 발휘하세요",
            "exampleTranslation": "創造性を発揮してください"
        },
        {
            "korean": "효율성",
            "reading": "ヒョユルソン",
            "meaning": "効率性",
            "type": "名詞",
            "example": "효율성을 높이세요",
            "exampleTranslation": "効率性を高めてください"
        }
    ]

    return {
        "beginner": beginner_words,
        "intermediate": intermediate_words,
        "advanced": advanced_words
    }

def expand_vocabulary_data(base_data, target_count_per_level):
    """
    語彙データを拡張する（AIで生成することを想定）

    Args:
        base_data: 基本語彙データ
        target_count_per_level: レベルごとの目標語彙数

    Returns:
        dict: 拡張された語彙データ
    """
    # 実際のプロジェクトでは、ここでAI APIを使用して語彙を生成
    # この例では、既存のデータを繰り返すだけ

    expanded = {}

    for level, words in base_data.items():
        expanded[level] = words.copy()

        # 目標数に達するまで拡張（サンプル実装）
        while len(expanded[level]) < target_count_per_level:
            # 既存の単語をベースに新しい単語を生成
            # 実際にはAI APIを使用
            base_word = words[len(expanded[level]) % len(words)]
            new_word = base_word.copy()
            new_word["korean"] = f"{base_word['korean']} (拡張)"
            expanded[level].append(new_word)

    return expanded

def save_vocabulary_data(vocabulary, output_path):
    """
    語彙データをJSONファイルに保存

    Args:
        vocabulary: 語彙データ
        output_path: 出力ファイルパス
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(vocabulary, f, ensure_ascii=False, indent=2)

    print(f"✅ 語彙データを生成しました: {output_path}")
    for level, words in vocabulary.items():
        print(f"   {level}: {len(words)}語")

def main():
    """メイン関数"""
    print("📚 韓国語語彙データ生成スクリプト")
    print("=" * 50)

    # 基本データ生成
    base_vocabulary = generate_vocabulary_by_level()

    # データ拡張（オプション）
    # expanded_vocabulary = expand_vocabulary_data(base_vocabulary, target_count_per_level=50)

    # ファイル保存
    output_path = "../data/vocabulary/vocabulary-data.json"
    save_vocabulary_data(base_vocabulary, output_path)

    print("\n✨ データ生成完了!")
    print("\n💡 ヒント:")
    print("   - より多くの語彙を生成するには、AI APIを使用してください")
    print("   - expand_vocabulary_data() 関数をカスタマイズできます")

if __name__ == "__main__":
    main()
