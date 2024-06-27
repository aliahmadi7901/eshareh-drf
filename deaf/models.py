from django.db import models


class CategoriesOfTheDeaf(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان دسته بندی")
    icon = models.FileField(upload_to='categories_deaf', verbose_name="آیکون")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='categories_deaf', verbose_name='والد')
    url_title = models.URLField(verbose_name="عنوان در url")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی ناشنوایان'
        verbose_name_plural = 'دسته بندی های ناشنوایان'


class Sentence(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان جمله")
    video_url = models.URLField(verbose_name="url ویدیو")
    category = models.ManyToManyField(CategoriesOfTheDeaf, related_name='sentences', verbose_name="دسته بندی حمله")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "جمله"
        verbose_name_plural = "جمله ها"
