## Creating an web app with Python Bottle

Source of inspiration: https://onetimesecret.com

Key features:
 - Create records with text with one-time reading
 - User and admin views
 - Generate qr code and shorten url

### 1. Web application development in Python

Virtualenv is a python way to limit packages installation and other interaction of the piece of software to selected pre-configured 'virtual folder'.  Creating a custom sandbox (for example with python v2.7) in folder name abc:
    ```
    virtualenv -p /usr/bin/python2.7 abc
    source abc/bin/activate
    ```
    then you can install stuff and work with the application and later just call ``` deactivate``` to stop virtualenv.

### 2. Choosing a framework
Among available options: Flask, Django and others bottle was chosen as on of the most lightweight ones. Tutorial on how to configure bottle - http://bottlepy.org/docs/dev/tutorial_app.html

#### Enabling gZip
 ++++ about
 ++++ service to test 
Bottle can't do it, so we're using a more sophisticated WSGY servier which will run bottle ap as a container. We're using cherrypy for this.
See index.py, first we load routes: ```__app__ = routes.app``` then
enable sessions plugin ```app = SessionMiddleware(__app__, config.session_opts)``` and then using the GzipMiddleware method of the wsgigzip package to wrap the application ```application = wsgigzip.GzipMiddleware(app)```
    
#### Routes configuration
Check the routes.py file and you will see several types of routes:
    - ```/api/create``` and ```/api/read``` for AJAX creation
    - ```/assets/<filepath:path>``` - for static files handling
    - ````/create```, ```/secret``` and ```/``` (homepage)

#### Extra functions
Arrange this as a plugins module.
Use module requests in ```plugins/___init___.py```
1) Use [API of tiny url](http://www.tiny-url.info/) to create shortened link.
+++ intput / output JSON
2) Generate QU-code
3) ITTT

##### Extra tips
    - using modules in Python
    - move configs to separate  files
    - using templates
    - including libraries

#### Database: mongodb
How to install [mongodb](http://www.bigspaceship.com/mongodb-on-mac/) , https://docs.mongodb.com/v3.2/tutorial/install-mongodb-on-os-x/
    
Running mongodb on local machine is as simple as that: 
```mongod --dbpath <path to data directory>```

+++++ about GUI tools

Using **pymongo** library and this [python mongodb tutorial](http://api.mongodb.com/python/current/tutorial.html)