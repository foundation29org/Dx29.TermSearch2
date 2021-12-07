FROM python:3.7

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /app

WORKDIR /app

RUN python setup.py

EXPOSE 8080

ENTRYPOINT ["python", "app.py"]
