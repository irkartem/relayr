FROM python 

MAINTAINER Artem Artemev

ADD ./run.py /root/run.py
RUN pip install pymysql requests

EXPOSE 8080

CMD python /root/run.py
