#!/bin/bash

# export ON_DOCKER_UTILS_BIN=<path>/on-docker/utils/bin/execute_on_host_os.sh

# ###############################################################################
# setting
# ###############################################################################
export LOG_LEVEL=DEBUG
# export EXECUTE_MODE=back  # back rm back-rm
export EXECUTE_NAME=_sample
export EXECUTE_PYTHON_FILE=on_docker/sample.py

# ###############################################################################
# execute
# ###############################################################################
bash ${ON_DOCKER_UTILS_BIN} bar

