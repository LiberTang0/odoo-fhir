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
# sudo wget https://raw.githubusercontent.com/luigisison/healthcare/master/create-module.sh

# Make the file executable:
# sudo chmod +x create_module.sh
# Execute the script to install Odoo:
# ./create_module.sh
################################################################################# 

./odoo.py scaffold hc_procedure addons
./odoo.py scaffold hc_family_member_history addons
cd addons
sudo mv hc_procedure /odoo/custom/addons/hc_procedure
sudo mv hc_family_member_history /odoo/custom/addons/hc_family_member_history
echo "-----------------------------------------------------------"
echo "Done! The module directories have been created."
echo "-----------------------------------------------------------"
