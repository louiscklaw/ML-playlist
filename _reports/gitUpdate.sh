#!/usr/bin/env bash

set -ex

git add . 

git commit -m"update reports,"

git push &
