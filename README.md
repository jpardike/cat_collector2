## Cat Collector

Feel free to browse these files as a reference.

Or if you want to work off of this project on your machine follow these steps.

1. Clone it down

2. Make sure you are using Python 3.9
```bash
$ brew install python@3.9
```

3. Create a catcollector database if you don't already have one.
```bash
$ createdb catcollector
```

4. Create a new virtual environment in your project with
```bash
$ python3 -m venv .env
$ source .env/bin/activate
```

5. Install its dependencies with
```bash
$ pip3 install -r requirements.txt
```

6. Start your application in the shell where you activated your virtual environment
```bash
$ python3 manage.py runserver
```


