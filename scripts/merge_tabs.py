import json
import sys

# JSONファイルを読み込む
def load_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data.get('windows', [])

# ウィンドウデータを統合して新しいJSONファイルとして保存
def merge_and_save_windows(filename1, filename2, output_filename):
    windows1 = load_json_file(filename1)
    windows2 = load_json_file(filename2)
    merged_windows = windows1 + windows2  # 二つのリストを結合
    merged_data = {'windows': merged_windows}
    
    with open(output_filename, 'w', encoding='utf-8') as file:
        json.dump(merged_data, file, indent=4)
    print(f"Merged data saved to {output_filename}")

# メイン関数
def main():
    if len(sys.argv) != 4:
        print("Usage: python merge_tabs.py <input.json> <input2.json> <merged.json>")
        sys.exit(1)

    filename1 = sys.argv[1]  # 最初のJSONファイルのパス
    filename2 = sys.argv[2]  # 二番目のJSONファイルのパス
    output_filename = sys.argv[3]  # 統合後のファイル名
    merge_and_save_windows(filename1, filename2, output_filename)

if __name__ == "__main__":
    main()
