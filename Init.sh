#!/usr/bin/env bash
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test