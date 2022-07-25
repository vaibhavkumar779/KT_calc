# KT_calc

to use this you mysql client installed on system

# deploying on EC2
* connecting with Instance
ssh -i "ktflask.pem" ubuntu@ec2-54-237-132-117.compute-1.amazonaws.com

* service file

I have used a Service file to run this application on EC2 ubuntu 22.04 instance

'''
[Unit]
Description=Gunicorn instance for KT calci
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/KT_calc
ExecStart=/home/ubuntu/KT_calc/venv/bin/gunicorn -b 0.0.0.0:7700 app:app
Restart=always
[Install]
WantedBy=multi-user.target

'''

I encountered a problem in running my Service 


* Solution:

The fix is obscure: you will have to manually edit a system file, so be extra-careful when doing that. The file in question is /usr/lib/systemd/system/initrd-switch-root.service.

As root, open that file with your favourite editor, and scroll down to the line that says:

ExecStart=systemctl --no-block switch-root /sysroot
and change it to

ExecStart=/usr/bin/systemctl --no-block switch-root /sysroot
Then run systemctl daemon-reload, and you should be able to start your unit.

Source: https://github.com/systemd/systemd/issues/16076

# installing and using mysql on ubuntu

* Server: mysql-server

sudo apt update
sudo apt install mysql-server
sudo apt install libmysqlclient-dev

* Ensure that the server is running using the systemctl start command:

sudo systemctl start mysql.service

## follow:
https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-22-04

#### error followup:

#### my mydqld was not working so shifted to docker mysql

* sudo apt-get purge mysql\* libmysql\*
* sudo apt autoremove

##### installing docker first

* prerequisites

sudo apt install apt-transport-https ca-certificates curl software-properties-common

* key addition

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

* update for cache

sudo apt update

apt-cache policy docker-ce

docker-ce:

  Installed: (none)

  Candidate: 5:20.10.17~3-0~ubuntu-jammy

  Version table:

     5:20.10.17~3-0~ubuntu-jammy 500

        500 https://download.docker.com/linux/ubuntu jammy/stable amd64 Packages

     5:20.10.16~3-0~ubuntu-jammy 500

        500 https://download.docker.com/linux/ubuntu jammy/stable amd64 Packages

     5:20.10.15~3-0~ubuntu-jammy 500

        500 https://download.docker.com/linux/ubuntu jammy/stable amd64 Packages

     5:20.10.14~3-0~ubuntu-jammy 500

        500 https://download.docker.com/linux/ubuntu jammy/stable amd64 Packages

     5:20.10.13~3-0~ubuntu-jammy 500

        500 https://download.docker.com/linux/ubuntu jammy/stable amd64 Packages

    * install docker

    sudo apt install docker-ce

    * Check status

    sudo systemctl status docker

    * Execute docker command without sudo

    sudo usermod -aG docker ${USER}

    * complete this  group addition 

    su - ${USER}

    * check if added to group

    groups

#### Using docker for msql

* pull image

docker pull mysql:latest

* run image

docker run --name kt_db  --restart on-failure  -d    -e MYSQL_ROOT_PASSWORD=123 mysql/mysql-server:8.0

* check if running

docker ps

CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS                            PORTS                       NAMES

44b3b5e1b389   mysql/mysql-server:8.0   "/entrypoint.sh mysq…"   25 seconds ago   Up 6 seconds (health: starting)   3306/tcp, 33060-33061/tcp   kt_db

* get generated password

docker logs kt_db





