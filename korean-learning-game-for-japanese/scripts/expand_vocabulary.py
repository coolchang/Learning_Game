#!/usr/bin/env python3
"""
韓国語語彙データ拡張スクリプト
各レベル50語まで拡張
"""

import json
import os

def generate_expanded_vocabulary():
    """拡張された語彙データを生成"""

    # 初級語彙 (50語)
    beginner_words = [
        # 挨拶・基本表現
        {"korean": "안녕하세요", "reading": "アンニョンハセヨ", "meaning": "こんにちは", "type": "挨拶", "example": "안녕하세요, 만나서 반갑습니다", "exampleTranslation": "こんにちは、お会いできて嬉しいです"},
        {"korean": "감사합니다", "reading": "カムサハムニダ", "meaning": "ありがとうございます", "type": "挨拶", "example": "도와주셔서 감사합니다", "exampleTranslation": "助けていただきありがとうございます"},
        {"korean": "안녕히 가세요", "reading": "アンニョンヒ カセヨ", "meaning": "さようなら(見送る)", "type": "挨拶", "example": "안녕히 가세요, 조심해서 가세요", "exampleTranslation": "さようなら、気をつけて"},
        {"korean": "안녕히 계세요", "reading": "アンニョンヒ ケセヨ", "meaning": "さようなら(去る)", "type": "挨拶", "example": "안녕히 계세요, 또 뵙겠습니다", "exampleTranslation": "さようなら、またお会いしましょう"},
        {"korean": "죄송합니다", "reading": "チェソンハムニダ", "meaning": "申し訳ございません", "type": "挨拶", "example": "늦어서 죄송합니다", "exampleTranslation": "遅れて申し訳ございません"},
        {"korean": "미안해요", "reading": "ミアネヨ", "meaning": "ごめんなさい", "type": "挨拶", "example": "미안해요, 실수했어요", "exampleTranslation": "ごめんなさい、間違えました"},
        {"korean": "괜찮아요", "reading": "クェンチャナヨ", "meaning": "大丈夫です", "type": "挨拶", "example": "괜찮아요, 걱정하지 마세요", "exampleTranslation": "大丈夫です、心配しないでください"},
        {"korean": "네", "reading": "ネ", "meaning": "はい", "type": "返事", "example": "네, 알겠습니다", "exampleTranslation": "はい、わかりました"},
        {"korean": "아니요", "reading": "アニヨ", "meaning": "いいえ", "type": "返事", "example": "아니요, 괜찮아요", "exampleTranslation": "いいえ、大丈夫です"},
        {"korean": "잘 부탁합니다", "reading": "チャル プタカムニダ", "meaning": "よろしくお願いします", "type": "挨拶", "example": "앞으로 잘 부탁합니다", "exampleTranslation": "今後ともよろしくお願いします"},

        # 人・家族
        {"korean": "사람", "reading": "サラム", "meaning": "人", "type": "名詞", "example": "좋은 사람이에요", "exampleTranslation": "良い人です"},
        {"korean": "친구", "reading": "チング", "meaning": "友達", "type": "名詞", "example": "친구를 만나요", "exampleTranslation": "友達に会います"},
        {"korean": "가족", "reading": "カジョク", "meaning": "家族", "type": "名詞", "example": "가족이 중요해요", "exampleTranslation": "家族が大切です"},
        {"korean": "아버지", "reading": "アボジ", "meaning": "父", "type": "名詞", "example": "아버지는 회사원이에요", "exampleTranslation": "父は会社員です"},
        {"korean": "어머니", "reading": "オモニ", "meaning": "母", "type": "名詞", "example": "어머니는 요리를 잘해요", "exampleTranslation": "母は料理が上手です"},
        {"korean": "형", "reading": "ヒョン", "meaning": "兄(男性から)", "type": "名詞", "example": "형이 두 명 있어요", "exampleTranslation": "兄が2人います"},
        {"korean": "오빠", "reading": "オッパ", "meaning": "兄(女性から)", "type": "名詞", "example": "오빠가 학생이에요", "exampleTranslation": "お兄さんは学生です"},
        {"korean": "누나", "reading": "ヌナ", "meaning": "姉(男性から)", "type": "名詞", "example": "누나는 의사예요", "exampleTranslation": "姉は医者です"},
        {"korean": "언니", "reading": "オンニ", "meaning": "姉(女性から)", "type": "名詞", "example": "언니와 쇼핑해요", "exampleTranslation": "姉と買い物します"},
        {"korean": "동생", "reading": "トンセン", "meaning": "弟・妹", "type": "名詞", "example": "동생이 귀여워요", "exampleTranslation": "弟/妹が可愛いです"},

        # 場所
        {"korean": "집", "reading": "チプ", "meaning": "家", "type": "名詞", "example": "집에 가요", "exampleTranslation": "家に帰ります"},
        {"korean": "학교", "reading": "ハッキョ", "meaning": "学校", "type": "名詞", "example": "학교에 가요", "exampleTranslation": "学校に行きます"},
        {"korean": "회사", "reading": "フェサ", "meaning": "会社", "type": "名詞", "example": "회사에서 일해요", "exampleTranslation": "会社で働きます"},
        {"korean": "식당", "reading": "シクタン", "meaning": "食堂・レストラン", "type": "名詞", "example": "식당에서 밥을 먹어요", "exampleTranslation": "食堂でご飯を食べます"},
        {"korean": "카페", "reading": "カペ", "meaning": "カフェ", "type": "名詞", "example": "카페에서 커피를 마셔요", "exampleTranslation": "カフェでコーヒーを飲みます"},
        {"korean": "병원", "reading": "ピョンウォン", "meaning": "病院", "type": "名詞", "example": "병원에 가요", "exampleTranslation": "病院に行きます"},
        {"korean": "은행", "reading": "ウネン", "meaning": "銀行", "type": "名詞", "example": "은행에서 돈을 찾아요", "exampleTranslation": "銀行でお金を下ろします"},
        {"korean": "공원", "reading": "コンウォン", "meaning": "公園", "type": "名詞", "example": "공원에서 산책해요", "exampleTranslation": "公園で散歩します"},
        {"korean": "시장", "reading": "シジャン", "meaning": "市場", "type": "名詞", "example": "시장에서 장을 봐요", "exampleTranslation": "市場で買い物します"},
        {"korean": "백화점", "reading": "ペカジョム", "meaning": "百貨店", "type": "名詞", "example": "백화점에서 쇼핑해요", "exampleTranslation": "百貨店でショッピングします"},

        # 時間
        {"korean": "시간", "reading": "シガン", "meaning": "時間", "type": "名詞", "example": "시간이 없어요", "exampleTranslation": "時間がありません"},
        {"korean": "오늘", "reading": "オヌル", "meaning": "今日", "type": "名詞", "example": "오늘은 날씨가 좋아요", "exampleTranslation": "今日は天気が良いです"},
        {"korean": "어제", "reading": "オジェ", "meaning": "昨日", "type": "名詞", "example": "어제 친구를 만났어요", "exampleTranslation": "昨日友達に会いました"},
        {"korean": "내일", "reading": "ネイル", "meaning": "明日", "type": "名詞", "example": "내일 시험이 있어요", "exampleTranslation": "明日試験があります"},
        {"korean": "아침", "reading": "アチム", "meaning": "朝", "type": "名詞", "example": "아침에 일어나요", "exampleTranslation": "朝起きます"},
        {"korean": "점심", "reading": "チョムシム", "meaning": "昼", "type": "名詞", "example": "점심을 먹어요", "exampleTranslation": "昼食を食べます"},
        {"korean": "저녁", "reading": "チョニョク", "meaning": "夕方・夜", "type": "名詞", "example": "저녁에 만나요", "exampleTranslation": "夕方に会います"},
        {"korean": "밤", "reading": "パム", "meaning": "夜", "type": "名詞", "example": "밤에 자요", "exampleTranslation": "夜寝ます"},

        # 食べ物・飲み物
        {"korean": "음식", "reading": "ウムシク", "meaning": "食べ物", "type": "名詞", "example": "한국 음식을 좋아해요", "exampleTranslation": "韓国料理が好きです"},
        {"korean": "밥", "reading": "パプ", "meaning": "ご飯", "type": "名詞", "example": "밥을 먹어요", "exampleTranslation": "ご飯を食べます"},
        {"korean": "물", "reading": "ムル", "meaning": "水", "type": "名詞", "example": "물을 마셔요", "exampleTranslation": "水を飲みます"},
        {"korean": "커피", "reading": "コピ", "meaning": "コーヒー", "type": "名詞", "example": "커피를 좋아해요", "exampleTranslation": "コーヒーが好きです"},
        {"korean": "차", "reading": "チャ", "meaning": "お茶", "type": "名詞", "example": "차를 마셔요", "exampleTranslation": "お茶を飲みます"},
        {"korean": "빵", "reading": "パン", "meaning": "パン", "type": "名詞", "example": "빵을 먹어요", "exampleTranslation": "パンを食べます"},

        # 基本動詞・形容詞
        {"korean": "가다", "reading": "カダ", "meaning": "行く", "type": "動詞", "example": "학교에 가요", "exampleTranslation": "学校に行きます"},
        {"korean": "오다", "reading": "オダ", "meaning": "来る", "type": "動詞", "example": "친구가 와요", "exampleTranslation": "友達が来ます"},
        {"korean": "먹다", "reading": "モクタ", "meaning": "食べる", "type": "動詞", "example": "밥을 먹어요", "exampleTranslation": "ご飯を食べます"},
        {"korean": "마시다", "reading": "マシダ", "meaning": "飲む", "type": "動詞", "example": "물을 마셔요", "exampleTranslation": "水を飲みます"},
        {"korean": "자다", "reading": "チャダ", "meaning": "寝る", "type": "動詞", "example": "밤에 자요", "exampleTranslation": "夜寝ます"},
        {"korean": "좋다", "reading": "チョタ", "meaning": "良い", "type": "形容詞", "example": "날씨가 좋아요", "exampleTranslation": "天気が良いです"},
        {"korean": "크다", "reading": "クダ", "meaning": "大きい", "type": "形容詞", "example": "집이 커요", "exampleTranslation": "家が大きいです"}
    ]

    # 中級語彙 (50語)
    intermediate_words = [
        # 感情・心理
        {"korean": "행복", "reading": "ヘンボク", "meaning": "幸せ", "type": "名詞", "example": "행복한 하루 보내세요", "exampleTranslation": "幸せな一日をお過ごしください"},
        {"korean": "사랑", "reading": "サラン", "meaning": "愛", "type": "名詞", "example": "사랑이 필요해요", "exampleTranslation": "愛が必要です"},
        {"korean": "기쁨", "reading": "キップム", "meaning": "喜び", "type": "名詞", "example": "큰 기쁨을 느껴요", "exampleTranslation": "大きな喜びを感じます"},
        {"korean": "슬픔", "reading": "スルプム", "meaning": "悲しみ", "type": "名詞", "example": "슬픔을 이겨내요", "exampleTranslation": "悲しみを乗り越えます"},
        {"korean": "화", "reading": "ファ", "meaning": "怒り", "type": "名詞", "example": "화가 나요", "exampleTranslation": "怒りが出ます"},
        {"korean": "두려움", "reading": "トゥリョウム", "meaning": "恐れ", "type": "名詞", "example": "두려움을 극복해요", "exampleTranslation": "恐れを克服します"},
        {"korean": "희망", "reading": "フィマン", "meaning": "希望", "type": "名詞", "example": "희망을 가져요", "exampleTranslation": "希望を持ちます"},
        {"korean": "걱정", "reading": "コクチョン", "meaning": "心配", "type": "名詞", "example": "걱정하지 마세요", "exampleTranslation": "心配しないでください"},
        {"korean": "외로움", "reading": "ウェロウム", "meaning": "寂しさ", "type": "名詞", "example": "외로움을 느껴요", "exampleTranslation": "寂しさを感じます"},
        {"korean": "그리움", "reading": "クリウム", "meaning": "恋しさ", "type": "名詞", "example": "고향에 대한 그리움", "exampleTranslation": "故郷への恋しさ"},

        # 活動・行動
        {"korean": "여행", "reading": "ヨヘン", "meaning": "旅行", "type": "名詞", "example": "한국 여행을 갔어요", "exampleTranslation": "韓国旅行に行きました"},
        {"korean": "운동", "reading": "ウンドン", "meaning": "運動", "type": "名詞", "example": "매일 운동해요", "exampleTranslation": "毎日運動します"},
        {"korean": "공부", "reading": "コンブ", "meaning": "勉強", "type": "名詞", "example": "한국어를 공부해요", "exampleTranslation": "韓国語を勉強します"},
        {"korean": "일", "reading": "イル", "meaning": "仕事", "type": "名詞", "example": "일이 많아요", "exampleTranslation": "仕事が多いです"},
        {"korean": "쇼핑", "reading": "ショピン", "meaning": "買い物", "type": "名詞", "example": "주말에 쇼핑해요", "exampleTranslation": "週末に買い物します"},
        {"korean": "요리", "reading": "ヨリ", "meaning": "料理", "type": "名詞", "example": "요리를 배워요", "exampleTranslation": "料理を習います"},
        {"korean": "독서", "reading": "トクソ", "meaning": "読書", "type": "名詞", "example": "독서를 좋아해요", "exampleTranslation": "読書が好きです"},
        {"korean": "영화", "reading": "ヨンファ", "meaning": "映画", "type": "名詞", "example": "영화를 봐요", "exampleTranslation": "映画を見ます"},
        {"korean": "음악", "reading": "ウマク", "meaning": "音楽", "type": "名詞", "example": "음악을 들어요", "exampleTranslation": "音楽を聴きます"},
        {"korean": "게임", "reading": "ケイム", "meaning": "ゲーム", "type": "名詞", "example": "게임을 해요", "exampleTranslation": "ゲームをします"},

        # 社会・文化
        {"korean": "문화", "reading": "ムンファ", "meaning": "文化", "type": "名詞", "example": "한국 문화를 배워요", "exampleTranslation": "韓国文化を学びます"},
        {"korean": "역사", "reading": "ヨクサ", "meaning": "歴史", "type": "名詞", "example": "역사를 공부해요", "exampleTranslation": "歴史を勉強します"},
        {"korean": "전통", "reading": "チョントン", "meaning": "伝統", "type": "名詞", "example": "전통을 지켜요", "exampleTranslation": "伝統を守ります"},
        {"korean": "사회", "reading": "サフェ", "meaning": "社会", "type": "名詞", "example": "사회가 변해요", "exampleTranslation": "社会が変わります"},
        {"korean": "경제", "reading": "キョンジェ", "meaning": "経済", "type": "名詞", "example": "경제가 어려워요", "exampleTranslation": "経済が難しいです"},
        {"korean": "정치", "reading": "チョンチ", "meaning": "政治", "type": "名詞", "example": "정치에 관심이 있어요", "exampleTranslation": "政治に関心があります"},
        {"korean": "교육", "reading": "キョユク", "meaning": "教育", "type": "名詞", "example": "교육이 중요해요", "exampleTranslation": "教育が重要です"},
        {"korean": "과학", "reading": "クァハク", "meaning": "科学", "type": "名詞", "example": "과학을 좋아해요", "exampleTranslation": "科学が好きです"},
        {"korean": "기술", "reading": "キスル", "meaning": "技術", "type": "名詞", "example": "기술이 발전해요", "exampleTranslation": "技術が発展します"},
        {"korean": "예술", "reading": "イェスル", "meaning": "芸術", "type": "名詞", "example": "예술을 감상해요", "exampleTranslation": "芸術を鑑賞します"},

        # 自然・環境
        {"korean": "자연", "reading": "チャヨン", "meaning": "自然", "type": "名詞", "example": "자연이 아름다워요", "exampleTranslation": "自然が美しいです"},
        {"korean": "환경", "reading": "ファンギョン", "meaning": "環境", "type": "名詞", "example": "환경을 보호해요", "exampleTranslation": "環境を保護します"},
        {"korean": "날씨", "reading": "ナルシ", "meaning": "天気", "type": "名詞", "example": "날씨가 좋아요", "exampleTranslation": "天気が良いです"},
        {"korean": "계절", "reading": "ケジョル", "meaning": "季節", "type": "名詞", "example": "좋아하는 계절이 뭐예요?", "exampleTranslation": "好きな季節は何ですか?"},
        {"korean": "봄", "reading": "ポム", "meaning": "春", "type": "名詞", "example": "봄이 왔어요", "exampleTranslation": "春が来ました"},
        {"korean": "여름", "reading": "ヨルム", "meaning": "夏", "type": "名詞", "example": "여름이 더워요", "exampleTranslation": "夏が暑いです"},
        {"korean": "가을", "reading": "カウル", "meaning": "秋", "type": "名詞", "example": "가을이 시원해요", "exampleTranslation": "秋が涼しいです"},
        {"korean": "겨울", "reading": "キョウル", "meaning": "冬", "type": "名詞", "example": "겨울이 추워요", "exampleTranslation": "冬が寒いです"},
        {"korean": "바다", "reading": "パダ", "meaning": "海", "type": "名詞", "example": "바다에 가요", "exampleTranslation": "海に行きます"},
        {"korean": "산", "reading": "サン", "meaning": "山", "type": "名詞", "example": "산을 올라요", "exampleTranslation": "山に登ります"},

        # 抽象概念
        {"korean": "경험", "reading": "キョンホム", "meaning": "経験", "type": "名詞", "example": "좋은 경험이었어요", "exampleTranslation": "良い経験でした"},
        {"korean": "노력", "reading": "ノリョク", "meaning": "努力", "type": "名詞", "example": "노력하면 성공해요", "exampleTranslation": "努力すれば成功します"},
        {"korean": "건강", "reading": "コンガン", "meaning": "健康", "type": "名詞", "example": "건강이 중요해요", "exampleTranslation": "健康が大切です"},
        {"korean": "미래", "reading": "ミレ", "meaning": "未来", "type": "名詞", "example": "미래가 기대돼요", "exampleTranslation": "未来が楽しみです"},
        {"korean": "과거", "reading": "クァゴ", "meaning": "過去", "type": "名詞", "example": "과거를 돌아봐요", "exampleTranslation": "過去を振り返ります"},
        {"korean": "현재", "reading": "ヒョンジェ", "meaning": "現在", "type": "名詞", "example": "현재에 집중해요", "exampleTranslation": "現在に集中します"},
        {"korean": "기회", "reading": "キフェ", "meaning": "機会", "type": "名詞", "example": "좋은 기회예요", "exampleTranslation": "良い機会です"},
        {"korean": "계획", "reading": "ケフェク", "meaning": "計画", "type": "名詞", "example": "계획을 세워요", "exampleTranslation": "計画を立てます"},
        {"korean": "목표", "reading": "モクピョ", "meaning": "目標", "type": "名詞", "example": "목표를 달성해요", "exampleTranslation": "目標を達成します"},
        {"korean": "꿈", "reading": "ックム", "meaning": "夢", "type": "名詞", "example": "꿈을 이뤄요", "exampleTranslation": "夢を叶えます"}
    ]

    # 上級語彙 (50語)
    advanced_words = [
        # 高度な抽象概念
        {"korean": "성취감", "reading": "ソンチュィガム", "meaning": "達成感", "type": "名詞", "example": "큰 성취감을 느꼈어요", "exampleTranslation": "大きな達成感を感じました"},
        {"korean": "인내심", "reading": "インネシム", "meaning": "忍耐力", "type": "名詞", "example": "인내심이 필요합니다", "exampleTranslation": "忍耐力が必要です"},
        {"korean": "협력", "reading": "ヒョプリョク", "meaning": "協力", "type": "名詞", "example": "팀워크와 협력이 중요해요", "exampleTranslation": "チームワークと協力が重要です"},
        {"korean": "창의성", "reading": "チャンウィソン", "meaning": "創造性", "type": "名詞", "example": "창의성을 발휘하세요", "exampleTranslation": "創造性を発揮してください"},
        {"korean": "효율성", "reading": "ヒョユルソン", "meaning": "効率性", "type": "名詞", "example": "효율성을 높이세요", "exampleTranslation": "効率性を高めてください"},
        {"korean": "책임감", "reading": "チェギムガム", "meaning": "責任感", "type": "名詞", "example": "강한 책임감이 필요해요", "exampleTranslation": "強い責任感が必要です"},
        {"korean": "전문성", "reading": "チョンムンソン", "meaning": "専門性", "type": "名詞", "example": "전문성을 키워요", "exampleTranslation": "専門性を育てます"},
        {"korean": "다양성", "reading": "タヤンソン", "meaning": "多様性", "type": "名詞", "example": "다양성을 존중해요", "exampleTranslation": "多様性を尊重します"},
        {"korean": "지속가능성", "reading": "チソクカヌンソン", "meaning": "持続可能性", "type": "名詞", "example": "지속가능성이 중요해요", "exampleTranslation": "持続可能性が重要です"},
        {"korean": "투명성", "reading": "トゥミョンソン", "meaning": "透明性", "type": "名詞", "example": "투명성을 확보해요", "exampleTranslation": "透明性を確保します"},

        # ビジネス・経営
        {"korean": "경영", "reading": "キョンヨン", "meaning": "経営", "type": "名詞", "example": "회사를 경영해요", "exampleTranslation": "会社を経営します"},
        {"korean": "전략", "reading": "チョンニャク", "meaning": "戦略", "type": "名詞", "example": "마케팅 전략을 세워요", "exampleTranslation": "マーケティング戦略を立てます"},
        {"korean": "혁신", "reading": "ヒョクシン", "meaning": "革新", "type": "名詞", "example": "혁신이 필요해요", "exampleTranslation": "革新が必要です"},
        {"korean": "경쟁력", "reading": "キョンジェンリョク", "meaning": "競争力", "type": "名詞", "example": "경쟁력을 강화해요", "exampleTranslation": "競争力を強化します"},
        {"korean": "생산성", "reading": "センサンソン", "meaning": "生産性", "type": "名詞", "example": "생산성을 높여요", "exampleTranslation": "生産性を高めます"},
        {"korean": "수익성", "reading": "スイクソン", "meaning": "収益性", "type": "名詞", "example": "수익성이 개선됐어요", "exampleTranslation": "収益性が改善されました"},
        {"korean": "투자", "reading": "トゥジャ", "meaning": "投資", "type": "名詞", "example": "미래에 투자해요", "exampleTranslation": "未来に投資します"},
        {"korean": "개발", "reading": "ケバル", "meaning": "開発", "type": "名詞", "example": "신제품을 개발해요", "exampleTranslation": "新製品を開発します"},
        {"korean": "마케팅", "reading": "マケティン", "meaning": "マーケティング", "type": "名詞", "example": "마케팅 전략이 중요해요", "exampleTranslation": "マーケティング戦略が重要です"},
        {"korean": "브랜드", "reading": "ブレンドゥ", "meaning": "ブランド", "type": "名詞", "example": "브랜드 가치를 높여요", "exampleTranslation": "ブランド価値を高めます"},

        # 学術・研究
        {"korean": "연구", "reading": "ヨング", "meaning": "研究", "type": "名詞", "example": "연구를 진행해요", "exampleTranslation": "研究を進めます"},
        {"korean": "분석", "reading": "プンソク", "meaning": "分析", "type": "名詞", "example": "데이터를 분석해요", "exampleTranslation": "データを分析します"},
        {"korean": "이론", "reading": "イロン", "meaning": "理論", "type": "名詞", "example": "이론을 배워요", "exampleTranslation": "理論を学びます"},
        {"korean": "가설", "reading": "カソル", "meaning": "仮説", "type": "名詞", "example": "가설을 세워요", "exampleTranslation": "仮説を立てます"},
        {"korean": "검증", "reading": "コムジュン", "meaning": "検証", "type": "名詞", "example": "결과를 검증해요", "exampleTranslation": "結果を検証します"},
        {"korean": "실험", "reading": "シロム", "meaning": "実験", "type": "名詞", "example": "실험을 해요", "exampleTranslation": "実験をします"},
        {"korean": "관찰", "reading": "クァンチャル", "meaning": "観察", "type": "名詞", "example": "현상을 관찰해요", "exampleTranslation": "現象を観察します"},
        {"korean": "논문", "reading": "ノンムン", "meaning": "論文", "type": "名詞", "example": "논문을 써요", "exampleTranslation": "論文を書きます"},
        {"korean": "발표", "reading": "パルピョ", "meaning": "発表", "type": "名詞", "example": "연구 결과를 발표해요", "exampleTranslation": "研究結果を発表します"},
        {"korean": "학술", "reading": "ハクスル", "meaning": "学術", "type": "名詞", "example": "학술 대회에 참가해요", "exampleTranslation": "学術大会に参加します"},

        # 社会問題
        {"korean": "불평등", "reading": "プルピョンドン", "meaning": "不平等", "type": "名詞", "example": "불평등을 해소해요", "exampleTranslation": "不平等を解消します"},
        {"korean": "차별", "reading": "チャビョル", "meaning": "差別", "type": "名詞", "example": "차별을 없애요", "exampleTranslation": "差別をなくします"},
        {"korean": "갈등", "reading": "カルトゥン", "meaning": "葛藤", "type": "名詞", "example": "갈등을 해결해요", "exampleTranslation": "葛藤を解決します"},
        {"korean": "빈곤", "reading": "ピンゴン", "meaning": "貧困", "type": "名詞", "example": "빈곤을 퇴치해요", "exampleTranslation": "貧困を退治します"},
        {"korean": "복지", "reading": "ポクチ", "meaning": "福祉", "type": "名詞", "example": "복지가 중요해요", "exampleTranslation": "福祉が重要です"},
        {"korean": "인권", "reading": "インクォン", "meaning": "人権", "type": "名詞", "example": "인권을 보호해요", "exampleTranslation": "人権を保護します"},
        {"korean": "평등", "reading": "ピョンドン", "meaning": "平等", "type": "名詞", "example": "평등을 실현해요", "exampleTranslation": "平等を実現します"},
        {"korean": "정의", "reading": "チョンウィ", "meaning": "正義", "type": "名詞", "example": "정의를 추구해요", "exampleTranslation": "正義を追求します"},
        {"korean": "공정", "reading": "コンジョン", "meaning": "公正", "type": "名詞", "example": "공정한 사회를 만들어요", "exampleTranslation": "公正な社会を作ります"},
        {"korean": "윤리", "reading": "ユンニ", "meaning": "倫理", "type": "名詞", "example": "윤리가 중요해요", "exampleTranslation": "倫理が重要です"},

        # 技術・IT
        {"korean": "인공지능", "reading": "インゴンジヌン", "meaning": "人工知能", "type": "名詞", "example": "인공지능이 발전해요", "exampleTranslation": "人工知能が発展します"},
        {"korean": "디지털", "reading": "ディジタル", "meaning": "デジタル", "type": "名詞", "example": "디지털 시대예요", "exampleTranslation": "デジタル時代です"},
        {"korean": "네트워크", "reading": "ネトゥウォク", "meaning": "ネットワーク", "type": "名詞", "example": "네트워크를 구축해요", "exampleTranslation": "ネットワークを構築します"},
        {"korean": "플랫폼", "reading": "プルレトポム", "meaning": "プラットフォーム", "type": "名詞", "example": "온라인 플랫폼이에요", "exampleTranslation": "オンラインプラットフォームです"},
        {"korean": "알고리즘", "reading": "アルゴリジュム", "meaning": "アルゴリズム", "type": "名詞", "example": "알고리즘을 개발해요", "exampleTranslation": "アルゴリズムを開発します"},
        {"korean": "데이터", "reading": "デイト", "meaning": "データ", "type": "名詞", "example": "데이터를 수집해요", "exampleTranslation": "データを収集します"},
        {"korean": "보안", "reading": "ポアン", "meaning": "セキュリティ", "type": "名詞", "example": "보안이 중요해요", "exampleTranslation": "セキュリティが重要です"},
        {"korean": "암호화", "reading": "アムホファ", "meaning": "暗号化", "type": "名詞", "example": "데이터를 암호화해요", "exampleTranslation": "データを暗号化します"},
        {"korean": "자동화", "reading": "チャドンファ", "meaning": "自動化", "type": "名詞", "example": "업무를 자동화해요", "exampleTranslation": "業務を自動化します"},
        {"korean": "최적화", "reading": "チェジョクァ", "meaning": "最適化", "type": "名詞", "example": "시스템을 최적화해요", "exampleTranslation": "システムを最適化します"}
    ]

    return {
        "beginner": beginner_words,
        "intermediate": intermediate_words,
        "advanced": advanced_words
    }

def main():
    """メイン関数"""
    print("📚 韓国語語彙データ拡張スクリプト")
    print("=" * 50)

    # 拡張データ生成
    vocabulary = generate_expanded_vocabulary()

    # ファイル保存
    output_path = "../data/vocabulary/vocabulary-data.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(vocabulary, f, ensure_ascii=False, indent=2)

    print(f"✅ 語彙データを生成しました: {output_path}")
    for level, words in vocabulary.items():
        print(f"   {level}: {len(words)}語")

    print("\n✨ データ生成完了!")

if __name__ == "__main__":
    main()
