Some notes on how to build the Django app for Docker.

# Build the image
sudo docker image build -t coviz:1.0 .

# Run the image
sudo docker container run --publish 127.0.0.1:8080:8080 --detach --name coviz coviz:1.0
