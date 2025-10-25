#!/usr/bin/env python3
"""
韓国語学習ゲーム - 歌データ生成スクリプト

このスクリプトは、K-POP歌詞データを生成します。
日本人学習者向けに、発音ガイドと日本語訳を含みます。
"""

import json
import os

def generate_song_data(count=10):
    """
    歌データを生成する

    Args:
        count: 生成する歌の数

    Returns:
        list: 歌データのリスト
    """

    # サンプル単語リスト
    common_words = [
        {"korean": "사랑", "japanese": "愛", "reading": "サラン"},
        {"korean": "마음", "japanese": "心", "reading": "マウム"},
        {"korean": "그리움", "japanese": "懐かしさ", "reading": "クリウム"},
        {"korean": "행복", "japanese": "幸せ", "reading": "ヘンボク"},
        {"korean": "슬픔", "japanese": "悲しみ", "reading": "スルプム"},
        {"korean": "기쁨", "japanese": "喜び", "reading": "キップム"},
        {"korean": "영원", "japanese": "永遠", "reading": "ヨンウォン"},
        {"korean": "순간", "japanese": "瞬間", "reading": "スンガン"},
        {"korean": "기억", "japanese": "記憶", "reading": "キオク"},
        {"korean": "약속", "japanese": "約束", "reading": "ヤクソク"}
    ]

    songs = []

    for i in range(count):
        song = {
            "id": i + 1,
            "title": f"샘플 노래 {i + 1}",
            "artist": "サンプルアーティスト",
            "level": "初級" if i < 3 else "中級" if i < 7 else "上級",
            "lyrics": [],
            "pronunciationTips": []
        }

        # 歌詞を4行生成
        for j in range(4):
            word = common_words[j % len(common_words)]
            lyric = {
                "korean": f"{word['korean']}을 느껴요 {{" + word['korean'] + "}}",
                "japanese": f"{word['japanese']}を感じます",
                "blanks": [word['korean']]
            }
            song["lyrics"].append(lyric)

        # 発音ガイドを追加
        for j in range(2):
            word = common_words[j % len(common_words)]
            tip = {
                "word": word['korean'],
                "tip": f"「{word['reading']}」の発音に注意してください",
                "difficulty": "medium" if i < 5 else "hard"
            }
            song["pronunciationTips"].append(tip)

        songs.append(song)

    return songs

def save_songs_data(songs, output_path):
    """
    歌データをJSONファイルに保存

    Args:
        songs: 歌データのリスト
        output_path: 出力ファイルパス
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(songs, f, ensure_ascii=False, indent=2)

    print(f"✅ 歌データを生成しました: {output_path}")
    print(f"   総数: {len(songs)}曲")

def main():
    """メイン関数"""
    print("🎵 K-POP歌詞データ生成スクリプト")
    print("=" * 50)

    # データ生成
    songs = generate_song_data(count=10)

    # ファイル保存
    output_path = "../data/songs/songs-data.json"
    save_songs_data(songs, output_path)

    print("\n✨ データ生成完了!")

if __name__ == "__main__":
    main()
