from django.db import models

class Review(models.Model): # Review 모델 작성하기
    title = models.CharField(max_length=200)
    rating = models.FloatField()
    review = models.TextField()
    date_watched = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True) # 초기 생성 시 자동 저장
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=6)
    poster = models.ImageField(blank=True, upload_to='poster_images/') # 앞에는 기본적으로 media가 들어감(MEDIA_URL)

    def __str__(self):
        return self.title