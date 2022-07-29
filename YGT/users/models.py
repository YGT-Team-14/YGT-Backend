from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self,  user_id, school, password,  student_id, major ):
        user = self.model(
          
            user_id = user_id,
            school = school,
            major = major,
            student_id = student_id,
 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self , user_id, school, password, student_id=None,  major =None ):
        user = self.create_user( user_id, school, password,  student_id, major)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    
class User(AbstractBaseUser, PermissionsMixin):
    
    objects = UserManager()
    
    user_id = models.CharField(max_length=17, verbose_name="아이디", unique=True) 
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    school = models.CharField( max_length=24, verbose_name="학교", null=True)
    student_id = models.IntegerField(verbose_name="학번", null=True)
    major = models.CharField( max_length=24, verbose_name="학과", null=True) 

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
  
    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "회원목록"
        verbose_name = "사용자" 