from restcelery.celery import app
from App.models import Task
from time import sleep
import random
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)


@app.task(bind=True)
def process(self,):
    #its a task that conusme 10 seconds
    sleep(10)
    logger.info("its finished")


def girkone():
    sleep(10)
