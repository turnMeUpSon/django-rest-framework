# The image you are going to inherit your Dockerfile from
FROM alpine:3.17
# Necessary, so Docker doesn't buffer the output and that you can see the output 
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1
# Make a directory in your Docker image, which you can use to store your source code
RUN mkdir /drf
# Set the /django_recipe_api directory as the working directory
WORKDIR /drf
# Copies from your local machine's current directory to the django_recipe_api folder 
# in the Docker image
COPY . .
RUN apk add py3-pip
# Copy the requirements.txt file adjacent to the Dockerfile 
# to your Docker image
COPY ./requirements.txt /requirements.txt
# Install the requirements.txt file in Docker image
RUN pip install -r /requirements.txt
RUN apk add --update postgresql-client jpeg-dev
RUN apk add --update --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
# Create a user that can run your container
RUN adduser -D admin
USER admin