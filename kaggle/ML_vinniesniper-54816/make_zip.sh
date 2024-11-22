#!/usr/bin/env bash

set -ex

# export PYTHONDONTWRITEBYTECODE=1

rm -rf __pycache__

# cd helloworld
# zip -0 -r ../helloworld.zip . *
# cd ..

python ./delete_similiar_img.py
python ./check_valid_image.py
python ./resize_ds_img.py


cd /kaggle/input/ml-vinniesniper-54816-test
  rm -rf ./ml-vinniesniper-54816-test.zip
  zip -0 -r ./ml-vinniesniper-54816-test.zip . *  &
cd ..

cd /kaggle/input/ml-vinniesniper-54816-train
  rm -rf ./ml-vinniesniper-54816-train.zip
  zip -0 -r ./ml-vinniesniper-54816-train.zip . *  &
cd ..

wait

echo "done"
