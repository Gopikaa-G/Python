import csv
field_name=['No','company','Car Model']
car=[
    {'No':1,'company':'Ferrari','Car Model':'GH'},
    {'No':2,'company':'BMW','Car Model':'x5'},
    {'No':3,'company':'Maruti suzuki','Car Model':'swift'},
    {'No':4,'company':'Audi','Car Model':'RS7'},
    {'No':5,'company':'Toyota','Car Model':'Fortuner'}
]
with open('car.csv','w',newline='')as csvfile:
    write=csv.DictWriter(csvfile,fieldnames=field_name)
    write.writeheader()
    write.writerows(car)
with open('car.csv',newline='')as csvfile:
    d=csv.reader(csvfile)
    for r in d:
        print(','.join(r))