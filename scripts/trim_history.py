import argparse
import json
import lz4.block
import os
import sys

def trim_history(input_file, output_file, max_history=10, output_format='jsonlz4'):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # max_history は履歴の数を示すようにする
    if max_history < 0:
        print(f"Warning: --max {max_history} is invalid. Treated as 0 (no history).")
        max_history = 0

    # 履歴数 + 現在のページで entries を残す
    entries_to_keep = max_history + 1

    for win in data.get("windows", []):
        for tab in win.get("tabs", []):
            if "entries" in tab and isinstance(tab["entries"], list):
                if max_history == 0:
                    # 履歴ゼロなら最新（現在）だけ残す
                    tab["entries"] = [tab["entries"][-1]]
                else:
                    tab["entries"] = tab["entries"][-entries_to_keep:]

    if output_format == 'json':
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    else:
        compressed = lz4.block.compress(json.dumps(data).encode("utf-8"))
        with open(output_file, "wb") as f:
            f.write(b'mozLz40\0')
            f.write(compressed)

    print(f"Trimmed history written to {output_file} as {output_format.upper()}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Trim history entries in Firefox session JSON file.'
    )
    parser.add_argument('input', help='Input JSON file (decoded from jsonlz4)')
    parser.add_argument('output', help='Output file (JSON or JSONLZ4)')
    parser.add_argument('--max', type=int, default=10,
        help='Number of history entries to keep per tab (excluding current page). '
             '0 = no history, 1 = current page + 1 history entry, etc. '
             'Negative values are treated as 0.'
    )
    parser.add_argument('--format', choices=['json', 'jsonlz4'], default=None,
        help='Output format. If omitted, determined by output filename extension.')

    args = parser.parse_args()

    # フォーマット自動判定
    output_format = args.format
    if output_format is None:
        ext = os.path.splitext(args.output)[1].lower()
        if ext == ".json":
            output_format = "json"
        elif ext == ".jsonlz4":
            output_format = "jsonlz4"
        else:
            print(f"Error: unknown output format from extension: {ext}")
            sys.exit(1)

    trim_history(args.input, args.output, args.max, output_format)
