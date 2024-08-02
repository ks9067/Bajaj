from rest_framework import serializers

class UserInputSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    college_email = serializers.EmailField()
    college_roll_number = serializers.CharField()
    numbers = serializers.ListField(
        child=serializers.IntegerField()
    )
    alphabets = serializers.ListField(
        child=serializers.CharField(max_length=1)
    )
