from django.db import models

# Create your models here.
# class AllProduct(models.Model):
#     product_name = models.CharField(max_Length=100)
#     product_type = models.CharField(max_Length=100)
#     product_price = models.CharField(max_Length=100)
#     product_detail = models.TextField(null=True, blanl=True)

#     def __str__(self):
#         return self.product_name

# class PhotoPattern(models.Model):
#     pattern_name = models.CharField(max_Length=100)
#     pattern_detail = models.TextField(null=True, blanl=True)

#     def __str__(self):
#         return self.pattern_name


























class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'