from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy
from dynaconf import settings as _ds

User = get_user_model()


def upload_to(instance: "QRCode", filename):
    return f"{_ds.AWS_S3_CODES_LOCATION}/code_{instance.pk}_{filename}"


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original = models.URLField(null=True, blank=True)
    shortcut = models.URLField(null=True, blank=True)
    confirm = models.BooleanField(default=False)
    utm_copy = models.URLField(null=True, blank=True, editable=False)

    class Meta:
        verbose_name_plural = "url"

    def __str__(self):
        return f"{self.shortcut}(user = {self.user})"

    def get_absolute_url(self):
        return reverse_lazy("statistics:hits", kwargs={"pk": self.pk})
