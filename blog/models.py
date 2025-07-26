from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator,MinLengthValidator


# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)
    def tag(self):
        return self.caption
    def __str__(self):
        return self.tag()


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=254)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        

    def __str__(self):
        return self.full_name()
        


class Posts(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, 
                            auto_now_add=False)
    slug = models.SlugField(max_length=50,
                            default="",
                            unique=True,
                            blank=False,
                            null=False,
                            db_index= True,
                            help_text="unique URL path for the post")
    content = models.TextField(validators=[MinLengthValidator(50)])
    author = models.ForeignKey(Author,
                               
                               null = True,
                               on_delete=models.SET_NULL,
                               related_name= "posts")
    tags = models.ManyToManyField(Tag )

    class Meta:
        ordering = ["date"]

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} {self.date} {self.author}"
