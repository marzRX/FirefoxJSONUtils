# 環境設定ガイド

本スクリプトは、LZ4を使用します。以下に、Anacondaとvenvを使用して仮想環境を設定する二つの方法を紹介します。

## 仮想環境の作成

### Anacondaを使用した方法

Anacondaを使用してPython 3.8の環境を作成し、アクティベートします。


```bash
conda create -n py38ff python=3.8 -y
conda activate py38ff
```

### venvを使用した方法

venvを使用して仮想環境を設定する場合、最初にvenvモジュールがインストールされていることを確認します。

```bash
sudo apt install python3-venv  # Ubuntu/Debianの場合
```

仮想環境を作成し、アクティベートします。

```bash
python3 -m venv ffvenv
source ffvenv/bin/activate
```

## モジュールのインストール

必要なパッケージをインストールします。
```bash
pip install --upgrade pip
pip install setuptools --upgrade
pip install lz4
```

これで、必要な環境が整いました。スクリプトの実行にはこの環境が必要です。
