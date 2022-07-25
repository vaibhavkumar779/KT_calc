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

* Ensure that the server is running using the systemctl start command:

sudo systemctl start mysql.service

#### error followup:

#### my mydqld was not working so shifted to docker mysql

* sudo apt-get purge mysql\* libmysql\*
* sudo apt autoremove
