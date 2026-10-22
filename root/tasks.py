from celery import shared_task
import time

@shared_task
def send_email():
    time.sleep(10)
    print ("email send successfully .... ")