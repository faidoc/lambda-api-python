#!/bin/bash

cd docs
export APP_ENV=DEVELOPMENT

sphinx-apidoc -f -o source/ ../
make html