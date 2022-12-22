#!/bin/bash

docker ps -a --format "table {{.ID}}\t{{.Names}}\t{{.Status}}" | grep on-docker_execute_run | grep Exited | awk '{print "docker rm " $1}' | bash
# docker ps -a --format "table {{.ID}}\t{{.Names}}\t{{.Status}}" | grep on-docker_execute_run | grep Created | awk '{print "docker rm " $1}' | bash


