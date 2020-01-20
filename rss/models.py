import feedparser
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class RSS(models.Model):
    link = models.URLField(max_length=256, verbose_name='link')
    user = models.ForeignKey(User,
                             related_name='Utente',
                             on_delete=models.CASCADE,
                             null=True)

    class Meta:
        verbose_name = "RSS"
        verbose_name_plural = "RSS"

    def __str__(self):
        return self.link

    def get_title(self):
        d = feedparser.parse(str(self.link))

        try:
            return d.feed.title

        except AttributeError:
            return self.link
