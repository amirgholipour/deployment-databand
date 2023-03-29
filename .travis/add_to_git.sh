#!/bin/bash -e

if [ -n "$GITHUB_TOKEN" ]
then
  git config user.name "Travis CI"
  git config user.email "Travis CI"
  git checkout -q main
  git add README.pdf
  git commit --allow-empty -m "Update repo [skip ci]"
  git remote add authenticated https://$GITHUB_TOKEN@github.ibm.com/angelito/databand-workshop.git
  git push --quiet authenticated main &>/dev/null
else
  echo Github token not available
fi