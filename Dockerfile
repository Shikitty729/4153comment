FROM python:3.12-slim

# add dependencies for mysqlclient
RUN apt-get update && apt-get install -y  \
    pkg-config  \
    default-mysql-client  \
    default-libmysqlclient-dev \
    build-essential

COPY . /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]