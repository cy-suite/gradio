#!/bin/bash

set -e
git pull origin master

old_version=$(ggrep -Po "(?<=version=\")[^\"]+(?=\")" setup.py)
echo "Current version is $old_version. New version?"
read new_version
gsed -i "s/version=\"$old_version\"/version=\"$new_version\"/g" setup.py

read -p "frontend updates? " -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo -n $new_version > gradio/version.txt
    cd frontend
    npm run build
    cd ..
    aws s3 cp gradio/templates/frontend s3://gradio/$new_version/ --recursive 
fi

rm -r dist/*
rm -r build/*
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
git add -A
git commit -m "updated PyPi version to $new_version"
git push origin master
