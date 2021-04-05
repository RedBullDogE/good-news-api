# Good News API

MVP project of news board with ability to create and manipulate posts and comments.

Postman documentation is [here](https://documenter.getpostman.com/view/10340815/TzCQc72P)

Deployment link is [here](https://good-news-api.herokuapp.com/api/posts/)

## Annotations
Code was formatted with Black, passed flake8 checks and additionally went through isort. All validations was added to pre-commit hooks.

Recurring task for reseting upvote counters of all posts was implemented with Celery. Initially this feature works every day at 0:00. On deployment 
it triggers every ten minutes for clarity.

**Note:** due to heroku limits for number of workers (in particular for celery/celery beat), on deployment was used heroku scheduler and custom 
django command for reseting number of upvotes. Perhaps this can be solved in some other way.

All data were paginated to prevent failures during retrieving large number of records.

## Local running
To run this application locally you simply need to clone this project:

`git clone https://github.com/RedBullDogE/good-news-api`

Add `.env.dev` config file with the following variables:

```env
DEBUG=1
SECRET_KEY="jl^0)k+%w#lrqnl46c0-u1h8s@@12v+vxf!h@*l7r6=6+4wh(m"
DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]"

DATABASE=postgres
POSTGRES_USER=user
POSTGRES_PASSWORD=passwd123
POSTGRES_DB=news_db
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

Run docker-compose:

`docker-compose up -d --build`

And after successfully launching all containers, you need to apply migrations:

`docker-compose exec api python manage.py migrate`
