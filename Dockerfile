# syntax=docker/dockerfile:1
FROM python:3-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "mysite.wsgi"]
EXPOSE 8000
