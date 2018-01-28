sudo apt-get update
sudo apt-get install python3-pip libssl-dev chromium-browser docker -y
sudo -H pip3 install --upgrade pip
sudo -H pip3 install -r requirements.txt
sudo docker pull scrapinghub/splash
