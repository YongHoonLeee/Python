import csv
# exel file 쓰기
with open('test.csv','w',newline="") as csv_file:
    fieldnames = ['Name','Count']
    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name':'yonghoon','Count':'100'})
    writer.writerow({'Name':'ggong','Count':'200'})

# file 읽기
with open('test.csv','r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'],row['Count'])


