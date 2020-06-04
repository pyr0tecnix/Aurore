from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


from api.models import Alarm

# Signals

@receiver(post_save, sender=Alarm)
def alarmSaveCallback(sender, instance, created, **kwargs):
    if created:
        print("Save")
    else:
        print("Update")


@receiver(pre_delete, sender=Alarm)
def alarmDeleteCallback(sender, instance, **kwargs):
    print("Delete")

