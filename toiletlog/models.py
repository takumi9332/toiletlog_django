from django.db import models


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


class Clean(models.IntegerChoices):
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

    prefecture = models.IntegerField(
        choices=Prefecture.choices,
        default=0,
    )

    city = models.CharField(
        blank=False,
        null=False,
        max_length=255,
    )

    address = models.CharField(
        blank=False,
        null=False,
        max_length=255,
    )

    building = models.CharField(
        blank=True,
        max_length=255,
    )

    sex = models.IntegerField(
        choices=Sex.choices,
        default=0,
    )

    type = models.IntegerField(
        choices=Type.choices,
        default=0,
    )

    washlet = models.IntegerField(
        choices=Washlet.choices,
        default=0,
    )

    clean = models.IntegerField(
        choices=Clean.choices,
        default=0,
    )

    info = models.TextField(
        blank=True,
        max_length=1000,
    )

    def __str__(self):
        return self.updated
