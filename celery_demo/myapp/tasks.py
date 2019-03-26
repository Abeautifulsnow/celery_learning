#!usr/bin/env python
# -*- coding:utf-8 -*-
import time
from celery_demo import celery_app


@celery_app.task
def send_email(email):
    print 'Start send email to %s' % email
    time.sleep(20)
    print 'Success'
    return True
