#!/bin/bash

/usr/bin/curl -X PUT -d '{"Node": "mysql", "Address": "'`/sbin/ip route|/usr/bin/awk '/src/ { print  $NF}'`'", "Service": {"Service": "mysql", "Port": 3306, "Address": "'`/sbin/ip route|/usr/bin/awk '/src/ { print  $NF}'`'"}}' http://$CONSUL_PORT_8500_TCP_ADDR:8500/v1/catalog/register && /usr/bin/curl -X PUT -d $MYSQL_ROOT_PASSWORD http://$CONSUL_PORT_8500_TCP_ADDR:8500/v1/kv/mysql_root_password
mysqld -u mysql
