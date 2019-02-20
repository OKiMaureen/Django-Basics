FROM python:3

WORKDIR /app

RUN pip install django djangorestframework

COPY . .

EXPOSE 8000

ENTRYPOINT [ "/bin/bash", "start_app.sh" ]




