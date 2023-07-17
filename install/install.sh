apt update -y
apt install python3 python3-pip ufw -y
ufw enable
ufw allow 3000
mv picam.service /etc/systemd/system/picam.service
systemctl enable picam
mkdir /app
mv ../app/main.py /app/main.py
systemctl start picam
echo "complete!"