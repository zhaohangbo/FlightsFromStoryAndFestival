from rest_framework import serializers
from stories.models import Story
from stories.models import Place
from stories.models import Customer


# class Story(models.Model):
#     title        = models.CharField(max_length=100, blank=False)
#     lastEditTime = models.DateTimeField(auto_now_add=True)
#     liked        = models.IntegerField()
#     generateFlightTimes    = models.IntegerField()
#     class Meta:
#         unique_together = ('title','lastEditTime')
#         ordering = ('lastEditTime','title',)
#
# class Customer(models.Model):
#     story = models.ForeignKey(Story, related_name='customer')
#     registeredTime = models.DateTimeField(auto_now_add=True)
#     username = models.CharField(max_length=100, blank=False)
#     pwd  = models.CharField(max_length=100, blank=False)
#     email = models.EmailField(max_length=254, blank=True)
#     token = models.CharField(max_length=100, blank=False)
#     class Meta:
#         # unique_together = ('username','email')
#         ordering = ('username',)
#
# class Places(models.Model):
#     story = models.ForeignKey(Story, related_name='places')
#     placeName = models.CharField(max_length=100, blank=False)
#     timeVisited= models.DateTimeField(auto_now_add=False)
#     timeLeft   = models.DateTimeField(auto_now_add=False)
#     class Meta:
#         # unique_together = ('placeName')
#         ordering = ('placeName',)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('registeredTime','username','pwd','email','token')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('placeName','timeVisited','timeLeft')

class StorySerializer(serializers.ModelSerializer):
    customer =Customer()
    places   =Place()
    class Meta:
        model = Story
        fields = ('title','lastEditTime','liked','generateFlightTimes','customer','places')
    #For Post
    def create(self, validated_data):
        customer_data   = validated_data.pop('customer')
        places_data = validated_data.pop('places')
        story = Story.objects.create(**validated_data)

        Customer.objects.create(story=story, **customer_data)
        for place_data in places_data:
            Place.objects.create(story=story, **places_data)
        return story

    #For Put
    def update(self, instance , validated_data):
        pass