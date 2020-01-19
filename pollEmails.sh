#!/bin/bash

cd /home/csss/
. envCSSS/bin/activate
cd csss-site-in-dev/csss-site/src/
. enVariables/setEnv.sh
python3.7 manage.py getmail
deactivate
