# にじさんじ共通テスト清陵祭2026統計サイト
## 概要
このレポジトリは、2026年清陵祭で実施したにじさんじ共通テストの統計データをまとめるstreamlitを管理するレポジトリです
## 各ツール解説
### .pyファイル
- app.py
  - streamlitの起動ベースとなるファイル。各種モジュールファイルから関数を取得してページを構成している
- setting.py
  - CSSやHTMLを用いてサイト設定を行うモジュールを格納したファイル。背景画像、ページフォント、BGMなどを管理している
- Google_Sheets.py
  - Google spreadsheetからデータを持ってくるモジュールを格納したファイル。Google APIを用いてデータを持ってきている。
- calc.py
  - 持ってきたデータをもとに採点、統計データの算出を行うモジュール
- main.py
  - メインページのstreamlitデータを保管しているファイル
- whole_analysis.py
  - 全体統計ページのstreamlitデータを保管しているファイル
- rate_question.py
  - 問題別統計ページのstreamlitデータを保管しているファイル
- ranking.py
  - ランキングページのstreamlitデータを保管しているファイル
### その他のファイル
- answer.json
  - フォームの問題と回答の対応を記録したjsonファイル
- image.png
  - サイトの背景画像