from django.db.models.signals import pre_save, post_save, pre_delete
from django.contrib.contenttypes.models import ContentType
from .models import History

class HistoryTrackerMixin:
    def save(self, *args, **kwargs):
        if self.pk is not None:
            pre_save.connect(self._pre_save_handler, sender=self.__class__)
        super().save(*args, **kwargs)
        post_save.connect(self._post_save_handler, sender=self.__class__)

    def delete(self, *args, **kwargs):
        pre_delete.connect(self._pre_delete_handler, sender=self.__class__)
        super().delete(*args, **kwargs)

    def _pre_save_handler(self, sender, instance, **kwargs):
        self._old_instance = sender.objects.get(pk=self.pk)

    def _post_save_handler(self, sender, instance, created, **kwargs):
        action = 'create' if created else 'update'
        changes = self._compare_instances(self._old_instance, instance) if not created else instance.__dict__
        self._create_history(action, changes)
        pre_save.disconnect(self._pre_save_handler, sender=self.__class__)
        post_save.disconnect(self._post_save_handler, sender=self.__class__)

    def _pre_delete_handler(self, sender, instance, **kwargs):
        self._create_history('delete', instance.__dict__)
        pre_delete.disconnect(self._pre_delete_handler, sender=self.__class__)

    def _compare_instances(self, old_instance, new_instance):
        changes = {}
        for field in old_instance._meta.fields:
            old_value = getattr(old_instance, field.name)
            new_value = getattr(new_instance, field.name)
            if old_value != new_value:
                changes[field.name] = {'old': old_value, 'new': new_value}
        return changes

    def _create_history(self, action, changes):
        History.objects.create(
            action=action,
            content_type=ContentType.objects.get_for_model(self),
            object_id=self.pk,
            changes=changes
        )
