#!/bin/bash
cd /home/daniil/Processing-requests-and-templates/3.2-crud/stocks_products
export DJANGO_SETTINGS_MODULE=stocks_products.settings
git pull origin ci
source env/bin/activate
python manage.py migrate
sudo systemctl restart gunicorn
