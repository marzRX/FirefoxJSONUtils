import json
import sys

# JSONファイルを読み込む
def load_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# ウィンドウとアクティブタブの情報を表示する
def display_active_tabs(data):
    # ウィンドウのリストを取得（実際のキーはファイルによって異なるかもしれません）
    windows = data.get('windows', [])
    for i, window in enumerate(windows, start=1):
        tabs = window.get('tabs', [])
        active_tab_index = window.get('selected', 1) - 1  # インデックスは0始まりなので1を引く
        if tabs:  # タブがある場合のみ
            active_tab = tabs[active_tab_index]  # アクティブなタブを取得
            entries = active_tab.get('entries', [])
            if entries:  # 履歴エントリがある場合のみ
                active_entry = entries[-1]  # 最後のエントリが現在のURL
                title = active_entry.get('title', 'No Title')
                url = active_entry.get('url', 'No URL')
                print(f"Window {i}: Active Tab - Title: {title}, URL: {url}")
            else:
                print(f"Window {i}: No active tab information available.")
        else:
            print(f"Window {i}: No tabs available.")

# メイン関数
def main():
    if len(sys.argv) != 2:
        print("Usage: python list_active_tabs.py <input.json>")
        sys.exit(1)

    filename = sys.argv[1]  # JSONファイルのパスを指定
    data = load_json_file(filename)
    display_active_tabs(data)

if __name__ == "__main__":
    main()
