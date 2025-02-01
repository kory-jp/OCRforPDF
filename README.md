# PDF からテキスト情報を抽出する

PDF 内の文字列(日本語、英語)を認識して文字情報をテキストファイルに抽出する

## 起動

必要なもツール

- Docker

```
git clone https://github.com/kory-jp/OCRforPDF.git
docker compose build
docker compose up -d
```

## 実行

app/input ディレクトリ以下に文字列を抽出したい PDF ファイルを配置

以下のコマンドを実行

```
python3 ./app/ocr.py
```

実行が成功した場合に app/output ディレクトリにテキストファイルが生成される
