FROM ubuntu:bionic

ENV LANG="C.UTF-8" \
    LC_ALL="C.UTF-8" \
    PYTHONIOENCODING="UTF-8"

RUN set -x \
 && apt-get update \
 && apt-get install --yes --no-install-recommends \
        software-properties-common \
 && add-apt-repository ppa:deadsnakes/ppa --yes \
 && apt-get update \
 && apt-get install --yes \
        python2.3 \
        python2.4 \
        python2.5 \
        python2.6 \
        python2.7 \
        python3.1 \
        python3.2 \
        python3.3 \
        python3.4 \
        python3.5 \
        python3.6 \
        python3.7 \
        python3.8
