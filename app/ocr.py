from pathlib import Path
from pdf2image import convert_from_path
import pyocr
import pyocr.builders
import sys

# 使用可能なOCRツールを探す
tools = pyocr.get_available_tools()
tool = tools[0]
if len(tools) == 0:
    print("OCR tool is not found.")
    sys.exit(1)
lan = "jpn"

# ###抽出したいファイル名を指定####
f_name = "達人に学ぶDB設計徹底指南指南書"

# パスを設定
pdf_path = Path(f"./input/{f_name}.pdf")
txt_path = Path(f"./output/{f_name}.txt")

# PDFから画像ファイルに変換
print("start convert pdf to image")
# 第二引数の値で画像の解像度が変化され、文字の抽出の精度に影響が発生する
# 値が大きすぎるとプロセスが失敗する
pages = convert_from_path(str(pdf_path), 163)
print("finish convert pdf to image")

print("start getting textdata")
txt = ""
for i, page in enumerate(pages):
    txt = txt + tool.image_to_string(page, lang=lan, builder=pyocr.builders.TextBuilder(tesseract_layout=6))
print("finish getting textdata")

# テキストファイルに書き出し
print("start writing textfile")
with open(txt_path, mode="w") as f:
    f.write(txt)
print("Process completed!")
