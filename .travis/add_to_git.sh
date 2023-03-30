#!/bin/bash -e

if [ -n "$GITHUB_TOKEN" ]
then
  git config user.name "Travis CI"
  git config user.email "Travis CI"
  git checkout -q main
  
  for i in ./docs/*
  do
   git add $i
  done

  git commit --allow-empty -m "[skip travis] create documents via travis "
  git remote add authenticated https://$GITHUB_TOKEN@github.ibm.com/angelito/databand-workshop.git
  git push --quiet authenticated main &>/dev/null
else
  echo Github token not available
fi