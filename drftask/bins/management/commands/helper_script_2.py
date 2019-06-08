from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from bins.models import Bin;
from django.db.models import Count 
import csv;  
class Command(BaseCommand):
    """
    return bin and number of user this bin shared with them
    """
    help = 'return bin and number of user this bin shared with them'

    def handle(self, *args, **kwargs):
        bins_within = Bin.objects.annotate(Total_Share = Count('shared_with'));
        with open('number_of_shared_for_bins.csv', mode='w') as csv_file:
            fieldnames = ['Bin',"Number Of Shared"];
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader() 
            for i in bins_within:
                  writer.writerow({
                      "Bin":i.title,"Number Of Shared":i.Total_Share});
                  self.stdout.write("Bin %s Shared %s"%(i.title,i.Total_Share));