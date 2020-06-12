import time
from django.conf import settings

from huey import crontab
from huey.contrib.djhuey import task, periodic_task

def tprint(s, c=42):
    # Helper to print messages from within tasks using color, to make them
    # stand out in examples.
    print('\x1b[1;%sm%s\x1b[0m' % (c, s))

def alarm(name):
    print('Running : "%s" alarm' % name)

@task()
def schedule_alarm(alarm_name, cron_minutes, cron_hours, cron_days):
    def wrapper():
        alarm(alarm_name)

    # The schedule that was specified for this task.
    schedule = crontab(minute = cron_minutes, hour = cron_hours, day_of_week = cron_days)

    periodic_task(schedule, name=alarm_name)(wrapper)


# def activate(task_id):
