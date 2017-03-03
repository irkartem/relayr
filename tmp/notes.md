 ansible-playbook -i "localhost," -c local all.yml 

 curl http://172.17.0.3:8500/v1/health/service/consul?pretty

echo '{"service": {"name": "mysql", "tags": ["mysql"], "port": 3306, "ip":"'`/sbin/ip route|awk '/src/ { print  $NF}'`'"}}' | tee /etc/consul.d/mysql.json

curl -X PUT -d '{"Node": "mysql", "Address": "172.17.0.1", "Service": {"Service": "mysql", "Port": 3306, "Address": "172.17.0.1"}}' http://$CONSUL_PORT_8500_TCP_ADDR:8500/v1/catalog/register
curl -X PUT -d $MYSQL_ROOT_PASSWORD http://$CONSUL_PORT_8500_TCP_ADDR:8500/v1/kv/mysql_root_password
curl http://$CONSUL_PORT_8500_TCP_ADDR:8500/v1/health/service/mysql


/sbin/ip route|awk '/default/ { print  $3}'


/usr/bin/curl -X PUT -d '{"Node": "mysql", "Address": "'`/sbin/ip route|/usr/bin/awk '/src/ { print  $NF}'`'", "Service": {"Service": "mysql", "Port": 3306, "Address": "'`/sbin/ip route|/usr/bin/awk '/src/ { print  $NF}'`'"}}' http://$CONSUL_PORT_8500_TCP_ADDR:8500/v1/catalog/register && /usr/bin/curl -X PUT -d $MYSQL_ROOT_PASSWORD http://$CONSUL_PORT_8500_TCP_ADDR:8500/v1/kv/mysql_root_password
