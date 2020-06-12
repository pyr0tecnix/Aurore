from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver


from api.models import Alarm
from api.tasks import schedule_alarm

# Signals

@receiver(pre_save, sender=Alarm)
def alarmSaveCallback(sender, **kwargs):

    alarm = kwargs['instance']
    print(alarm)

    if alarm.pk is None :
        print(alarm.hour)
        task = schedule_alarm(alarm.name, alarm.hour.minute, alarm.hour.hour, alarm.days)
        alarm.task_id = task.id
    else:
        print("Update")


@receiver(pre_delete, sender=Alarm)
def alarmDeleteCallback(sender, instance, **kwargs):
    print("Delete")

