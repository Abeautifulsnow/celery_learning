#!usr/bin/env python
# -*- coding:utf-8 -*-
import os
from celery import Celery
from django.conf import settings

# 获取项目名称
project_name = os.path.split(os.path.abspath('.'))[-1]
project_settings = '%s.settings' % project_name

# 设置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", project_settings)

# 实例化celery
app = Celery(project_name)

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)


# 有些情况可以防止死锁
CELERYD_FORCE_EXECV = True

# 设置并发的worker数
CELERYD_CONCURRENCY = 4

# 允许重试
CELERY_ACKS_LATE = True

# 每个worker最多执行100个任务被销毁，可以防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务的最大运行时间
CELERYD_TASK_TIME_LIMIT = 12 * 30

