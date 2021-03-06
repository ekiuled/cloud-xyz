FROM python:3.9

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

ENTRYPOINT ["python", "-m", "cloud"]
