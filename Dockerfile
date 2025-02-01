FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
  localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

COPY requirements.txt /root/

RUN apt-get install -y vim less
RUN apt-get install -y poppler-utils
RUN apt-get install -y tesseract-ocr
# 日本語用の学習データをインストール
RUN apt-get install -y tesseract-ocr-jpn
# best版を利用した場合は以下のコメントアウトを外す
# RUN curl -L -o /usr/share/tesseract-ocr/5/tessdata/jpn.traineddata https://github.com/tesseract-ocr/tessdata_best/raw/main/jpn.traineddata
RUN apt-get install -y libtesseract-dev
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install -r /root/requirements.txt