from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating_author = models.IntegerField(default = 0)

    def update_rating(self):
        rating_posts_author = Post.objects.filter(author_id=self.pk).aggregate(rating=Sum('rating'))['rating']
        rating_comments_author = Comment.objects.filter(user_id=self.user).aggregate(comment_rating=Sum('comment_rating'))['comment_rating']
        rating_comments_posts = Comment.objects.filter(post__author__user=self.user).aggregate(comment_rating=Sum('comment_rating'))['comment_rating']
        self.user_rating = rating_posts_author * 3 + rating_comments_author + rating_comments_posts
        self.save()

class Category(models.Model):
    name_category = models.CharField(null=True, max_length = 255)
    unique = True

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
    category = models.ManyToManyField(Category, through = 'PostCategory')
    header = models.CharField(max_length = 255)
    text = models.TextField()
    rating_post = models.IntegerField(default = 0)

    def like_post(self):
        self.like_post += 1
        self.save()

    def dislike_post(self):
        self.dislike_post -= 1
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


