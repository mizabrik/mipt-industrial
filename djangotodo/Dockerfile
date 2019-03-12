FROM python:3.7-alpine as base

FROM base as builder

COPY requirements.txt /requirements.txt
RUN apk add --no-cache postgresql-dev musl-dev gcc
RUN pip install --prefix=/install -r /requirements.txt

FROM base

RUN apk --no-cache add libpq
COPY --from=builder /install /usr/local
COPY . /app
WORKDIR /app

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
