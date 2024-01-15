ARG VERSION
FROM ubuntu:${VERSION}
ARG VERSION

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true

# Setup bash as the interpreter.
RUN unlink /bin/sh && link /bin/bash /bin/sh

# Configure apt for versions that reached EOL.
RUN if false \
    || [[ ${VERSION} == "19.10" ]] \
    || [[ ${VERSION} == "21.10" ]] \
    ; then \
    sed 's/http:\/\/archive.ubuntu.com\/ubuntu/http:\/\/old-releases.ubuntu.com\/ubuntu/' /etc/apt/sources.list > /etc/apt/sources.list1; \
    mv /etc/apt/sources.list1 /etc/apt/sources.list; \
    sed 's/http:\/\/security.ubuntu.com\/ubuntu/http:\/\/old-releases.ubuntu.com\/ubuntu/' /etc/apt/sources.list > /etc/apt/sources.list1; \
    mv /etc/apt/sources.list1 /etc/apt/sources.list; \
    sed 's/http:\/\/archive.canonical.com\/ubuntu/http:\/\/old-releases.ubuntu.com\/ubuntu/' /etc/apt/sources.list > /etc/apt/sources.list1; \
    mv /etc/apt/sources.list1 /etc/apt/sources.list; \
    sed 's/http:\/\/ports.ubuntu.com\/ubuntu-ports/http:\/\/old-releases.ubuntu.com\/ubuntu/' /etc/apt/sources.list > /etc/apt/sources.list1; \
    mv /etc/apt/sources.list1 /etc/apt/sources.list; \
    fi

# Configure locale, this is often required.
RUN true \
    && apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install locales \
    && sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen \
    ;

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

RUN apt-get -y install \
    python3 \
    python3-venv \
    ;

RUN true \
    && python3 -m venv /tmp/venv \
    && source /tmp/venv/bin/activate \
    && chmod -R 777 /tmp/venv \
    && export PIP_CACHE_DIR=/tmp/venv/.cache \
    && python3 -m pip install pytest \
    ;
