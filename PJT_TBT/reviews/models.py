from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, Thumbnail
from products.models import Product
from django.conf import settings

# Create your models here.
# rate = (
#     (1, 1),
#     (2, 2),
#     (3, 3),
#     (4, 4),
#     (5, 5),
# )


class Review(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    grade = models.IntegerField(default=3)
    review_image = ProcessedImageField(
        upload_to="review_images/",
        blank=True,
        processors=[ResizeToFill(500, 500)],
        format="JPEG",
        options={"quality": 80},
    )
    thumbnail = ImageSpecField(
        source="review_image",
        processors=[Thumbnail(200, 200)],
        format="JPEG",
        options={"quality": 60},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes")
