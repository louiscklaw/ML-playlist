#!/usr/bin/env bash
set -x

: <<'END_COMMENT'
reset
pyenv deactivate
pyenv uninstall -f openai_gym_helloworld
pyenv virtualenv 3.9 openai_gym_helloworld
pyenv activate openai_gym_helloworld
END_COMMENT

pip install "gymnasium[all]"
