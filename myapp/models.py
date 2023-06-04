from django.db import models

# Create your models here.
class Loanlist(models.Model):
    l_no = models.AutoField(primary_key=True)
    l_book_no = models.IntegerField()
    l_m_id = models.CharField(max_length=50)
    l_regdate = models.DateTimeField(blank=True, null=True)
    l_returndate = models.DateTimeField(blank=True, null=True)
    l_status = models.IntegerField(blank=True, null=True)
    l_deley = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loanlist'