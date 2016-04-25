# Linux

## Cheatsheet

```
cd /odoo
sudo mkdir odoo-fhir --create directory named odoo-fhir
sudo rm -rf odoo-fhir --delete directory
```

# GitHub

* Reference: [How to Install Git on Ubuntu] (https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-14-04)
* Reference: [Git - Installng Git] (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Reference: [Ubuntu Server Guide] (https://help.ubuntu.com/lts/serverguide/git.html)

## Setup - Do once

### Install Git dependencies
```
sudo apt-get install build-essential libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext unzip
```

### Install Git
```
cd /opt
sudo wget https://github.com/git/git/archive/v2.8.0.zip -O git.zip
sudo unzip git.zip
cd git-*
sudo make prefix=/usr/local install
```
### Register GitHub account
```
git config --list
git config --global user.name "Luigi Sison"
git config --global user.email lsison@moxylus.com
```
### Create local repository odoo-fhir
```
cd /odoo
sudo mkdir odoo-fhir
cd odoo-fhir
sudo git init
```
## Download content from GitHub



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
