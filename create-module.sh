#!/bin/bash
################################################################################
# Script for installing Odoo V9 on Ubuntu 14.04 LTS (could be used for other versions too)
# Original Author: Yenthe Van Ginneken; Additions: Luigi Sison
# Original Source: http://www.odoo.yenthevg.com/installing-odoo-9-enterprise-on-ubuntu-14-04/
#-------------------------------------------------------------------------------
# This script will install Odoo Enterprise on your Ubuntu 14.04 server.
# Installation of enterprise programs requires an Odoo-approved Github username and password.
# It can install multiple Odoo instances in one Ubuntu because of the different xmlrpc_ports.
#-------------------------------------------------------------------------------
# Go to Ubuntu directory where you want to install the software. For example:
# cd /odoo/odoo-server
# Place this script in the directory:
# sudo wget https://raw.githubusercontent.com/luigisison/moxylus/master/Odoo9Enterprise/odoo-install.sh
# (Optional) Edit the file to change parameters:
# sudo nano odoo-install.sh
# Save changes and then make the file executable:
# sudo chmod +x odoo-install.sh
# Execute the script to install Odoo:
# ./odoo-install.sh
################################################################################# cd /odoo/odoo-server
./odoo.py scaffold hc_allergy_intolerance addons
cd addons
sudo mv hc_allergy_intolerance /odoo/custom/addons/hc_allergy_intolerance
