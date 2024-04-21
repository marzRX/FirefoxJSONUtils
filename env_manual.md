# 環境設定ガイド

本スクリプトは、LZ4を使用します。以下にAnacondaを使用して仮想環境を設定する例を記します。

## 仮想環境の作成とアクティベーション

Anacondaを使用してPython 3.8の環境を作成します。

```bash
conda create -n py38ff python=3.8 -y
conda activate py38ff
```

## モジュールのインストール

必要なパッケージをインストールします。
```bash
pip install --upgrade pip
pip install setuptools --upgrade
pip install lz4
```

これで、必要な環境が整いました。スクリプトの実行にはこの環境が必要です。
