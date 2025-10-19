# FirefoxJSONUtils

## 概要
Firefox のセッションファイル（sessionstore.jsonlz4）を操作するためのスクリプト群です。jsonlz4 のデコードとエンコード、json ファイルのリスト表示、分割、マージが含まれます。

## 環境設定
本スクリプトは、`lz4` パッケージに依存しています。詳細な環境構築方法は [env_manual.md](env_manual.md) に記載しています。Anaconda を使用した Python 環境の設定方法を紹介しています。

## 使い方
以下に具体的な使用例を示します。

### タブの分割（ウィンドウレベル）
```bash
python divide_tabs_window.py sessionstore.json
```
実行すると、各ウィンドウのアクティブタブが表示され、分離するウィンドウを選択できます。

### タブの分割（検索ワード）
```bash
python divide_tabs_keyword.py sessionstore.json youtube.json
```

キーワードや除外キーワードを指定する対話画面が表示されます。

-    Include: youtube [enter]
-    Exclude: [enter]

出力:

-    検索結果: youtube.json
-    それ以外: others_search.json

### スクリプトマニュアル
より詳細なスクリプトの説明については、[script_manual.md](script_manual.md)を参照してください。

## Firefox セッションファイルの場所
- Linux Mint: ~/.mozilla/firefox 下に存在します。
- カレントディレクトリにセッションファイルをコピーする方法:

```bash
find ~/.mozilla/ -name sessionstore.jsonlz4 | xargs -I% cp % .
```

Firefoxで複数のプロファイルを使用している場合の対応:
```bash
find ~/.mozilla/ -path "*default-release/sessionstore.jsonlz4" | xargs -I% cp % .
```


## ライセンス
このプロジェクトは [MITライセンス](LICENSE.txt) の下で公開されています。
