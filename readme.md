Requirements:

1. Python 
2. Vagrant
3. Virtual Box
This is a demo that will fire up 3 vagranted virtual machines and run a node js servers on Docker Containers. The idea is to have a terminal multiplexer which is automated. 

The IPs of the VMS:
VM1 = 192.168.33.101   port  map=  80
VM1 = 192.168.33.102   port  map=  80
VM1 = 192.168.33.103   port  map=  80

The server will return respond with "Hello World" for now in the following IPs:

VM1 = http://localhost:8081/ or 192.168.33.101
VM2 = http://localhost:8082/ or 192.168.33.102
VM3 = http://localhost:8083/ or 192.168.33.103

API endpoints

GET IP/pong-> gets "PONG request"

query parameters: none
body: none
behavior: Waits 10 seconds and then responds with a string "PONG"
response: "PONG"


POST IP/ping 
query parameters: none
body: { "targets": [<ip address>, ...] }
behavior: Receives a list of ip addresses in the message body. For EACH ip address <addr> in parallel, should send an HTTP GET to http://<addr>/pong
response: { "success": [<addr pong was successful>, ...], "fail": [<addr pong failed>, ...] }

Ssh into the VMS for eg. vagrant ssh VM1
$> vagrant ssh {VM1 or VM2 or VM3}

Find Docker container id in the ssh console
$> docker ps

Attach docker container to see the ping output
$>docker attach {container id}


That should give the ping from server to other ips


__________________________________________________________________
Running the python code:


requirement:

1. pip
2. pipenv

on the directory where requirements.txt:

$>pipenv shell

That should activate the virtual environment for python.
After that 
$>pip install -r requirements.txt
$>python run-test.py <IP1......IPn>

The code will fire vagranted machines if they are not already running. to destroy the machines please use vagrant destroy



