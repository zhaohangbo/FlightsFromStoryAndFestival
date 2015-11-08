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
    # username=serializers.CharField(source='customer.username')
    class Meta:
        model = Customer
        fields = ('registeredTime','username','pwd','email','token')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('placeName','timeVisited','timeLeft')

class StorySerializer(serializers.ModelSerializer):
    # rules   = AlertRuleSerializer(many=True,read_only=False)
    customers =CustomerSerializer(many=True)
    places   =PlaceSerializer(many=True)
    class Meta:
        model = Story
        fields = ('title','token','lastEditTime','liked','generateFlightTimes','customers','places')
    #For Post
    def create(self, validated_data):
        customers_data   = validated_data.pop('customers')
        places_data = validated_data.pop('places')
        story = Story.objects.create(**validated_data)
        for customer_data in customers_data:
            Customer.objects.create(story=story, **customer_data)
        for place_data in places_data:
            Place.objects.create(story=story, **place_data)
        return story

    #For Put
    def update(self, instance , validated_data):
        pass