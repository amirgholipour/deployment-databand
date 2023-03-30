#!/bin/bash -e

for i in ./jupyter/*
do
   myipynb=$(basename $i)
   mydocx=$(basename $i .ipynb).docx

   docker run --rm --volume "$(pwd):/data" --user `id -u`:`id -g` pandoc/latex jupyter/$myipynb -o docs/$mydocx

   # docker run --rm --volume "$(pwd)/jupyter:/data" --volume "$(pwd)/pictures:/pictures" --volume "$(pwd)/docs:/docs" --user `id -u`:`id -g` pandoc/latex $myipynb -o ../docs/$mydocx
done

docker run --rm --volume "$(pwd):/data" --user $(id -u):$(id -g) pandoc/latex README.md -o ./docs/README.docx
