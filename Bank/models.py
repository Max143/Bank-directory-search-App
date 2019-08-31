from django.db import models
# import csv


class Branches(models.Model):
    
    ifsc       = models.CharField(max_length=1009)
    bank_id    = models.IntegerField()
    branch     = models.CharField(max_length=1009)
    address    = models.CharField(max_length=1500)
    city       = models.CharField(max_length=1999)
    district   = models.CharField(max_length=1999)
    state      = models.CharField(max_length=1000)
    bank_name  = models.CharField(max_length=1000)


    def __str__(self):
        return self.branch



# No. Longer Required. Used to upload csv content to postgres table via Django Model.
# data = csv.DictReader(open("C:/Users/Desktop/indian_banks/bank_branches.csv"))
# for row in data:
#     Branches.objects.create(ifsc=row['ifsc'], bank_id=row['bank_id'], branch=row['branch'], address=row['address'], city=row['city'], district=row['district'], state=row['state'], bank_name=row['bank_name'])
