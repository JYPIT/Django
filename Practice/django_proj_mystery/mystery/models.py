from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ufo(TimestampedModel):
    case = models.CharField(max_length=30, db_index=True, verbose_name="사건명")
    photo = models.ImageField(verbose_name="사진")
    time = models.CharField(max_length=10, db_index=True, verbose_name="사건 시간")
    area = models.CharField(max_length=30, db_index=True, verbose_name="지역")
    desc = models.TextField(verbose_name="설명")

    class Meta:
        verbose_name = "UFO"
        verbose_name_plural = "UFO"


class Creature(TimestampedModel):
    case = models.CharField(max_length=30, db_index=True, verbose_name="사건명")
    photo = models.ImageField(verbose_name="사진")
    time = models.CharField(max_length=10, db_index=True, verbose_name="사건 시간")
    area = models.CharField(max_length=30, db_index=True, verbose_name="지역")
    desc = models.TextField(verbose_name="설명")

    class Meta:
        verbose_name = "Crature"
        verbose_name_plural = "Creature"


class Timetravel(TimestampedModel):
    case = models.CharField(max_length=30, db_index=True, verbose_name="사건명")
    photo = models.ImageField(verbose_name="사진")
    time = models.CharField(max_length=10, db_index=True, verbose_name="사건 시간")
    area = models.CharField(max_length=30, db_index=True, verbose_name="지역")
    desc = models.TextField(verbose_name="설명")

    class Meta:
        verbose_name = "Time Travle"
        verbose_name_plural = "Time Travel"


class Video(TimestampedModel):
    ufo_case = models.ForeignKey(Ufo, on_delete=models.CASCADE)
    creature_case = models.ForeignKey(Creature, on_delete=models.CASCADE)
    Timretravel_case = models.ForeignKey(Timetravel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    youtube_url = models.URLField()

    class Meta:
        verbose_name = "비디오"
        verbose_name_plural = "비디오 목록"


class Review(TimestampedModel):
    ufo_case = models.ForeignKey(Ufo, on_delete=models.CASCADE)
    creature_case = models.ForeignKey(Creature, on_delete=models.CASCADE)
    Timretravel_case = models.ForeignKey(Timetravel, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰 목록"
