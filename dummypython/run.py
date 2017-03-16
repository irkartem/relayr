#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================
import sys
import pymysql
import requests
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

def geturlvalue(s):
    r = requests.get(s)
    if r.status_code != 200:
        return False
    return r.text.strip()
 

 
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  def do_GET(self):
        self.send_response(200)
 
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello world!"

        mysqlPas = geturlvalue("http://{}:8500/v1/kv/mysql_root_password?raw".format(os.environ['CONSUL_PORT_8500_TCP_ADDR']))
        r = requests.get('http://{0}:8500/v1/health/service/mysql'.format(os.environ['CONSUL_PORT_8500_TCP_ADDR']))
        j=r.json()
        for el in j:
           service = el['Service']['ID']
           ip = el['Service']['Address']
           port = el['Service']['Port']
        #message = message + "\n<br>\nip ={} port={} ps={}".format(ip, port, mysqlPas)
        conn = pymysql.connect(host=ip, port=port, user='root', passwd=mysqlPas, db='mysql')
        cur = conn.cursor()
        cur.execute("SELECT Host,User FROM user")
        message = message + "<br>\n{}".format(cur.description)
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run():
  print('starting server...')
 
  server_address = ('0.0.0.0', 8080)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()


