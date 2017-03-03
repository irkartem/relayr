
## My question 

- Do I need use static ip’s? 
- Do I need run consul agent inside DB container, for register service in good time? 
- if Ansible will register new service with checks script. Does it allow? 


## How it work 

 It will be easy with valid domains for consul. 

 I have 3 docker containers. With random ips. 

 My mysql docker container starts and register service in consul via curl request (may be it's not robust way)

 Dummy apps uses env variable connect to http consul and get data:

- http://$CONSUL_PORT_8500_TCP_ADDR:8500/v1/kv/mysql_root_password?raw
- http://$CONSUL_PORT_8500_TCP_ADDR:8500/v1/health/service/mysql

## Result

It's work for me and print information from DB:

# curl localhost:8080                                                                                                                                                                                                                                                                                                                               
Hello world!<br>
(('Host', 254, None, 60, 60, 0, False), ('User', 254, None, 80, 80, 0, False))


But I haven't time for test and improve.

##todo
- Add exeption for dummyapp 
- Develop service resitration concept
- Make domains for consul :) 

