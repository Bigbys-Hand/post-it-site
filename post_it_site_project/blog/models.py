from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Django makes each class its own table in the DB
# This class governs content posts. It has title, content, date_posted, and author functions, which will be DB fields.
# We did not add parentheses on timezone.now so that we can call the function repeatedly instead of running it now.
# We import the User class so that each post can have an author. 'on_delete' is meant to handle the post if the author
# is deleted. 'models.CASCADE' means that when the user-author is deleted, so is the post.