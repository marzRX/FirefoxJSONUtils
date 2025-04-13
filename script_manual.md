# JSONLZ4 ⇔ JSON デコード/エンコード

## デコード
**decode_jsonlz4.py**  
JSONLZ4 から JSON へのデコード  
**Usage:** `python decode_jsonlz4.py <input.jsonlz4> <output.json>`

本スクリプトを使用するにはデコードして、json ファイルにする必要があります。

## エンコード
**encode_jsonlz4.py**  
JSON から JSONLZ4へエンコード  
**Usage:** `python encode_jsonlz4.py <input.json> <output.jsonlz4>`

本スクリプトで操作した json をFirefoxで使うにはエンコード処理が必要です。

# JSON ファイルの確認
## タブ表示
**list_tabs.py**  
**Usage:** `python list_tabs.py <input.json>`

すべてのウィンドウのすべてのタブを表示します。

## アクティブタブ表示
**list_active_tabs.py**  
**Usage:** `python list_active_tabs.py <input.json>`

すべてのウィンドウのアクティブタブのみを表示します。

# JSON ファイルの分割とマージ
## ウィンドウごとの分割
**divide_tabs_window.py**  
ウィンドウを選んで分割（`selected_window.json` と `others.json` に分割）  
**Usage:** `python divide_tabs_window.py <input.json>`

対話画面で分割するウィンドウを指定します。

## キーワードによる分割
**divide_tabs_keyword.py**  
キーワードを含むタブを分割  
**Usage:** `python divide_tabs_keyword.py <input.json> <output.json>`  
**例:**  
`python divide_tabs_keyword.py sessionstore.json youtube.json`  

対話画面で include: と exclude: を指定します。例えば include に YouTube を指定すると、YouTube で検索した結果が `youtube.json` に保存され、その他のタブが `others_search.json` に保存されます。

## タブのマージ
**merge_tabs.py**  
**Usage:** `python merge_tabs.py <input.json> <input2.json> <merged.json>`

## 注意
分割とマージのスクリプトは、JSONLZ4ではなくJSONを対象としています。

# おまけユーティリティー
## タブの履歴をスリム化
**trim_history.py**  
タブごとの履歴数を制限します。  
**Usage:** `python trim_history.py <input.json> <output> [--max N] [--format json|jsonlz4]`  
**例**  
`python trim_history.py sessionstore.json sessionstore_trimmed.jsonlz4 --max 5`

一つのタブで履歴が多すぎる場合に、それらを指定した件数だけ残し、残りを削除します。
--max 0 を指定すると履歴は全て削除され、現在表示中のページのみが残ります。  
出力ファイル `<output>` の拡張子によって出力形式が決まります。  
.json → JSON形式（人が読める）  
.jsonlz4 → Firefox用の圧縮形式  


### trim_history.py のオプション一覧

| オプション | 説明 |
|---|---|
| `--max N` | 各タブごとに残す履歴の数（現在のページを除く）を指定します。<br>0 を指定すると履歴無し（現在ページのみ）、1 で現在ページ + 1 履歴、2 で現在ページ + 2 履歴となります。負の値は 0 として扱われます。 |
| `--format` | 出力形式の指定。`json` は人間が読みやすい JSON 形式、`jsonlz4` は Firefox 用の圧縮形式。省略可能です。省略した場合は `<output>` の拡張子から自動判定されます。 |

---

# 作業手順の見本
## タブの切り離し
1. `python decode_jsonlz4.py sessionstore.jsonlz4 sessionstore.json`
2. `python divide_tabs_window.py sessionstore.json`
3. `python encode_jsonlz4.py selected_window.json selected_window.jsonlz4`
4. `python encode_jsonlz4.py others.json sessionstore.jsonlz4`

## 分割したタブを現在のsessionstore.jsonlz4にマージ
1. `python decode_jsonlz4.py sessionstore.jsonlz4 sessionstore_org.json`
2. `python decode_jsonlz4.py selected_window.jsonlz4 selected_window.json`
3. `python merge_tabs.py sessionstore_org.json selected_window.json sessionstore.json`
4. `python encode_jsonlz4.py sessionstore.json sessionstore.jsonlz4`
