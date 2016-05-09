# Linux

## Cheatsheet

```
sudo mkdir mydir --create directory
sudo rm -rf mydir --delete directory
clear --clear the terminal screen
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

### Initialize odoo-fhir with content from GitHub
```
cd /odoo
sudo git clone --depth 1 https://github.com/luigisison/odoo-fhir.git
```

### Setup addons directory /odoo/odoo-fhir/addons
```
sudo nano /etc/odoo-server.conf
addons_path=/odoo/enterprise/addons,/odoo/odoo-server/addons,/odoo/odoo-fhir/addons
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

##Update Changes

syntax: ./odoo.py -d <database> --addons-path <directories> -i <modules>
```
cd /odoo/odoo-server
./odoo.py -d FHIR-DEV --addons-path /odoo/odoo-fhir/addons -u hc_base
```

##Error

###ERROR ? openerp.service.server: Failed to load server-wide module `web_kanban`
```
opt/openerp/server$ ./openerp-server --addons-path=web/addons
```

now you can assign multiple addons path,
```
opt/openerp/server$ ./openerp-server --addons-path=web/addons,../addons1,../addons2
```

##Save terminal output to a file

* Start a ```script``` session and save output to ```output.txt``` in the current directory.
```
script output.txt
```

* End a script session
```
exit
```