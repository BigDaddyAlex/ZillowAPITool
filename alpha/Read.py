import csv
from .PropertyObject import Property
import os
from django.core.files.storage import FileSystemStorage,default_storage

class APIconnection:
    def __init__(self,df):
        self.LsProperties=[]
        self.df=df

    def readfile(self):
        for index, row in self.df.iterrows():
            
            if row[0] is not None and row[1] is not None and row[2] is not None:
                tempProperty=Property(row[0],row[1],row[2])
                tempProperty.findValues()
                self.LsProperties.append(tempProperty)
            

    def writefile(self):
        currdir=os.getcwd()
        with open(os.path.join(currdir,'output.csv'), 'w', newline='') as csvfile:
            propertywriter = csv.writer(csvfile, delimiter=',')
            propertyheader=Property()
            propertywriter.writerow([key.capitalize() for key in propertyheader.info])    
            for property in self.LsProperties:
                print(property.info['Street Addr'])
                propertywriter.writerow([value for value in property.info.values()])

    def connect(self):
        self.readfile()
        self.writefile()

