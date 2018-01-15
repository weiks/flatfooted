#
# Setup Ubuntu environment for scraping
#
# NOTE: This does not ensure Python 3, extra care must be taken.
#       If necessary, add steps to install virtualenvwrapper,
#       and create a Python 3 environment.
#
sudo apt-get update
sudo apt-get install python-pip libssl-dev -y
sudo pip install -r requirements.txt
