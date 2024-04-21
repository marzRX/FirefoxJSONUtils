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
