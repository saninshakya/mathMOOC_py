from django.db import models
from django.contrib.auth.models import User

class StudentParent(models.Model):
	id = models.AutoField(primary_key=True, unique=True)
	student = models.ForeignKey(User, related_name='student')
	parent = models.ForeignKey(User, related_name='parent')	 
	class Meta:
		db_table = 'tbl_student_parent'