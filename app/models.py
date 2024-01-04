from django.db import models

# Create your models here.
class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100,unique=True)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return str(self.deptno)
    
class Employee(models.Model):
    deptno=models.ForeignKey(Department,on_delete=models.CASCADE)
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    

    def __str__(self):
        return self.ename
    
class Salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.IntegerField()
    hisal=models.IntegerField()

    def __str__(self):
        return self.grade
    
class Bonus(models.Model):
    amount=models.IntegerField()

    def __str__(self):
        return self.amount




