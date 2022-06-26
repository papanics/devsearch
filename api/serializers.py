from rest_framework import serializers
from dev_apps.models import Project, Tag, Review
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False) #connect the owner to the project --> nested relationships, one to one rfield many = False
    tags = TagSerializer(many=True) # many to many rfield many=True
    reviews = serializers.SerializerMethodField() # add attribute into this JSON object using a method field.

    class Meta:
        model = Project
        fields = '__all__'

    def get_reviews(self, obj): #it has to start with get_ if we have to create a serializer method field.
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data