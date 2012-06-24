#!/bin/bash

#sync game app
rsync -arvu /home/mdobbs/Tumblr/hangtumblr/game mdobbs@mdocode.com:~/webapps/django/hangtumblr

#sync project files: hangblogs, settings, urls
rsync -arvu /home/mdobbs/Tumblr/hangtumblr/hangblogs.py /home/mdobbs/Tumblr/hangtumblr/settings.py /home/mdobbs/Tumblr/hangtumblr/urls.py mdobbs@mdocode.com:~/webapps/django/hangtumblr

#sync static files
rsync -arvu /home/mdobbs/Tumblr/hangtumblr/media/* mdobbs@mdocode.com:~/webapps/dj_tumblr_static/

rsync -arvu /home/mdobbs/Tumblr/hangtumblr/django_templates mdobbs@mdocode.com:~/webapps/dj_tumblr_static/
