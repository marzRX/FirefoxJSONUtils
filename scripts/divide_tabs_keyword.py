import json
import sys

def load_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_windows_data(windows_data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump({'windows': windows_data}, file, indent=4)
    print(f"Data saved to {filename}")

def filter_tabs(data, include_keywords, exclude_keywords):
    selected_windows = []
    other_windows = []
    for window in data.get('windows', []):
        new_window_selected = {'tabs': []}
        new_window_other = {'tabs': []}
        for tab in window.get('tabs', []):
            tab_title = tab.get('entries', [{'title': ''}])[-1]['title'].lower()
            tab_url = tab.get('entries', [{'url': ''}])[-1]['url'].lower()
            
            include_match = any(keyword.lower() in tab_title or keyword.lower() in tab_url for keyword in include_keywords)
            # 除外キーワードリストが空ではない場合のみチェックする
            exclude_match = any(keyword.lower() in tab_title or keyword.lower() in tab_url for keyword in exclude_keywords) if exclude_keywords else False
              
            if exclude_keywords:
              print(f"除外文字列: {exclude_keywords}")
              if include_match and not exclude_match:
                new_window_selected['tabs'].append(tab)
              else:
                new_window_other['tabs'].append(tab)
            else:
              if include_match:
                new_window_selected['tabs'].append(tab)
              else:
                new_window_other['tabs'].append(tab)
              
        if new_window_selected['tabs']:
            selected_windows.append(new_window_selected)
        if new_window_other['tabs']:
            other_windows.append(new_window_other)
    
    return selected_windows, other_windows

def get_keywords_input(prompt):
    keywords_string = input(prompt)
    keywords = [keyword.strip() for keyword in keywords_string.split(',')]
    return keywords

def main():
    if len(sys.argv) != 3:
        print("Usage: python divide_tabs_keyword.py <input.json> <output.json>")
        sys.exit(1)

    filename = sys.argv[1]  # JSONファイルのパスを指定
    output_selected = sys.argv[2] # 出力ファイル名

    data = load_json_file(filename)
    
    # ユーザーからのキーワード入力を受け取る
    user_input = input("Include keywords (comma separated): ")
    include_keywords = [keyword.strip() for keyword in user_input.split(',') if keyword.strip()]

    user_input = input("Exclude keywords (comma separated): ")
    exclude_keywords = [keyword.strip() for keyword in user_input.split(',') if keyword.strip()]
    
    selected_windows, other_windows = filter_tabs(data, include_keywords, exclude_keywords)
    
    save_windows_data(selected_windows, output_selected)
    save_windows_data(other_windows, 'others_search.json')

if __name__ == "__main__":
    main()
