import lz4.block  # pip install lz4
import sys

def text_to_mozlz4(filepath_in, filepath_out):
    # ファイルをテキストモードで読み込み
    with open(filepath_in, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # テキストをLZ4で圧縮
    compressed = lz4.block.compress(text.encode('utf-8'))
    
    # ファイルをバイナリモードで書き込み、ヘッダーを追加
    with open(filepath_out, 'wb') as file:
        file.write(b"mozLz40\0")  # 独自の8バイトヘッダー
        file.write(compressed)

def main():
    if len(sys.argv) > 2:
        filepath_in = sys.argv[1]
        filepath_out = sys.argv[2]
        text_to_mozlz4(filepath_in, filepath_out)
    else:
        print("Usage: python encode_jsonlz4.py <input.json> <output.jsonlz4>")

if __name__ == "__main__":
    main()
