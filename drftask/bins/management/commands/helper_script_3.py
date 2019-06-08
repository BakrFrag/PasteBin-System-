from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from bins.models import Bin;
from django.db.models import Count
import csv;

class Command(BaseCommand):
    """
    return number of each status of bin \
    number of public/shared/private/bins
    """
    help = 'return number of each status of bin \
    number of public/shared/private/bins';
    def handle(self, *args, **kwargs):
        private_bins=Bin.objects.filter(private=True).count();
        public_bins=Bin.objects.filter(public=True).count();
        shared_bins=Bin.objects.filter(shared_with=True).count();
        with open('number_of_public_and_private.csv', mode='w') as csv_file:
            fieldnames = ['Number Of Public Bins',
            "Number Of Shared Bins",
            'Number Of Private Bins'];
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader() 
            writer.writerow({
            "Number Of Public Bins" : public_bins,"Number Of Private Bins" : private_bins,
            "Number Of Shared Bins":shared_bins
            });
        self.stdout.write("private bins : %s"%private_bins);
        self.stdout.write("public bins : %s"%public_bins);
        self.stdout.write("shared bins : %s"%shared_bins);