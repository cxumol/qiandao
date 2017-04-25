# coding: utf-8

import requests
import os

appid1 = os.getenv('appid1')
appid2 = os.getenv('appid2')
token = os.getenv('token')


def daocloud_restart():
    headers = {'Authorization': token}
    session = requests.Session()
    session.headers.update(headers)
    
    resp = session.post('https://openapi.daocloud.io/v1/apps/'+ appid1 +'/actions/restart', {})
    resp = session.post('https://openapi.daocloud.io/v1/apps/'+ appid2 +'/actions/restart', {})
    
if __name__ == '__main__':
    daocloud_restart()
