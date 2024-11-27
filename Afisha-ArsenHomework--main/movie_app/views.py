from django.shortcuts import render
from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, ReviewValiditySerializer, MovieValiditySerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class DirectorListAPIView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
 


class DirectorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        validator = MovieValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        title = validator.validated_data.get('title')
        description = validator.validated_data.get('description')
        duration = validator.validated_data.get('duration')
        director = validator.validated_data.get('director')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director=director)
        movie.save()
        return Response(MovieSerializer(movie).data, status=status.HTTP_201_CREATED)



class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        product_detail = self.get_object()
        validator = MovieValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        product_detail.title = validator.validated_data.get('title')
        product_detail.description = validator.validated_data.get('description')
        product_detail.duration = validator.validated_data.get('duration')
        product_detail.director = validator.validated_data.get('director')
        product_detail.save()
        return Response(MovieSerializer(product_detail).data, status=status.HTTP_200_OK)
        


class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request, *args, **kwargs):
        validator = ReviewValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        text = validator.validated_data.get('text')
        movie = validator.validated_data.get('movie')
        stars = validator.validated_data.get('stars')
        review = Review.objects.create(text=text, movie=movie, stars=stars)
        review.save()
        return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        review_detail = self.get_object()
        validator = ReviewValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(validator.errors, status=status.HTTP_400_BAD_REQUEST)
        review_detail.text = validator.validated_data.get('text')
        review_detail.movie = validator.validated_data.get('movie')
        review_detail.stars = validator.validated_data.get('stars')
        review_detail.save()
        return Response(ReviewSerializer(review_detail).data, status=status.HTTP_200_OK)
