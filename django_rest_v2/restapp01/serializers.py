from rest_framework import serializers
from .models import *



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =['name' , 'age', 'phone']

        # exclude => To remove fields
        # fields = '__all__'

    def validate(self, data):
        
        if data['age'] < 18:
            raise serializers.ValidationError({'error':'Age must be greater than 18'})

        return data



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'