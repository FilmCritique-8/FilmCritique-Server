from django.shortcuts import render
from .serializers import ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Review
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ReviewViewset(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# 비밀번호 인증 뷰 함수 작성(FBV : Function Based View)
@api_view(['POST'])
def validate_password(request, pk):
    review = get_object_or_404(Review, pk=pk) # 해당 pk로 Review 객체를 찾고 없으면 404 Not Found

    password = request.data['password'] # requset의 body 중 password를 추출
    if password == review.password: # Review의 field들 중 password와 같으면
        return Response({"password" : True})
    else:
        return Response({"password" : False})