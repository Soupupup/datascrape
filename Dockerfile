FROM python:alpine

RUN mkdir /code

COPY pyscrape.py /code

CMD ["python","/code/pyscrape.py"]