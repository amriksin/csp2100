#!/usr/bin/env python

import base64
import csp2100

csp_ip=''
username=''
password=''

key = base64.b64encode(username+':'+password)

csp2100.poweron(csp_ip,key,'Student23_CSR1')
csp2100.poweroff(csp_ip,key,'Student23_CSR1')
csp2100.deleteservice(csp_ip,key,'Student23_CSR1')


