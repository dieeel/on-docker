#!/bin/bash

docker ps -a --format "table {{.Names}}\t{{.Status}}" | grep on-docker_execute_run

