from django.db import models
from accounts.models import CustomUser

# Create your models here.


# class Message(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     message = models.TextField()
#     date_posted = models.DateTimeField(auto_now=False, auto_now_add=True)
#     last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    # class Meta:
    #     verbose_name = _("Message")
    #     verbose_name_plural = _("Messages")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Message_detail", kwargs={"pk": self.pk})
