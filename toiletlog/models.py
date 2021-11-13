from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse_lazy
from django.core import validators


class Prefecture(models.IntegerChoices):
    NULL = 0, ('--')
    HOKKAIDO = 1, ('北海道')
    AOMORI = 2, ('青森県')
    IWATE = 3, ('岩手県')
    MIYAGI = 4, ('宮城県')
    AKITA = 5, ('秋田県')
    YAMAGATA = 6, ('山形県')
    FUKUSHIMA = 7, ('福島県')
    IBARAKI = 8, ('茨城県')
    TOCHIGI = 9, ('栃木県')
    GUNMA = 10, ('群馬県')
    SAITAMA = 11, ('埼玉県')
    CHIBA = 12, ('千葉県')
    TOKYO = 13, ('東京都')
    KANAGAWA = 14, ('神奈川県')
    NIIGATA = 15, ('新潟県')
    TOYAMA = 16, ('富山県')
    ISHIKAWA = 17, ('石川県')
    FUKUI = 18, ('福井県')
    YAMANASHI = 19, ('山梨県')
    NAGANO = 20, ('長野県')
    GIFU = 21, ('岐阜県')
    SHIZUOKA = 22, ('静岡県')
    AICHI = 23, ('愛知県')
    MIE = 24, ('三重県')
    SHIGA = 25, ('滋賀県')
    KYOUTO = 26, ('京都府')
    OSAKA = 27, ('大阪府')
    HYOUGO = 28, ('兵庫県')
    NARA = 29, ('奈良県')
    WAKAYAMA = 30, ('和歌山県')
    TOTTORI = 31, ('鳥取県')
    SHIMANE = 32, ('島根県')
    OKAYAMA = 33, ('岡山県')
    HIROSHIMA = 34, ('広島県')
    YAMAGUCHI = 35, ('山口県')
    TOKUSHIMA = 36, ('徳島県')
    KAGAWA = 37, ('香川県')
    EHIME = 38, ('愛媛県')
    KOCHI = 39, ('高知県')
    FUKUOKA = 40, ('福岡県')
    SAGA = 41, ('佐賀県')
    NAGASAKI = 42, ('長崎県')
    KUMAMOTO = 43, ('熊本県')
    OITA = 44, ('大分県')
    MIYAZAKI = 45, ('宮崎県')
    KAGOSHIMA = 46, ('鹿児島県')
    OKINAWA = 47, ('沖縄県')


class Sex(models.IntegerChoices):
    SHARE = 0, ('共用トイレ')
    MAN = 1, ('男子トイレ')
    WOMAN = 2, ('女子トイレ')


class Type(models.IntegerChoices):
    WESTERN = 0, ('洋式トイレ')
    JAPANESE = 1, ('和式トイレ')
    BOTH = 2, ('両方あり')


class Washlet(models.IntegerChoices):
    ATTACHED = 0, ('ウォシュレットあり')
    NOT_ATTACHED = 1, ('ウォシュレットなし')
    BOTH = 2, ('両方あり')


class Cleanliness(models.IntegerChoices):
    GOOD = 0, ('すごく綺麗')
    LITTLE_GOOD = 1, ('やや綺麗')
    LITTLE_BAD = 2, ('やや汚い')
    BAD = 3, ('すごく汚い')


class Toilet(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False,
    )

    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False,
    )

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='タイトル',
    )

    prefecture = models.IntegerField(
        choices=Prefecture.choices,
        validators=[validators.MinValueValidator(1)],
        default=0,
        verbose_name='都道府県',
    )

    city = models.CharField(
        blank=False,
        null=False,
        max_length=255,
        verbose_name='市区町村',
    )

    address = models.CharField(
        blank=False,
        null=False,
        max_length=255,
        verbose_name='番地',
    )

    building = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='建物名',
    )

    sex = models.IntegerField(
        choices=Sex.choices,
        default=0,
        verbose_name='何トイレ',
    )

    type = models.IntegerField(
        choices=Type.choices,
        default=0,
        verbose_name='種類',
    )

    washlet = models.IntegerField(
        choices=Washlet.choices,
        default=0,
        verbose_name='ウォシュレット',
    )

    cleanliness = models.IntegerField(
        choices=Cleanliness.choices,
        default=0,
        verbose_name='綺麗さ',
    )

    info = models.TextField(
        blank=True,
        max_length=1000,
        verbose_name='情報',
    )

    image = models.ImageField(
        upload_to='images',
        blank=True,
        null=True,
        verbose_name='トイレ画像',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])


def validate_rate(value):
    if value > 0 or value <= 5:
        raise ValidationError('1~5で評価してください')


class Comment(models.Model):
    rate = models.IntegerField(validators=[validate_rate])
    text = models.TextField(max_length=100)
    target = models.ForeignKey(
        Toilet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False,)
