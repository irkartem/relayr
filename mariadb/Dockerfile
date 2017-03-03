FROM mariadb

MAINTAINER Artem Artemev

RUN apt-get update && apt-get install -y \
    curl \
 && rm -rf /var/lib/apt/lists/*

ADD ./register.sh /opt/register.sh
RUN chmod +x /opt/register.sh
COPY docker-entrypoint.sh /usr/local/bin/


