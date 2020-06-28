#!/bin/bash

ENV=$1

if [ ${ENV} == 'dev' ]; then
    pip install -r requirements/dev.txt
elif [ ${ENV} == 'prod' ]; then
    pip install -r requirements/prod.txt
fi
