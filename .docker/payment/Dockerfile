# build version
ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION}

# scripts
COPY ./scripts/ /tmp/scripts/
RUN chmod +x -R /tmp/scripts/

# env
ARG ENV

# permant scripts
RUN mkdir -p /bin/scripts/ \
 && cp /tmp/scripts/install-py-packages.sh /bin/scripts/install-py-packages.sh \
 && cp /tmp/scripts/start.sh /bin/scripts/start.sh \
 && chmod +x -R /bin/scripts \
;

# workdir
ARG WORK_DIR
WORKDIR ${WORK_DIR}

# install packages
ENTRYPOINT /bin/scripts/install-py-packages.sh ${ENV} && /bin/scripts/start.sh ${ENV}