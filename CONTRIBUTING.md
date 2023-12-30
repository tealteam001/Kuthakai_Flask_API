# CONTRIBUTING

## How to run the Dockerfile locally


```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run"

venv cmds:
to create: 
    python3.12 -m venv .venv
to activate: 
    Source .venv/bin/activate



docker cmnds:
to build the image:
    docker build -t docker-image-tag .      (. where dockre find the code files)
binding host machine port to dockers 5000:
    docker run -d -p 127.0.0.1:3000:5000 docker-image-tag 
To run container where host folder dynced with container folder: 
    docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api
    docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run --host 0.0.0.0s"
```
