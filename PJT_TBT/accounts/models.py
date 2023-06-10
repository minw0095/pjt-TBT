from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    profile_image = ProcessedImageField(
        upload_to="media/",
        blank=True,
        processors=[ResizeToFill(100, 100)],
        format="JPEG",
        options={"quality": 60},
    )
    like_products = models.ManyToManyField(
        "products.Product", related_name="like_users"
    )

    def profile_image1(self):
        if self.profile_image and hasattr(self.profile_image, "url"):
            return self.profile_image.url

    def __self__(self):
        return self.name
