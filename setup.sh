sudo pip3 install -r requirements.txt
sudo cp agents_video.conf /etc/supervisor/conf.d/
sudo cp agents_video_nginx.conf /etc/nginx/sites-enabled/
sudo supervisorctl update
sudo systemctl restart nginx
sudo certbot --nginx -d video.medsenger.ru
touch config.py