from articles.models import Article, Comment
Article.objects.all()
from django.utils import timezone
a = Article(article_title='Title-001', article_text='Text-001', pub_date=timezone.now())
a = Article(article_title='Title-002', article_text='Text-002', pub_date=timezone.now())

a.comment_set.create(author_name='Yan', comment_text='Kruto!')
a.comment_set.create(author_name='Yana', comment_text='Norm!')
a.comment_set.create(author_name='Libby', comment_text='Class!')

a = Article.objects.get(id=1)
a.was_published_recently()
a.comment_set.count()
a.comment_set.all()

a.save()

Article.objects.filter(id=2).delete()
Article.objects.filter(article_title__startswith = 'Title')
a. article_title = 'Title-001-UPDATED'

Comment.objects.filter(id=3).delete()



quit()