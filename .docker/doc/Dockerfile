# build version
ARG ALPINE_VERSION

FROM alpine:${ALPINE_VERSION}

RUN mkdir -p /etc/Sphinx/build

RUN apk add --no-cache python3 make git

RUN pip3 install git+https://github.com/sphinx-doc/sphinx && \
    pip3 install sphinx-autobuild

CMD sphinx-autobuild -b html --host 0.0.0.0 --port 80 /etc/Sphinx/source /etc/Sphinx/build