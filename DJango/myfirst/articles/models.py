import datetime

from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('article_title', max_length=200)
    article_text = models.TextField('article_text')
    pub_date = models.DateTimeField('publication_date')

    def __str__(self):
        return str(self.id) + ' :: ' + self.article_title

    def was_published_recently(self):
        return self.pub_date > (timezone.now() - datetime.timedelta(days=7))

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('author_name', max_length=50)
    comment_text = models.CharField('comment_text', max_length=200)

    def __str__(self):
        return str(self.id) + ' :: ' +  self.author_name

