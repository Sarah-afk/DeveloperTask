# Task#2: Python

The task is to write a RESTful service in Python that features the following endpoints. Python best practices were applied whereby this service could be part of a larger application later.

• GET /fib/<number>: Given a number, find all combinations of fibonacci number that add up to
that particular number.

Example for /fib/11 the response will be a list of all possible combinations:

[ [2, 2, 2, 2, 3], [2, 2, 2, 5], [2, 3, 3, 3], [3, 3, 5], [8, 3] ]

• GET/health: Return health information about the service. This service will return how many elements are in the cache, the time and the runtime of each request.

## Run without Docker

To test and use this service without docker, run the following commands in terminal:

```bash
git clone https://github.com/Sarah-afk/DeveloperTask.git
cd DeveloperTask
```
The database used for this service must be created before running, hence after cloning this repo and changing directory to its file, the following should be run in terminal:

```bash
python
from database import *
db.create_all()
```
Now that the database is created, exit python and continue running the following in the terminal
```bash
pip install -r requirements.txt
python flask_app.py
```
The terminal will prompt a url that you can Ctrl and click to open the page in browser.

## Run inside Docker
To run inside Docker, first make sure that docker is installed. Create the database if not created before like mentioned above, then run the following in terminal:

```bash
git clone https://github.com/Sarah-afk/DeveloperTask.git
cd DeveloperTask
docker build -t <image name>
docker run -it -p 2224:2224 <image name>:latest
```
The terminal will prompt a url that you can Ctrl and click to open the page in browser.

## Happy Testing!
I hope this task was fulfilled to your standards.

