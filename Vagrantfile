# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  
  config.vm.box = "centos/7"
  
  

  (1..3).each do |i|
    port = 8080+i         #increment port 
    ip_address = i+100    #increment ip address 
    config.vm.define "VM-#{i}" do |node|
      node.vm.network "forwarded_port", guest: 80, host: port, host_ip: "127.0.0.1"
      node.vm.network "private_network", ip: "192.168.33.#{ip_address}"
      node.vm.provision "shell", inline: <<-SHELL
        curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
        sudo yum install -y nodejs
        sudo yum install -y yum-utils device-mapper-persistent-data lvm2
        sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
        sudo yum install -y docker
        sudo systemctl start docker
        sudo chmod 777 /var/run/docker.sock
        cd /vagrant
        docker build -t binod/app .
        docker run -d -e PORT=80 -p 80:80 binod/app
        docker images
        docker ps

      SHELL

    end
  end
  
end
