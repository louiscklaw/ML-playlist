#!/usr/bin/env bash

set -ex

python ./tensorboard_helloworld.py

tensorboard --logdir=./logs
