from datetime import datetime
from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from django.urls import reverse
# from django.core.validators import MinValueValidator


class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating_author = models.IntegerField(default = 0)

    def update_rating(self):
        rating_posts_author = Post.objects.filter(author_id=self.pk).aggregate(rating=Sum('rating_post'))['rating']
        rating_comments_author = Comment.objects.filter(user_id=self.user).aggregate(comment_rating=Sum('rating_comment'))['comment_rating']
        rating_comments_posts = Comment.objects.filter(post__author__user=self.user).aggregate(comment_rating=Sum('rating_comment'))['comment_rating']
        self.rating_author = rating_posts_author * 3 + rating_comments_author + rating_comments_posts
        self.save()


class Category(models.Model):
    name_category = models.CharField(null=True, max_length = 255, unique=True)
    # subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')

    def subscribe(request, pk):
        category = Category.objects.get(pk=pk)
        category.subscribers.add(request.user.id)


class Post(models.Model):
    article = 'AR'
    news = 'NW'

    POST_TYPES = [
        (article, 'статья'),
        (news, 'новость'),
    ]

    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    choice = models.CharField(choices = POST_TYPES, max_length = 2)
    time_post = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, through = 'PostCategory', related_name = 'posts')
    header = models.CharField(max_length = 255)
    text = models.TextField()
    rating_post = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.choice.title()}: {self.header[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def like_post(self):
        self.rating_post += 1
        self.save()

    def dislike_post(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...' if len(self.text) > 124 else self.text


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    date_time_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like_comment(self):
        self.rating_comment += 1
        self.save()
        return self.rating_comment

    def dislike_comment(self):
        self.rating_comment -= 1
        self.save()
        return self.rating_comment


class Appointment(models.Model):
    date = models.DateField(default=datetime.utcnow)
    client_name = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return f'{self.message}'

