from django.db import models

# Create your models here.
class Banks(models.Model):
    ifsc=models.TextField(max_length=20,blank=True, null=True)
    bank_id=models.IntegerField(blank=True, null=True)
    branch	= models.TextField(blank=True, null=True)
    address	=models.TextField(blank=True, null=True)
    city	=models.TextField(default=60,blank=True, null=True)
    district=models.TextField(default=200,blank=True, null=True)
    state	=models.TextField(default=200,blank=True, null=True)
    bank_name =models.TextField(blank=True, null=True)

    class Meta:
        ordering=('bank_name',)
        verbose_name='Bank'
        verbose_name_plural='Banks'

    def __str__(self):
        return "{} - {} - {}".format(self.ifsc,self.city,self.bank_name)

