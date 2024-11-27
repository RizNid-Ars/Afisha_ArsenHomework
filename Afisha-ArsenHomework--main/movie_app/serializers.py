from .models import Movie, Director, Review
from rest_framework import serializers

class DirectorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ("id", "name", "movie_count")


    def get_movie_count(self, director):
        return director.movies.count()
    




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "text", "movie", "stars")


class ReviewValiditySerializer(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    stars = serializers.IntegerField(min_value=1, max_value=5)


    
class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    director = DirectorSerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "director", "reviews", "average_rating")

    def get_average_rating(self, movie):
        reviews = movie.reviews.all()
        if reviews:
            sum_reviews = sum([review.stars for review in reviews])
            average = sum_reviews / len(reviews)
            return average
        return None
    

class MovieValiditySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField(min_value=60)
    director = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all())



