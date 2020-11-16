import pandas as pd
import numpy as np

#to choose from which columns change here
cols = [2, 3, 4]

#to read from specific sheet change the second arg
df = pd.read_excel('data.xlsx', 'Localization-1', usecols=cols)

default = 0
list1 = list()
list2 = list()
newdf = pd.DataFrame(columns=["distance", "4G", "5G"])

for index, row in df.iloc[1:].iterrows():
    print(row[0], row[1], row[2])


    if default!=row[0]:
    	print("first iter")
    	if len(list1)==0 and len(list2)==0:
    		print("first first round")
    		default=row[0]
    		list1.append(row[1])
    		list2.append(row[2])
    	
    	else:

    		median1 = np.median(np.asarray(list1, dtype=np.float32))
    		median2 = np.median(np.asarray(list2, dtype=np.float32))
    		print(median1)
    		print(median2)
    		new_row = pd.Series(data={'distance':default, '4G':median1, '5G':median2})
    		newdf = newdf.append(new_row, ignore_index=True)
    		print(newdf)
    		default=row[0]
    		list1.clear()
    		list2.clear()

    else:
    	list1.append(row[1])
    	list2.append(row[2])


median1 = np.median(np.asarray(list1, dtype=np.float32))
median2 = np.median(np.asarray(list2, dtype=np.float32))
print(median1)
print(median2)
new_row = pd.Series(data={'distance':default, '4G':median1, '5G':median2})
newdf = newdf.append(new_row, ignore_index=True)



print(newdf)

#write to excel
newdf.to_excel('Localization-1.xlsx', sheet_name='medians', index=False)

