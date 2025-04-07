from django.db import models


# This would be a job posting that was made from a recruiter
# endpoints to come soon...
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[("open", "Open"), ("closed", "Closed"), ("paused", "Paused")],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.location}"
