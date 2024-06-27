from django.db import models


class CategorizeWord(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان دسته بندی')
    icon = models.FileField(upload_to='categorize', verbose_name='آیکون')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='categorize_words', verbose_name='والد'
    )
    url_title = models.URLField(verbose_name='عنوان در url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی کلمه'
        verbose_name_plural = 'دسته بندی کلمات'


class Word(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان کلمه')
    pronunciation_of_the_word = models.CharField(max_length=100, verbose_name='تلفظ کلمه')
    image = models.ImageField(upload_to='words', verbose_name='تصویر کلمه')
    video_url = models.URLField(verbose_name='url ویدیو')
    categorize_word = models.ManyToManyField(CategorizeWord, related_name='words', verbose_name='دسته بندی کلمه')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کلمه'
        verbose_name_plural = 'کلمات'
