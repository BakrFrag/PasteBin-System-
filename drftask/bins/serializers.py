from rest_framework import serializers;
from bins.models import Bin;

# used for retrive and display object
class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bin;
        fields=("__all__");
class BinCreateUpdateSerializer(serializers.ModelSerializer):
    """
    used to create update delete bins
    """
    class Meta:
        model=Bin;
        exclude=('author',);
    
    def validate(self,data):
        """
        validate data to allow user to share bins to public or private or share with some other 

        """
        public=data['public']
        private=data['private']
        shared=data['shared_with'];
        # check public only checked
        public_condition=(public==True and private==False and shared==[]);
        # check private only checked
        private_condition=(private==True and public==False and shared==[]);
        # check shared with only selected
        shared_condition=(bool(shared)==True and public==False and private==False);
        if public_condition or private_condition or shared_condition:
            return data;
        raise serializers.ValidationError("only on field of public or private or shared with can selected one and only one")


