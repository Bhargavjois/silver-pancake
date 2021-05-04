"""Created by Bhargav. 
   Created on May 4 2021.
   Created just test python skill.
   Python skill: Just a beginner.
"""




#Importing some modules used in the code.
import csv
import os




# To create the csv file to store contact details.
try:
    f = open("contacts.csv")
except FileNotFoundError:
    with open('contacts.csv', 'w') as csv_file:
        fieldnames = ['name', 'number']
        writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()
        
        


#Some styling.
def decor_draw_title(func):
    def wrap():
        print("\n=====================================")
        func()
        print("=====================================\n")
    return wrap
     
      
 
 
#Part of styling.
@decor_draw_title
def print_choices():
  print("\n1.Add Contact\n2.Delete Contact\n3.Search Contact\n4.Display All Contacts\n5.Exit\n")


    
    
    
#To insert the contact details in the created csv file.      
def insert_info():
   found_name=0
   name=input("Enter the name to add: ")
   with open("contacts.csv",newline="") as f:
     readed=csv.reader(f)
     for fname in readed:
        if fname[0]==name: 
          found_name=1
   if found_name==1:
      print('X-  ',name,"Already exist  -X")
   else:
     number=int(input("Enter the Number to add: "))    
     with open('contacts.csv', mode='a') as csv_file:
        fieldnames = ['name', 'number']
        writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writerow({'name': name, 'number': number})
        print('√- ',name,'Added successfully  -√')
     
      
      
      
#To delete the selected contact from csv file.     
def delete_info():
    found_item=0
    contactlist=[]
    with open("contacts.csv",newline="") as f:
      reader=csv.reader(f)
      username=input("Name of contact: ")
      
      for row in reader: 
            
                if row[0].lower()!=username.lower(): 
                    contactlist.append(row)
                else:
                    found_item=1
      with open("contacts.csv","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(contactlist)
        if found_item==1:
           print('√-  ',username,'Deleted successfully  -√')   
        else:
           print("X- Contact not found -X")
        
        
        
        
#To display all the contact details in the csv file.        
def display_contacts():
  with open("contacts.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    filesize = os.path.getsize("contacts.csv")
    if filesize<14:
      print("X-  No Contacts  -X")
    else:
      print('\n')
      print("Name        :    Number\n")
      for row in csv_file:
        contact_details=dict(row)
        lnth=10-len(contact_details['name'])
        print(contact_details['name'],lnth*' ',':  ',contact_details['number'])

        
        
        
#To search a specific contact from csv file.       
def search_contacts():
  found=0
  search_name=input('Search Contact with name: ')
  with open("contacts.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
      contact_details=dict(row)
      if contact_details['name'].lower()==search_name.lower():
        found+=1
        print("\nName       ",':','  Number\n')
        print(contact_details['name'],(10-len(contact_details['name']))*' ',':  ',contact_details['number'],'\n')
    if found==0:
      print("*SEARCH FAILED*\nContact doesn't exist")
        
        
        
        
#The main function, where you chose what to do.        
while(1):
  print_choices()
  choice=int(input("Enter your Choice: "))
  if choice == 1: insert_info()
  elif choice == 2: delete_info()
  elif choice == 3: search_contacts()
  elif choice == 4: display_contacts()
  else: exit()
  
  
  
  
  #Thank you for checking this out. Please give your opinion about this. Rate it out of 10.