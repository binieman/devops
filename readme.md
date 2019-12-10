Requirements:

1. Python 
2. Vagrant
3. Virtual Box

This is a demo that will fire up 3 vagranted virtual machines and run a node js servers on Docker Containers.

The IPs of the VMS:
VM1 = 192.168.33.101   port  map=  3001 
VM1 = 192.168.33.102   port  map=  3001 
VM1 = 192.168.33.103   port  map=  3001

The server will return respond with "Hello World" for now in the following IPs:

VM1 = http://localhost:8081/ or 192.168.33.101:3001
VM2 = http://localhost:8082/ or 192.168.33.102:3001
VM3 = http://localhost:8083/ or 192.168.33.103:3001

To Run straight from shell:

$>vagrant up

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
$>python automate.py or automateControl.py

