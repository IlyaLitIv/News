from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from .tasks.basic import new_post_subscription
from NewsPaper.rest.models import PostCategory



@receiver(m2m_changed, sender=PostCategory)
def notify_subscribers(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        pass
        new_post_subscription(instance)