# デバック実行ファイル
# 開発段階=> スプレッドシートを動かすのみ

# 開発段階終了=> インスタンス=> autoLoginHeadless=> Spreadsheetで読み取る
from dotenv import load_dotenv
import os

# 自作モジュール
from debugLogger import Logger
from spreadsheet_write import Spreadsheet_write
from spreadsheet_read import Spreadsheet_read
from scraper import Scraper



load_dotenv()  # .env ファイルから環境変数を読み込む

debug_mode = os.getenv('DEBUG_MODE', 'False') == 'True'

spreadsheet_write = Spreadsheet_write(debug_mode=debug_mode)
spreadsheet_read = Spreadsheet_read(debug_mode=debug_mode)
scraper = Scraper(debug_mode=debug_mode)


# test_write.spreadsheet_write()
mix_data = Spreadsheet_read.spreadsheet_read()
scraper = scraper()

# 検索ワードに変換
for jan, name in mix_data.items():
    sarch_word = (f"{jan} {name}")
    scraper.scraper(sarch_word)

# スクレイピング実行したデータをスプレッドシートに書き込む