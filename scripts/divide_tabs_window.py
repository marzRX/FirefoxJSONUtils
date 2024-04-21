import json
import sys

# JSONファイルを読み込む
def load_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# ウィンドウデータを新しいJSONファイルとして保存
def save_windows_data(windows_data, filename):
    data = {'windows': windows_data}
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

# アクティブなタブの情報を取得
def get_active_tab_info(window):
    tabs = window.get('tabs', [])
    active_tab_index = window.get('selected', 1) - 1
    if tabs:
        active_tab = tabs[active_tab_index]
        entries = active_tab.get('entries', [])
        if entries:
            active_entry = entries[-1]  # 最後のエントリが現在のURL
            title = active_entry.get('title', 'No Title')
            url = active_entry.get('url', 'No URL')
            return f" - Active Tab: {title} ({url})"
    return " - No active tab information available."

# 分割するウィンドウを選択し保存
def split_and_save_windows(data):
    windows = data.get('windows', [])
    for i, window in enumerate(windows, start=1):
        active_tab_info = get_active_tab_info(window)
        print(f"Window {i}{active_tab_info}")
    selected_window_numbers = input("Enter the window numbers to include in selected.json (comma separated): ")
    selected_window_numbers = [int(n.strip()) for n in selected_window_numbers.split(',')]

    # 選択されたウィンドウと残りのウィンドウを分ける
    selected_windows = [windows[n-1] for n in selected_window_numbers if 0 < n <= len(windows)]
    other_windows = [win for i, win in enumerate(windows, start=1) if i not in selected_window_numbers]

    # ファイルに保存
    save_windows_data(selected_windows, 'selected_window.json')
    save_windows_data(other_windows, 'other.json')

# メイン関数
def main():
    if len(sys.argv) != 2:
        print("Usage: python divide_tabs_window.py <input.json>")
        sys.exit(1)

    filename = sys.argv[1]  # JSONファイルのパスを指定
    data = load_json_file(filename)
    split_and_save_windows(data)

if __name__ == "__main__":
    main()
