## Upload directory from Ubuntu

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
git config --list
git config --global user.name "Luigi Sison"
git config --global user.email lsison@moxylus.com

```
### Upload directory
```
cd odoo-fhir
git init
git add .
git commit -m "Initial Commit" -a
git push origin master
git remote add origin URL
git remote set-url origin URL
git remote -v
git merge origin/master
git push origin master
```
