# billo
> Everything around you that you call life was made up by people that were no smarter than you and you can change it, you can influence it, you can build your own things that other people can use.Once you learn that, you’ll never be the same again.” — Steve Jobs

## Set Up Instructions
* Install Homebrew
* Install python 3 using Homebew - brew install python3
* To test everything worked properly, type python3 on terminal and verify that the output displays "Python 3.5.1"
* Navigate to the directory you're setting up the project, in my case it is ~/django/billo for the project and ~/django/bill_env for the virtual environment
* Set up virtual environment, virtualenv -p python3 billo_env
* Activate virtualenv, source "path to virtualenv/bin" activate
* git clone git url
* Install Django, pip3.5 install -r requirements.txt

* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver
