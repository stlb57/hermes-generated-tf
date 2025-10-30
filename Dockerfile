FROM jenkins/jenkins:lts-jdk11
USER root
RUN apt-get update && apt-get install -y \
    python3 \
    python3-jinja2 \
    python3-git \
    git
RUN apt-get install -y wget unzip
RUN wget https://releases.hashicorp.com/terraform/1.5.7/terraform_1.5.7_linux_amd64.zip
RUN unzip terraform_1.5.7_linux_amd64.zip && mv terraform /usr/bin/
USER jenkins
