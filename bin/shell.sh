#!/usr/bin/env bash
#
# Run docker container in bash shell session

source bin/setup_environment.sh

if [ $# -eq 0 ]; then
  SERVICE="app"
else
  SERVICE="$*"
fi

docker-compose run --rm --entrypoint bash --service-ports $SERVICE
