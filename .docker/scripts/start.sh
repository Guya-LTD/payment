#!/bin/bash

ENV=$1

if [ ${ENV} == 'dev' ]; then
    python manager.py run
elif [ ${ENV} == 'test' ]; then
    python manager.py test
fi