# Team6

**Note: Make sure to be under root permissions when running all of these commands. Alternative to being under root is to include "sudo" at the beginning of each command.**

#Installation instructions --

Go here to retrieve the installation script:

http://eden.sahanafoundation.org/raw-attachment/wiki/InstallationGuidelines/Linux/Developer/Script/debian_ubuntu_eden_dev.3.2.2.sh

Run using:

sudo bash debian_ubuntu_eden_dev.3.2.2.sh
    **if running from a different directory you will need to run: 

        sudo bash /home/<username>/Downloads/debian_ubuntu_eden_dev.3.2.2.sh

        

This will install web2py into /home/web2py:
The terminal will ask you for a choice:
Medium - installs all mandatory and some common optional dependencies
Quick - installs only mandatory dependencies
Full - installs all optional dependencies & the Eclipse debugger
Select 1 for the medium install

**bugs: encountered errors when running this command. Make sure you run ‘sudo apt-get update’ without any problems. Those will need to be resolved before installation.

**bugs: may need to install pyDAL? get pip with ‘sudo apt-get install python-pip’ then ‘sudo pip install pyDAL’


#Test framework instructions --


Start web2py:
    Start web2py by moving into the web2py main directory and using the command
        
        python web2py.py -a 1234
   
     **May need to install Google Chrome: download chromedriver and put it in your bash path

    
Download Team6 repository:

sudo git clone https://github.com/CSCI-362-03-2015/Team6.git    

Symlink the repository into testsuites folder of Eden:

sudo ln -s /home/www-data/Team6 /home/www-data/web2py/applications/eden/tests/implementation/testsuites

Run the framework while in the Team6 repo:
    
    cd scripts/
    sudo ./runAllTests.sh

