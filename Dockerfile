FROM python:3.6-slim

WORKDIR /usr/src/app/
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

RUN apt-get -y update && apt-get install -y ffmpeg
COPY ./requirements.txt /usr/src/app/
RUN pip install --upgrade pip; pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ -r /usr/src/app/requirements.txt

COPY . /usr/src/app/

EXPOSE 8080
VOLUME /usr/src/app/data

CMD ["python", "/usr/src/app/app.py"]

