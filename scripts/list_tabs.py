import json
import sys

def load_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def display_tabs(data):
    for window_index, window in enumerate(data.get('windows', []), start=1):
        print(f"Window {window_index}:")
        for tab_index, tab in enumerate(window.get('tabs', []), start=1):
            tab_title = tab.get('entries', [{'title': 'No title'}])[-1]['title']
            tab_url = tab.get('entries', [{'url': 'No URL'}])[-1]['url']
            print(f"\tTab {tab_index}: Title = {tab_title}, URL = {tab_url}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python list_tabs.py <input.json>")
        sys.exit(1)

    filename = sys.argv[1]  # JSONファイルのパスを指定
    data = load_json_file(filename)
    display_tabs(data)

if __name__ == "__main__":
    main()
