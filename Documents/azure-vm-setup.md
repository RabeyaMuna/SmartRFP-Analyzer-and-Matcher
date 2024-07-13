# Create a Azure VM using Virtual Machine

1. Select Virtual Machine and select options

2. Create Public IP address using Virtual Network

3. Access to Azure VM using Public IP address and password
   ```
    ssh username@ip-address
    Enter your password when prompted
   ```

4. Setup Azure VM based on the application requirements.
   - Setup Docker for Azure VM
   ```
    sudo apt update
    sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"
    sudo apt update
    sudo apt-get install docker-ce
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo systemctl status docker

    sudo groupadd docker
    sudo usermod -aG docker ubuntu
    su - ubuntu
    ```

   - Setup Ngnix for Azure VM

    ```
    sudo apt-get -y update
    sudo apt-get -y install nginx
    sudo systemctl status nginx

    ```
    - If you can't access it from browser right now because we haven't added port rule. To access the server we need to add PORT to Access Rule to our VM. In order to add rule for port, we need to add port in network settings of Azure VM in Add Inbound Port Rule 
    
    ```
    Add Inbound Port Rule
    ```

    You need to all expose port in which you want to run the application

    - SSL Certificate using Certbot

       * add one last PORT 443 rule. As we know HTTPS runs on port 443 and without 443 access browser can't use https connection.

       * Install Certbot in VM

       ```
        sudo apt-get install software-properties-common
        sudo add-apt-repository ppa:certbot/certbot
        sudo apt-get update
        sudo apt-get install python-certbot-nginx
        sudo certbot --nginx
       ```
5. Install Necessary dependencies in the Azure VM if it requires to setup like local pc.

6. Pull images from Azure Conatiner regustry to Azure VM

7. Check docker images

8. Run Docker images with the export port.

9. To create a static URl, need to create DNS from AZUR which will provide certain url against the provided name.

9. Add a ngnix.config file to build static url. It can be added within the frontend folder root file and the below code needs to be added:

   ```
         server {
         listen 80;
         server_name staticdomain.com;
         return 301 https://$host$request_uri;
         location / {
            proxy_pass http://127.0.0.1:8026;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
         }
      
      }
   ```

10. To set https server with static url, we required ssl certificate and add the below code in ngnix.conf

   ```
     server {
    listen 443 ssl;
    server_name staticdomain.com;
    ssl_certificate /etc/nginx/ssl/fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/staticdomain.key;
 
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
         }
      }

   ```
