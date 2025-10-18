### Create and initiate a virtual Environment
- Navigate to your root directory
- python3 -m venv hng_venv
- source hng_venv/Scripts/activate

### Installation
- python3 -m pip install flask
- python3 -m pip install requests

### Check installed Packages
- pip freeze

### Run Scripts locally
- cd Profile_Endpoint/
- chmod u+x app.py
- ./app.py
- Access on your browser through http://127.0.0.1:3000/me


### Deployment
#### Remove all enabled sites
sudo rm -f /etc/nginx/sites-enabled/*

#### Create only your flask-app config
sudo tee /etc/nginx/sites-available/flask-app > /dev/null << 'EOF'
server {
    listen 80 default_server;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
EOF

#### Enable your site
sudo ln -s /etc/nginx/sites-available/flask-app /etc/nginx/sites-enabled/

#### Test and restart
sudo nginx -t
sudo systemctl restart nginx
