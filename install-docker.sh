#! /bin/bash
curl https://get.docker.com | sudo bash
sudo groupadd docker
sudo usermod -aG docker $(whoami)
newgrp docker
docker run hello-world
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
