# Guest demo project

## Hey there!

In this repo, you can find my approach (very simplistic) to solve tech task. 

### What I have done:

0. docker
* packed all project into Docker. You can run it via `docker-compose up -d --build` and access via `http://127.0.0.1:8001/`

1. general:
* put project requirements in Pipfile via pipenv. With old-style requirements.txt it's quite hard to manage all dependencies. Better solutions for that to have something like Pipenv, Poetry, etc.
* added automatic migration into docker-compose.

2. dev experience:
* added `black` and `isort` libraries to keep sorting and code always in the same style.

3. app logic:
* main logic is located in `/demo/rental`

4. results:
* via `http://127.0.0.1:8001/` you can get HTML page with resulting table

5. tests (few simple testcase, thought):
* tests can be run via `docker-compose run --rm rental bash -c "python ./demo/manage.py test rental`
