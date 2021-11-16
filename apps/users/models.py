from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager, models.Manager):
#creacion de usuarios, recibe varios parametros, de acuerdo a lo que esta en nuesto modelo users
    def _create_user(self,documento, username, email,nombres,apellidos, password,
     is_staff, is_superuser, **extra_fields):

        if not username:
            raise ValueError('Users must have an username')


        user = self.model(
            documento=documento,
            username=username,
            email = self.normalize_email(email),
            nombres=nombres,
            apellidos=apellidos,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,documento, username, email,nombres,apellidos, password=None, **extra_fields):
        return self._create_user(documento,username, email,nombres,apellidos,password,False, False, **extra_fields)

    def create_superuser(self,documento, username, email,nombres,apellidos, password=None, **extra_fields):
        return self._create_user(documento,username, email,nombres,apellidos, password, True, True, **extra_fields)
    

class Usuario(AbstractBaseUser,PermissionsMixin):
    documento = models.CharField('Numero de Documento',max_length=50,primary_key=True)
    username = models.CharField('Nombre de Usuario',max_length=50,unique=True)
    email = models.EmailField('Correo Electronico', max_length=254,unique=True)
    telefono_celular = models.CharField('Numero de Telefono Celular', max_length=10,blank=True,null=True)
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)

    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN' 
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    
    objects = UserManager()


    #Campo que usara como identificador del usuario
    USERNAME_FIELD = 'username'

    #Campos que requerira para crear el usuario
    REQUIRED_FIELDS = ['documento','email','nombres','apellidos']


    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    def has_perm(self,perm,obj  = None):
        return True

    def has_module_perms(self,app_label):
        return True



# Create your models here.
