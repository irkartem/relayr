## How it work 

 I have 3 docker containers. With random ips. Static ip usage is simple. 

 My mysql docker container starts and register service in consul via curl request (may be it's not robust way). Another ways:
- run local consul agent in DB container
- register service in my vagrant-ansible provisioning, but it's not guarante what DB will work, but we have checks hmmm.   

## My question 

- Do I need run consul agent in mysql docker.
