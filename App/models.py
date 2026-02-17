from django.db import models
from django.utils import timezone
from datetime import timedelta

class Note(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)  # Soft delete flag
    deleted_at = models.DateTimeField(null=True, blank=True)  # Timestamp for soft deletion
    
    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
        
    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()
        
    @classmethod
    def delete_old_notes(cls):
        threshold_date = timezone.now() - timedelta(days=30)
        old_notes = cls.objects.filter(is_deleted=True, deleted_at__lte=threshold_date)
        old_notes.delete()
    
    def __str__(self):
        return self.title

