FROM python:3.10-slim

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD [ "gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000" ]