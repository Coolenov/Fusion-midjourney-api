FROM python:alpine


WORKDIR app/

COPY . .

RUN pip install requests flask beautifulsoup4 pprint3x

EXPOSE 9020

CMD ["python","api.py"]
