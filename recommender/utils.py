from django.utils import timezone
from .models import ViewHistory


def add_view_history(user_id, product_id):
    # Try to get an existing view history entry
    view_history, created = ViewHistory.objects.get_or_create(
        user_id=user_id,
        product_id=product_id,
        defaults={'visited_times': 1, 'last_visited_at': timezone.now()}
    )

    if not created:
        # If the entry exists, update the visited times and last visited timestamp
        view_history.visited_times += 1
        view_history.last_visited_at = timezone.now()
        view_history.save()

    return view_history
