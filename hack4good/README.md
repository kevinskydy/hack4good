INSTALLATION
===================
- pip install -r pip.txt
- createdb -U <user>
- cd hack4good/hack4good
- cp localsettings.py.template localsettings.py
- cd ..
- python manage.py syncdb
