from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Module(models.Model):
    name = models.CharField(max_length=50)
    

    
# Creating the Permission model.
class Permission(models.Model):
    name = models.CharField(max_length=50)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    
    
    
# Creating the Role model
class Role(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField(Permission)

  


# Creating the RoleModel
# Linking roles and permissions using the UserRole model.
class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)