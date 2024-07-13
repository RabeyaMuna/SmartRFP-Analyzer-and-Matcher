# Use the Alpine-based Node.js image with tag matching your version for building frontend
FROM node:22-alpine as builder

# Set the working directory in the container
WORKDIR /app

# Copy the .env file to the working directory if you are running docker locally
# COPY .env .env
# Copy package.json and package-lock.json to the working directory
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Set environment variables for delpoyment
ENV REACT_APP_BACKEND_URL=${REACT_APP_BACKEND_URL}

EXPOSE 3000

CMD ["npm", "start"]


# Build the app
# RUN npm run build

# Use a smaller image for serving the static files with nginx
# FROM nginx:alpine

# # Remove default nginx configuration file
# # RUN rm /etc/nginx/conf.d/default.conf

# # Copy the built app from the builder stage to the nginx image
# COPY --from=builder /app/build /usr/share/nginx/html

# # Copy custom nginx configuration
# # COPY nginx.conf /etc/nginx/nginx.conf

# # Expose port 80 to the outside world
# EXPOSE 80

# # Command to run nginx in the foreground
# CMD ["nginx", "-g", "daemon off;"]