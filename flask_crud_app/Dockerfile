FROM python:3.8-slim-buster

WORKDIR /app

COPY . .
COPY requirements.txt .

RUN pip3 install -r requirements.txt

# EXPOSE 5000
# CMD ["python","app.py"] 
# CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD exec gunicorn app:app  --bind 0.0.0.0:5000 --timeout 0 --workers 3 --threads 8

# CMD [ "python3", "-m", "flask", "run"]

