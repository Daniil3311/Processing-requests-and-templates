#!/bin/bash
cd /home/daniil/Processing-requests-and-templates/3.2-crud/stocks_products
git pull origin ci
source env/bin/activate
python manage.py
sudo systemctl restart gunicorn
