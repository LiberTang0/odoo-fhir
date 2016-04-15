## Upload directory from Ubuntu

### Install Git
```
wget https://github.com/git/git/archive/v2.8.0.zip -0 git.zip
unzip git.zip
cd git-*
```

```
sudo make prefix=/usr/local install
git config --list
git config --global user.name "Luigi Sison"
git config --global user.email lsison@moxylus.com

nano ~/.gitconfig

sudo scp -r /odoo/custom/addons/hc_condition luigisison@github.com:Odoo-FHIR

mkdir -p ~/git/testing ; cd ~/git/testing
```
### Upload directory
```
cd MODULE
git init
git add .
git commit -m "Initial Commit" -a
git push origin master
git remote add origin URL
git remote set-url origin URL
git remote git remote -v
git merge origin/master
git push origin master
```
