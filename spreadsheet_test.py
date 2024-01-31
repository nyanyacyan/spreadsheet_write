# デバック実行ファイル
# 開発段階=> スプレッドシートを動かすのみ

# 開発段階終了=> インスタンス=> autoLoginHeadless=> Spreadsheetで読み取る
from dotenv import load_dotenv
import os

# 自作モジュール
from spreadsheet_write import Spreadsheet_write
from spreadsheet_read import Spreadsheet_read



load_dotenv()  # .env ファイルから環境変数を読み込む
debug_mode = os.getenv('DEBUG_MODE', 'False') == 'True'  # 環境変数からデバッグモードを取得

test_write = Spreadsheet_write(debug_mode=debug_mode)
test_read = Spreadsheet_read(debug_mode=debug_mode)


# test_write.spreadsheet_write()
test_read.spreadsheet_read()
