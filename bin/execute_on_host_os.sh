#!/bin/bash

EXEC_DIR=$(dirname $0)
cd ${EXEC_DIR}/..

if [ "$EXECUTE_MODE" = "back" ]; then
    echo "execute background"
    docker-compose run -d execute $*
elif [ "$EXECUTE_MODE" = "rm" ]; then
    echo "execute and delete"
    docker-compose run --rm execute $*
elif [ "$EXECUTE_MODE" = "back-rm" ]; then
    echo "execute and delete"
    docker-compose run --rm -d execute $*
else
    echo "execute"
    docker-compose run execute $*
fi

