---
- hosts: all
  tasks:
    - shell: echo "hello world"
    -   name: Install python setup tools
        yum: name=python-setuptools
        tags: docker
    
    -   name: Install Pypi
        easy_install: name=pip
        tags: docker
    
    -   name: Install docker-py
        pip: name=docker-py
        tags: docker
    
    -   name: Install Docker
        yum: name=docker state=latest
        tags: docker
    
    -   name: Make sure Docker is running
        service: name=docker state=running
        tags: docker