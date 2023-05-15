# wget-python

本レポジトリは'wget'と似たような機能を実装する練習プロジェクトである．
Pythonで`requests`などのhttpモジュールを使わずに機能を実装した．

## 開発環境
- Dev OS: Ubuntu(22.04.2 LTS)
- Programming language: Python(3.11.2)

# 使用方法

このプログラムは使用者から`url`入力を受け，その`url`からHTMLコンテンツをダウンロードする．

- [準備](#準備)
- [実行](#実行)

## 準備

1. Pythonのインストール  
    [開発環境](#開発環境)で述べたようにPython(3.xバージョン)のインストールが必要である．

2. 本レポジトリをクローン(orダウンロード)する  

3. 必要パッケージをダウンロードする  
    プログラム実行に必要なパッケージをダウンロードする．
    `requirements.txt`に必要なパッケージが書かれている．
    以下のコマンドでダウンロードすることができる．
```bash
$ pip install -r requirements.txt
```

## 実行

ルートディレクトリで以下のコマンドを実行することで本プログラムを実行できる．

```bash
$ python main.py <url>
```

すると，`./downlads/<domain>`ディレクトリにHTMLコンテンツをダウンロードされる．

`<url>`に<https://www.city.takatsuki.osaka.jp/index2.html>を代入し実行した結果，約１３分経過後に合計6876個のhtmlファイルがダウンロードされた．
