#!/usr/bin/env python

import requests


def poweroff(csp_ip, login_key, service_name):
    requests.packages.urllib3.disable_warnings()
    payload = "\n{\"service\":{\"power\":\"off\"}}"
    headers = {
        'content-type': 'application/json',
        'authorization': 'Basic ' + login_key,
        'cache-control': 'no-cache'
    }
    url='https://'+csp_ip+'/api/running/services/service/'+service_name
    response = requests.patch(url, data=payload, headers=headers, verify=False)
    print ('Power off status code: ', response.status_code)
    return response


def poweron(csp_ip, login_key,service_name):
    requests.packages.urllib3.disable_warnings()

    payload = "\n{\"service\":{\"power\":\"on\"}}"
    headers = {
        'content-type': 'application/json',
        'authorization': 'Basic '+login_key,
        'cache-control': 'no-cache'
    }
    url='https://'+csp_ip+'/api/running/services/service/'+service_name
    response = requests.patch(url, data=payload, headers=headers, verify=False)
    print ('Power on status code: ',response.status_code)
    return response


def deleteservice(csp_ip, login_key,service_name):
    requests.packages.urllib3.disable_warnings()

    payload = "\n{\"service\":{\"power\":\"on\"}}"
    headers = {
        'content-type': 'application/json',
        'authorization': 'Basic '+login_key,
        'cache-control': 'no-cache'
    }
    url='https://'+csp_ip+'/api/running/services/service/'+service_name
    response = requests.delete(url, headers=headers, verify=False)
    print ('Delete Service status code: ', response.status_code)
    return response
