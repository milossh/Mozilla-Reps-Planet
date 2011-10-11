#!/bin/bash
source ./env/bin/activate
cd rplanet
python manage.py update_all_feeds
deactivate
