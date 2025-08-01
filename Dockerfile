FROM python:3.9.2
EXPOSE 80

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3"]

CMD ["app.py"]

