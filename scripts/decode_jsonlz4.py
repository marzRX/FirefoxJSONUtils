import lz4.block
import sys

def mozlz4_to_json(filepath_in, filepath_out):
    with open(filepath_in, 'rb') as file_in:
        # 最初の8バイト（ヘッダー）を読み飛ばす
        file_in.read(8)
        # 圧縮されたデータを読み込む
        compressed_data = file_in.read()
        # LZ4でデコード
        decompressed_data = lz4.block.decompress(compressed_data)
    
    with open(filepath_out, 'wb') as file_out:
        file_out.write(decompressed_data)

def main():
    if len(sys.argv) > 2:
        filepath_in = sys.argv[1]
        filepath_out = sys.argv[2]
        mozlz4_to_json(filepath_in, filepath_out)
    else:
        print("Usage: python decode_jsonlz4.py <input.jsonlz4> <output.json>")

if __name__ == "__main__":
    main()
