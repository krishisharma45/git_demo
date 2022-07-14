#!/usr/bin/env bash

export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1
export BUILDKIT_INLINE_CACHE=1

if [ "$(docker info | grep Runtimes | grep -o nvidia)" == "nvidia" ]; then
  export DOCKER_RUNTIME="nvidia"
else
  export DOCKER_RUNTIME="runc"
fi