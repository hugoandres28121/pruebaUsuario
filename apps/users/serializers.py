from rest_framework import serializers
from apps.users.models import Usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'Nombre de Usuario':instance['username'],
            'Clave':instance['password'],
            'ID Documento Identidad':instance['documento'],
            'Correo Electronico':instance['email'],
            'Nombres':instance['nombres'],
            'Apellidos':instance['apellidos']


        }
