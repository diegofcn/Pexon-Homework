FROM python:3.10

WORKDIR /flaskapp

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]