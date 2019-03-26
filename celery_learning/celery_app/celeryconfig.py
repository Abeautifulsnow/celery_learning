# -*- coding: utf-8 -*-
from datetime import timedelta
# 定时任务crontab
from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
CELERY_TIMEZONE = 'Asia/Shanghai'



# 导入指定的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)

# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=10),
        'args': (14, 14)
    },
    'task2': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=10, minute=37),
        'args': (9, 9),
    }
}