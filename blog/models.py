from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    e_mail = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = "Author"


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = "Tag"


class Post(models.Model):
    post_title = models.CharField(max_length=150)
    post_excerpt = models.CharField(max_length=200)
    post_content = models.TextField(validators=[MinLengthValidator(10)])
    post_slug = models.SlugField(unique=True, db_index=True)
    post_date = models.DateField(auto_now=True)
    post_imagename = models.CharField(max_length=100)
    post_author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    post_tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.post_title}'

    class Meta:
        verbose_name_plural = "Post"
