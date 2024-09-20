FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080
RUN python app.py
# CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
# CMD [ "python3", "-m", "flask", "run"]

