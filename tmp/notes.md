 ansible-playbook -i "localhost," -c local all.yml 

 curl http://172.17.0.3:8500/v1/health/service/consul?pretty

echo '{"service": {"name": "mysql", "tags": ["mysql"], "port": 3306}}' | tee /etc/consul.d/mysql.json
