#!/usr/bin/env bash
#
# Train model

source bin/setup_environment.sh

docker-compose run --rm app python -m src.training.training_session "$@"
