from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from bins.models import Bin;
import csv;
from django.db.models import Count   
class Command(BaseCommand):
    """
    return user and number of pastes  created by that user
    """
    help = 'return user and number of pastes  created by that user'

    def handle(self, *args, **kwargs):
        user_bins = User.objects.annotate(Total_Bins = Count('bin'));
        with open('number_of_bins_for_users.csv', mode='w') as csv_file:
            fieldnames = ['User',"Number Of Bins"];
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader() 
            for i in user_bins:
                self.stdout.write("user %s bins %s"%(i.username,i.Total_Bins));
                writer.writerow({"User":i.username,"Number Of Bins":i.Total_Bins});