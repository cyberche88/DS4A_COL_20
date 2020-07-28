FROM ubuntu:latest
MAINTAINER  "felix141996@gmail.com"
RUN apt-get update -y
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y software-properties-common build-essential python3.8 python-dev python3-pip git
COPY ./requirements.txt /var/www/app/
WORKDIR /var/www/app/
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/bin/bash"]
