from django.db import models

# Create your models here.


class Researcher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return '{}'.format(self.name)


class Paper(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    pub_date = models.DateField()
    url = models.URLField()

    def __str__(self):
        return "{} - {}, {}".format(self.title, self.pub_date, self.url)


class Author(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.researcher.name, self.paper.title)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Classification(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category
