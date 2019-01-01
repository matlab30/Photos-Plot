import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os.path, time
import getpass
import exifread
from PIL import Image

Cuser = getpass.getuser()  
directory = "C:\\Users\\"+Cuser+"\\Pictures"        
       
values = []
#Recursive looking for files
for root, directories, filenames in os.walk(directory):
    for file in filenames: 
        if file.lower().endswith(('.png', '.jpg', '.jpeg')): 
                
            with open(root+"/"+file, 'rb') as f:
                tags = exifread.process_file(f, details=False)   
            #Check image date taken    
            if "EXIF DateTimeOriginal" in tags.keys():
                DateTimeOriginal = tags["EXIF DateTimeOriginal"]
                x = DateTimeOriginal.values
                x = ''.join(x.split())
                if x != '':
                    xx = x[:4]
                    values.append(int(xx))
            #Check image date modified
            else:
                x = time.ctime(os.path.getmtime(root+"/"+file))
                xx = x[-4:]
                values.append(int(xx))
                      
def countX(lst, x): 
    return lst.count(x) 

print("Total Number of Photos:")
print(len(values))

#Font
font = {'size': 16}
plt.rc('font', **font)

plt.figure(figsize=(18,10))
plt.title('Photo per Year from My Photo Collection')
plt.xlabel('Year Taken')
plt.ylabel('Number of Photos')
plt.axis()

#determine x axis values
plt.xticks(np.arange(min(values), max(values)+1, 5.0))
xrange = np.arange(min(values), max(values)+1)
xrr = [xrange[0],xrange[-1]]
if xrange[-1] > xrange[0]:
    bins=(xrange[-1]-xrange[0])*2
else:
    bins=50
    
#Grid
plt.grid(True,color='lightgrey')
N, bins, patches = plt.hist(values,edgecolor='black',bins=bins,align='left' , alpha=0.75,range=(xrr))

plt.show()