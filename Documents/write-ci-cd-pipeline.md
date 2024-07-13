# Using the ci cd pipline deploy the entire project in azure VM and dockarize and run application.
1. Create Azure VM using Virtual Machine and setup with docker and ngnix
2. git clone "project url"
3. set .env with credentials inside the application in Azure VM
4. Now write cicd create the path .github->workflows->pipline-name.yml

  - Write Name of the workflow/ descrpting
  - write the branch name so that when the work is push in the barnch it should run the pipline and deploy project in the Azure VM
  - Start writing jobs adding each steps for the deployment and run the project.
  - the write the steps like that:

  ```
  steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      # Echo each secret to verify it's properly set
      - name: Check secrets
        run: |
          echo "AZURE_DATABASE_CONNECTOR=${{ secrets.AZURE_DATABASE_CONNECTOR }}"
          echo "AZ_VM_HOST=${{ secrets.AZURE_VM_HOST }}"
          echo "AZ_VM_USERNAME=${{ secrets.AZURE_VM_USERNAME }}"
          echo "AZ_VM_PASSWORD=${{ secrets.AZURE_VM_PASSWORD }}"
          echo "REACT_APP_BACKEND_URL=${{ secrets.REACT_APP_BACKEND_URL }}"
      - name: Log into Azure Container Registry
        run: |
          echo ${{ secrets.ACR_PASSWORD }} | docker login ${{ secrets.ACR_LOGIN_SERVER }} -u ${{ secrets.ACR_USERNAME }} --password-stdin
      - name: Build backend Docker image and push to Azure Container Registry
        run: |
            docker build \
              -t pem-backend-image:latest \
              --build-arg AZURE_DATABASE_CONNECTOR="${{ secrets.AZURE_DATABASE_CONNECTOR }}" \
              ./backend
  
            docker tag pem-backend-image:latest "${{ secrets.ACR_LOGIN_SERVER }}/pem-backend-image:latest"
            docker push "${{ secrets.ACR_LOGIN_SERVER }}/pem-backend-image:latest"

      - name: SSH into Azure VM and perform Docker operations
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.AZURE_VM_HOST }}
          username: ${{ secrets.AZURE_VM_USERNAME }}
          password: ${{ secrets.AZURE_VM_PASSWORD }}
          script: |

            # Stop all running Docker containers

            docker stop $(docker ps -aq)
            # Check if there are any images available or not
            if docker images -q | grep . >/dev/null; then
              # Remove all Docker images
              docker rmi -f $(docker images -q)
            fi
            
            git pull

            docker build -t pem-backend-image . ./backend
            docker build -t pem-frontend-image . ./frontend

            # Run backend container mapping port 8000:8000
            docker run -d -p 8000:8000 pem-backend-image:latest
            
            # Run frontend container mapping port 3000:3000
            # docker run -d -p 3000:3000 pem-frontend-image:latest
  ```
