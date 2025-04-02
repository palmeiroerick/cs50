FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install --no-install-recommends --yes \
    build-essential \
    openssh-client \
    fish \
    git \
    clang \
    gdb \
    valgrind \
    python3 \
    python3-pip \
    sqlite3 \
    unzip \
    zip \
    sudo \
    curl \
    wget \
    less \
    man \
    man-db \
    nano \
    bash-completion \
    coreutils \
    tzdata && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-c"]
CMD ["fish"]

RUN userdel --force --remove ubuntu && \
    rm --force --recursive /home/ubuntu

RUN useradd --create-home --shell /usr/bin/fish ubuntu && \
    usermod -aG sudo ubuntu && \
    chown -R ubuntu:ubuntu /home/ubuntu && \
    echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER ubuntu
WORKDIR /home/ubuntu
ENV WORKDIR=/home/ubuntu
