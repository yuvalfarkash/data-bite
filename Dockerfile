FROM python:3.10-alpine

WORKDIR /app

# התקנת Flask בתוך האימג' הדוקר
RUN pip install flask

COPY . .

CMD ["python", "app.py"]