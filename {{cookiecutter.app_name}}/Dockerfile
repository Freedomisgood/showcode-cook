FROM python:{{ cookiecutter.python_version }}-slim

#RUN apt-get update && \
#    apt-get install -y --no-install-recommends \
#    cron && \
#    rm -rf /var/lib/apt/lists/* && \
#    apt-get clean

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN chmod +x ./docker-entrypoint.sh

ENV LC_ALL C.UTF-8
ENTRYPOINT ["./docker-entrypoint.sh"]
