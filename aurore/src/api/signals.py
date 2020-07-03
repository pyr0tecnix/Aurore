from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from uuid import uuid4


from api.models import Alarm
from api.tasks import schedule_alarm, activate, deactivate

# Signals

@receiver(pre_save, sender=Alarm)
def alarmSaveCallback(sender, **kwargs):
    alarm = kwargs['instance']
    if alarm.pk is None :
        # Create
        task = schedule_alarm(str(uuid4())[:8], alarm.hour.minute, alarm.hour.hour, alarm.days)
        alarm.task_id = task.id
    else:
        # Update
        if alarm.status:
            activate(alarm.task_id)
        else:
            deactivate(alarm.task_id)


@receiver(pre_delete, sender=Alarm)
def alarmDeleteCallback(sender, **kwargs):
    alarm = kwargs['instance']
    deactivate(alarm.task_id)

