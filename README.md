# NGINX-Reverse-Proxy

## Reverse Proxy
```markdown
#  Concept:
  This is a method to host a Backend server where an Application is running, this is NOT for hosting a Static content.
  Reverse proxy server sits in front of a backend server and redirect the traffic to the backend server and hide this
  backend server from external exposure.
```

## The Architecture
1. One Nginx server and one Backend server where the application is running on some port(eg. 3000)
2. Client will hit Public IP of Nginx server, this Nginx server will work as reverse proxy server, when it receives the request it will redirect the traffic to Backend Server's particular port.
3. Allow all traffic in your both server as it is for testing purpose, otherwise for secure communication allow `http` on port `80` and `SSH` on port `22` in `Nginx` server and `http` on some port like `3000` in `Application` server.

## Launch Flask Application on `Application` server
1. Update the packages
```bash
sudo apt-get update
```
2. Install Python Pip
```bash
sudo apt install python3 python3-pip -y
```
3. Install Flask
```bash
pip install flask
```
4. Create a Directory and write application code inside the Directory
```bash
mkdir ~/my-flask-app
cd ~/my-flask-app
nano app.py
```
5. Install `gunicorn` to run the application in background
```bash
pip install gunicorn
//or
sudo apt install gunicorn
```
6. Run the Application in Background
```bash
nohup gunicorn --bind 0.0.0.0:<port> app:app >dev/null 2>&1 &
```

## Set up Reverse Proxy on NGINX server
1. Update the packages
```bash
sudo apt-get update
```
2. Install NGINX
```bash
sudo apt install nginx
nginx -v
```
3. Write the Config file
```bash
sudo nano /etc/nginx/sites-available/App
```
4. Link config file from `sites-enabled`
```bash
sudo ln -s /etc/nginx/sites-available/App /etc/nginx/sites-enabled/
```
5. Remove `default` from `sites-enabled`
```bash
sudo rm /etc/nginx/sites-enabled/default
```
6. Check Syntax
```bash
sudo nginx -t
```
7. Restart NGINX service
```bash
sudo systemctl restart nginx.service
```

## Browse the Public IP of NGINX server to get access of the Application
`http://<Public_IP_of_NGINX_server>`

![image alt](https://github.com/souravhajra123/NGINX-Reverse-Proxy/blob/4abf8fca70dc69f2fb82cdc3886104da9ff39e55/P1.png)

## Stop the Application
```bash
ps aux | grep gunicorn
kill <PID>
//or
pkill gunicorn # To terminate all gunicorn processes
```




