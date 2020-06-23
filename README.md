This repository contains the code for sharkjumpcalculator.com, a site that exists to answer the
question, "Does this show that I'm about to watch ever jump the shark?"

Following the instructions below will allow you to run a clone of the website from an Ubuntu machine,
but they should work for other *nix with minimal modifications.

First, we'll set up a virtual environment, so once you're done you can delete everything and your
system won't have changed.

```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
This will create a virtual environment with its own Python interpreter and install the project's dependencies for use only in the environment. If the first command doesn't work for you, you'll need to install python3-venv, which is harmless to have installed on your system:

```
$ sudo apt update
$ sudo apt-get install python3-venv
```

Once you have your virtual environment set up and activated and have installed the project's dependencies to it, you can serve the site by running

```
$ python app.py
```

This will run the development server on port 5000. If you wanted to run it on, e.g., port 8080, you
could run

```
$ flask run --port=8080
```

If you're running the cloned site on a virtual server and want to use its public IP, run


```
$ flask run --host='0.0.0.0'
```

When you're done, enter CTRL-C and the development server will quit. To exit the virtual environment
that you created, run

```
$ deactivate
```
