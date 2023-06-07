import csv

with open('D:\shixun\\xiangmu\\fyx_chinamoney.csv','r') as f:
    reader = csv.reader(f)
    data  = list(reader)

my_list = [int(row[0]) for row in data]
batch_size = 80
for i in range(0 , len(my_list),batch_size):
    batch = my_list[i:i+batch_size]
    print(batch)