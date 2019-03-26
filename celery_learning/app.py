# -*- coding: utf-8 -*-
import time
from tasks import add
from celery_app import task1, task2


task1.add.delay(2, 4)
task2.multiply.delay(4 ,5)
print('end ......')

# if __name__ == "__main__":
#     print('Start task...')
#     result = add.delay(2, 12)
#     print('End task...')
#     print(result)
