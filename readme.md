#its a simple rabbitmq celery django
its shows that how rabbitmq is working with celery
we assumed that our task consume 10 seconds , so we created a task in task.py


first run rabbitmq server  as your message broker
then run celery :  celery -A restcelery  worker -l info

in another terminal run celery flower to track requests