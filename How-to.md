## Setup - Do once

### Install Git dependencies
```
sudo apt-get install build-essential libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext unzip
```

### Install Git
```
wget https://github.com/git/git/archive/v2.8.0.zip -0 git.zip
unzip git.zip
cd git-*
sudo make prefix=/usr/local install
```
### Register GitHub account
```
git config --list
git config --global user.name "Luigi Sison"
git config --global user.email lsison@moxylus.com
```
### Create local repository
```
cd odoo-fhir
git init
```
## Do every time a change occurs

### Upload changes
```
cd odoo-fhir
sudo git add .
sudo git commit -m "Initial Commit" -a
sudo git push origin master
```

###Update local repository 

When remote repository changes or when error "! [rejected] master -> master (fetch first) error" occurs
```
sudo git fetch origin
sudo git pull origin master
```

##Make changes
* Change module 
* Logout Odoo
* Stop server
* Close VM
* Start VM
* Start server
* Login Odoo
* Activate developer mode
* Upgrade module
* Verify change
