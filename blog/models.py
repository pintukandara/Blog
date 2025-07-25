from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    emai_address = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Posts(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    image_name = models.ImageField(upload_to="blog/images",
                                   height_field=None,
                                   width_field=None,
                                   max_length=None)
    date = models.DateField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(max_length=50,
                            default="",
                            unique=True,
                            blank=False,
                            null=False,
                            help_text="unique URL path for the post")
    content = models.CharField(max_length=1000,
                               blank=False,
                               null=False,
                               db_index=True)
    author = models.ForeignKey(Author,
                               verbose_name=("Author's Name"),
                               on_delete=models.CASCADE)

    class Meta:
        ordering = ["date"]

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} {self.date} {self.author}"
