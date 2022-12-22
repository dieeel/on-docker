#!/bin/bash

EXEC_DIR=$(dirname $0)
cd ${EXEC_DIR}/..

python ${EXECUTE_PYTHON_FILE} "$@"

