FROM python:3.11.4-alpine3.18

WORKDIR /app

COPY . .

RUN pip install -e .

ENTRYPOINT [ "gpt-engineer", "/project" ]
