from django.db import models

from account.models import User
from deaf.models import Sentence
from word.models import Word


class FavoriteWord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_words', verbose_name='کاربر')
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='favorite_words', verbose_name='کلمه')

    def __str__(self):
        return str(self.word.title)

    class Meta:
        verbose_name = 'کلمه مورد علاقه'
        verbose_name_plural = 'کلمات مورد علاقه'


class FavoriteSentence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_sentences', verbose_name='کاربر')
    sentence = models.ForeignKey(
        Sentence, on_delete=models.CASCADE, related_name='favorite_sentences', verbose_name='جمله'
    )

    def __str__(self):
        return str(self.sentence.title)

    class Meta:
        verbose_name = "جمله مورد علاقه"
        verbose_name_plural = "حملات مورد علاقه"
