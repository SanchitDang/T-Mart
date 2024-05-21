from django.db import models
from django.utils import timezone


class ViewHistory(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    visited_times = models.IntegerField(default=0)
    last_visited_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user_id', 'product_id')

    def __str__(self):
        return f"User {self.user_id} viewed Product {self.product_id} {self.visited_times} times"
