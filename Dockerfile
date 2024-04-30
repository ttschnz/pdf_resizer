FROM python:3.11-alpine
RUN mkdir /app

WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
RUN mkdir ./temp
COPY ./convert.py  convert.py
COPY ./serve.py  serve.py
COPY ./upload.html  upload.html
WORKDIR /app
CMD ["python3", "serve.py"]