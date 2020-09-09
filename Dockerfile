FROM python:3.8.5-slim

WORKDIR /app

COPY requirements.txt *.py *.html  /app/

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

CMD [ "flask", "run","--host=0.0.0.0", "--port=5000" ]
