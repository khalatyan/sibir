import pytils

from django.db import models
from django.utils.html import format_html
from django.utils import timezone
from django.db.models import Q

from filer.fields.image import FilerImageField
from filer.fields.folder import FilerFolderField
from filer.fields.file import FilerFileField
from filer.models import Image
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.files import get_thumbnailer

from seo.models import SEO

class Static(SEO):

    """
    Текстовые разделы
    """

    title = models.CharField(
        max_length=512,
        verbose_name=u'Заголовок'
    )
    content = RichTextUploadingField(
        verbose_name=u'Контент'
    )

    active = models.BooleanField(
        default=True,
        verbose_name=u'Активный'
    )

    slug = models.CharField(
        verbose_name=u'Слаг',
        unique=True,
        max_length=100,
        blank=True,
        null=True,
        help_text=u'Оставить пустым, чтобы сгенерировался автоматически'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "%s" % self.slug

    class Meta:
        verbose_name = u'текстовый раздел'
        verbose_name_plural = u'Текстовые разделы'

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = self.slugify(self.title)
            slugs = set(
                self.__class__._default_manager.filter(
                    slug__startswith=self.slug
                ).values_list("slug", flat=True)
            )
            i = 1
            slug = self.slug
            while True:
                if slug not in slugs:
                    self.slug = slug
                    return super().save(*args, **kwargs)
                slug = self.slugify(self.title, i)
                i += 1
        else:
            return super().save(*args, **kwargs)

    def slugify(self, tag, i=None):
        slug = slugify(unidecode(tag))
        if i is not None:
            slug += "_%d" % i
        return slug


class Project(models.Model):

    '''
    Проекты
    '''

    title = models.CharField(
        verbose_name=u'Название',
        max_length=64,
        blank=True,
        null=True
    )

    description = RichTextUploadingField(
        verbose_name=u'Описание',
        blank=True,
        null=True
    )

    date = models.DateField(
        verbose_name=u'Дата публикации',
        default=timezone.now
    )

    on_gallery = models.BooleanField(
        verbose_name='Показать в Галерее?',
        default=True,
    )

    link = models.CharField(
        max_length=512,
        verbose_name=u'URL адрес',
        blank=True,
        null=True
    )

    folder = FilerFolderField(
        verbose_name=u'Папка',
        on_delete=models.CASCADE,
        default=None,
        null=True
    )


    def __str__(self):
        return u'[%s] %s' % (self.id, self.title)


    def get_cover(self):
        cover = AlbumCover.objects.filter(album_id=self.id).first()
        return cover

    def get_cover_admin(self):
        try:
            return format_html('<img src="{0}"/ width="300px">', self.get_cover().image.url)
        except:
            return False

    get_cover_admin.allow_tags = True
    get_cover_admin.short_description = u'Обложка'

    def get_photos(self):
        return Image.objects.filter(folder=self.folder)


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.link:
            super(Album, self).save()

            link = '%s' % pytils.translit.slugify(self.title + str(self.id))
            self.link = link
        super(Album, self).save()

    class Meta:
        ordering = ['-date', ]
        verbose_name = u"галерея"
        verbose_name_plural = u"Галерея"


class Category(models.Model):

    """
    Категория товаров
    """

    title = models.CharField(
        max_length=512,
        verbose_name=u'Заголовок'
    )

    slug = models.CharField(
        verbose_name=u'Слаг',
        unique=True,
        max_length=100,
        blank=True,
        null=True,
        help_text=u'Оставить пустым, чтобы сгенерировался автоматически'
    )


    order = models.PositiveSmallIntegerField(
        verbose_name='Порядок',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "%s" % self.slug

    class Meta:
        verbose_name = u'категория товаров'
        verbose_name_plural = u'Категории товаров'
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = self.slugify(self.title_block)
            slugs = set(
                self.__class__._default_manager.filter(
                    slug__startswith=self.slug
                ).values_list("slug", flat=True)
            )
            i = 1
            slug = self.slug
            while True:
                if slug not in slugs:
                    self.slug = slug
                    return super().save(*args, **kwargs)
                slug = self.slugify(self.title_block, i)
                i += 1
        else:
            return super().save(*args, **kwargs)

    def slugify(self, tag, i=None):
        slug = slugify(unidecode(tag))
        if i is not None:
            slug += "_%d" % i
        return slug


class GoodsCategory(models.Model):

    """
    Категория товаров
    """

    title = models.CharField(
        max_length=512,
        verbose_name=u'Заголовок'
    )

    title_block = models.CharField(
        max_length=512,
        verbose_name=u'Заголовок внутри блока',
        blank=True,
        null=True,
    )

    active = models.BooleanField(
        default=True,
        verbose_name=u'Активный'
    )

    slug = models.CharField(
        verbose_name=u'Слаг',
        unique=True,
        max_length=100,
        blank=True,
        null=True,
        help_text=u'Оставить пустым, чтобы сгенерировался автоматически'
    )

    category_icon_text = models.TextField(
        verbose_name='Иконка для категории текстом',
        blank=True,
        null=True,
    )

    order = models.PositiveSmallIntegerField(
        verbose_name='Порядок',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "%s" % self.slug

    class Meta:
        verbose_name = u'категория товаров'
        verbose_name_plural = u'Категории товаров'
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = self.slugify(self.title_block)
            slugs = set(
                self.__class__._default_manager.filter(
                    slug__startswith=self.slug
                ).values_list("slug", flat=True)
            )
            i = 1
            slug = self.slug
            while True:
                if slug not in slugs:
                    self.slug = slug
                    return super().save(*args, **kwargs)
                slug = self.slugify(self.title_block, i)
                i += 1
        else:
            return super().save(*args, **kwargs)

    def slugify(self, tag, i=None):
        slug = slugify(unidecode(tag))
        if i is not None:
            slug += "_%d" % i
        return slug



class Good(models.Model):

    """
    Товары
    """

    title = models.CharField(
        max_length=512,
        verbose_name=u'Заголовок'
    )

    category = models.ForeignKey(
        Category,
        verbose_name=u'категория',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    description = RichTextUploadingField(
        verbose_name=u'Описание'
    )

    active = models.BooleanField(
        default=True,
        verbose_name=u'Активный'
    )

    price_hour = models.CharField(
        verbose_name=u'Цена товара за час',
        max_length=64,
        blank=True,
        null=True
    )

    price_change = models.CharField(
        verbose_name=u'Цена товара за смену',
        max_length=64,
        blank=True,
        null=True
    )

    good_image = FilerImageField(
        verbose_name='Фотография',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    order = models.PositiveSmallIntegerField(
        verbose_name='Порядок',
        blank=True,
        null=True,
    )


    def __str__(self):
        return self.title

    def get_thumbnail(self):
        return format_html('<img src="{0}"/ width="200px">', self.good_image.url)

    get_thumbnail.allow_tags = True
    get_thumbnail.short_description = u'Фото'

    class Meta:
        verbose_name = u'товар'
        verbose_name_plural = u'Товары'
        ordering=["order"]


class Certificate(models.Model):

    """
    Компании-партнеры
    """

    title = models.CharField(
        verbose_name=u'Наименование',
        max_length=128
    )

    cover = FilerImageField(
        verbose_name=u'сертификат',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    on_main = models.BooleanField(
        verbose_name=u'Отображать на главной',
        default=True
    )


    def get_thumbnail(self):
        image = '-'
        if self.cover:
            image = format_html('<img src="{0}"/>', get_thumbnailer(self.cover)['news_item_200x200'].url)
        return image
    get_thumbnail.allow_tags = True
    get_thumbnail.short_description = u'Логотип'

    class Meta:
        verbose_name = u'сертификат'
        verbose_name_plural = u'Сертификаты'
        ordering = ['title']


class FAQItem(models.Model):

    '''
    Вопросы и ответы
    '''

    order = models.PositiveSmallIntegerField(
        verbose_name='Порядок',
    )

    question = models.CharField(
        verbose_name='Вопрос',
        max_length=256,
    )

    answer = models.TextField(
        verbose_name='Ответ',
    )

    is_active = models.BooleanField(
        verbose_name='Активен',
        default=True,
    )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'
        ordering = ['order']


class AboutUsInNumbers(models.Model):

    '''
    О нас в цифрах
    '''

    number = models.IntegerField(
        verbose_name='Цифра',
    )

    title = models.TextField(
        verbose_name='Заголовок',
    )

    is_active = models.BooleanField(
        verbose_name='Активен',
        default=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас в цифрах'
        verbose_name_plural = 'О нас в цифрах'
