### Install
 - ```pip install -r requirements.txt```
 - ```python index.py```

####Creating an web app with Python Bottle

Source of inspiration: https://onetimesecret.com

Key features:
 - Create records with text with one-time reading
 - User and admin views
 - Generate qr code and shorten url

#### python development
    Virtualenv is a python way to limit packages installation and other interaction of the piece of software to selected pre-configured 'virtual folder'. 
    Creating a custom sandbox (for example with python v2.7) in folder name abc:
    ```
    virtualenv -p /usr/bin/python2.7 abc
    source abc/bin/activate
    pip ... 
    deactivate
    ```

#####framework
    Available options: Flask, django, bottle
    Tutorial on configuring bottle - http://bottlepy.org/docs/dev/tutorial_app.html

##### Generating short url
    Use module requests
    And API of tiny url: http://www.tiny-url.info/

####### Extra tips
    - using modules in Python
    - move configs to separate  files
    - using templates
    - including libraries

##### Database: mongodb
    How to install mongodb: http://www.bigspaceship.com/mongodb-on-mac/
    https://docs.mongodb.com/v3.2/tutorial/install-mongodb-on-os-x/
    
    Running mongodb on local machine: 
    ```
    mongod --dbpath <path to data directory>
    ````

    Tutorial: http://api.mongodb.com/python/current/tutorial.html
