
Name=input('Enter your name: ')
Class=input('Enter Class Name: ')
Students_Number=int(input("Enter number of Students in class: "))


    
English=int(input('Enter English Marks: '))
Maths=int(input('Enter Maths Marks: '))
Kiswahili=int(input('Enter  Kiswahili Marks: '))
Science=int(input('Enter Science Marks: '))
Social_Studies_CRE=int(input('Enter Social_Studies & CRE Marks: '))


Total=(English+Maths+Kiswahili+Science+Social_Studies_CRE)

Average=Total/5

if Average >= 80:
    print ("Grade A")
elif  Average >=70:
    print('Grade B')
elif Average >= 60:
    print('Grade C')
elif  Average >= 50:
    print('Grade D')
elif Average <= 40:
    print('Grade E')
else:
    print(Name,"Did not sit for the eaxam")

print(Name,"has scored",Total,"and has gotten",Average,"Points")


