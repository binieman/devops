"""
This is the test file

"""

from os import system
import libtmux
from subprocess import PIPE, run,Popen
import argparse 
import requests
import json


parser = argparse.ArgumentParser()

parser.add_argument('ip', help="input the data in format ip", nargs='*')

args = parser.parse_args()

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}



#print(json.dumps(ip))

def output(command):
    result = Popen(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    output = ''
    while True:
        inchar = result.stdout.read(1)
        output+=inchar
        if inchar: #neither empty string nor None
            print(str(inchar), end='') #or end=None to flush immediately
        else:
            print('') #flush for implicit line-buffering
            break
    return output

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}


result = output('vagrant status')

if 'not created' in result:
    number = result.count('not created')
    print("not created machines found:")
    print(number)
    if number != 0:
        print('here')
        tempResult = output('vagrant up')
        if 'Vagrant locks each machine' in tempResult:
            print("Make sure vagrant is not already running this task")


if 'running' in result:
    number = result.count('running')
    print("running machines found::")
    print(number)

ip_list = args.ip
print("--------------------------------------------------------")
print("RUNNING TESTS.........")
print("--------------------------------------------------------")
for i in range(len(ip_list)):
    new_ip_list = ip_list.copy()
    host = new_ip_list.pop(i)
    ip = {"targets": new_ip_list}
    ip = json.dumps(ip)

    try:
        response = requests.post('http://{}/ping'.format(host),headers= headers, data = ip)
        #print(response.text)
        decoded = json.loads(response.text)
        #print(type(decoded))
        values = decoded["Success"]
        for value in values:
            IP = value.split(' ')[0].strip('<')
            print("{}->{} OK".format(host,IP))
        values = decoded["fail"]
        for value in values:
            IP = value.split(' ')[0].strip('<')
            print("{}->{} FAIL".format(host,IP))
    except requests.exceptions.RequestException as e:
        print(host + "  UNABLE TO CONNECT")



#curl -d '{"targets":["localhost","192.168.33.101"]}' -H "Content-Type: application/json" -X POST http://host/ping
#http://192.168.33.102/