# coding: utf-8

import requests
import os

# if you don't have a config.py
# You can set v2ex_username, v2ex_password yourself

appid = os.getenv('appid')
token = os.getenv('token')


def daocloud_restart():
    headers = {'Authorization': token}
    session = requests.Session()
    session.headers.update(headers)
    
    resp = session.post("https://openapi.daocloud.io/v1/apps/"+ appid +"/actions/restart", {})
    
if __name__ == '__main__':
    daocloud_restart()
