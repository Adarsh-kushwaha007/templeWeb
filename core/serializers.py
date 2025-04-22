from rest_framework import serializers
# from .models import Location ,Transportation,Feedback
from .models import Feedback


# class Locationserializer(serializers.ModelSerializer):
#     class meta:
#         model = Location
#         fields = ['id','address','latitude','longitude']


# class transportationserializer(serializers.ModelSerializer):
#     class meta:
#         model = Transportation
#         fields = ['id','origin','destination','transportation_medium']
        

class Feedbackserializer(serializers.ModelSerializer):
    class mete:
        model = Feedback
        fields = ['id','content',['content_at']]