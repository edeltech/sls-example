FROM amd64/python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APPDIR /

RUN pip install --upgrade pip
RUN pip install --no-cache-dir awscli

RUN mkdir -p $APPDIR
WORKDIR $APPDIR

ADD requirements.txt $APPDIR/
RUN pip install --no-cache-dir -r requirements.txt

ADD . $APPDIR