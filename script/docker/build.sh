#!/bin/bash

EXEC_DIR=$(dirname $0)
cd ${EXEC_DIR}/../../

docker-compose build on-docker-image

