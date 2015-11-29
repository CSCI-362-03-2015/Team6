Install web2py with eden to /home/web2py/ following instructions from eden website install When prompted, choose option one(medium install).

python web2py.py --no-banner -M -S eden -R applications/eden/tests/edentest_runner.py -A applications/eden/tests/implementation/testsuites/{testsuite you want to run}

cp test/execution/config.example.py /test/execution/config.py edit config to have right password

clear database cd web2py/eden/ rm databases/* sessions/* errors/*

launch web2py

register user email: admin@example.com password: testing

install google chrome

download chromedriver and put it in your bash path

SYMLINK the repo: sudo ln -s /home/www-data/Team6 /home/www-data/web2py/applications/eden/tests/implementation/testsuites

To run the testing framework:
cd to Team6/scripts
run command: ./runAllTests.sh

Results will automatically be displayed in browser