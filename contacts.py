import csv
import os





filesize = os.path.getsize("contacts.csv")
if filesize == 0:      
      with open('contacts.csv', mode='w') as csv_file:
        fieldnames = ['name', 'number']
        writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()
      
      
      
def decor_win(func):
    def wrap():
        print("\n*************************************")
        func()
        print("*************************************\n")
    return wrap      
      
      
      
      
      
def decor_lose(func):
    def wrap():
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
        func()
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    return wrap





def decor_draw_title(func):
    def wrap():
        print("\n=====================================")
        func()
        print("=====================================\n")
    return wrap
      
      
      
      
      
@decor_win
def print_added():
  print("Contact added successfully\n")
      
      
 
 
 
@decor_draw_title
def print_choices():
  print("\n1.Add Contact\n2.Delete Contact\n3.Search Contact\n4.Display All Contacts\n5.Exit\n")





@decor_lose
def print_deleted():
    print("Contact Deleted successfully\n")      
    
    
    
      
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
        print_added()
     
      
      
      
      
def delete_info():
    found_item=0
    contactlist=[]
    with open("contacts.csv",newline="") as f:
      reader=csv.reader(f)
      username=input("Name of contact: ")
      
      for row in reader: 
            
                if row[0]!=username: 
                    contactlist.append(row)
                else:
                    found_item=1
      with open("contacts.csv","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(contactlist)
        if found_item==1:
           print_deleted()
        else:
           print("X- Contact not found -X")
        
        
        
        
        
def display_contacts():
  with open("contacts.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    print('\n')
    print("Name        :    Number\n")
    for row in csv_file:
      contact_details=dict(row)
      lnth=10-len(contact_details['name'])
      print(contact_details['name'],lnth*' ',':  ',contact_details['number'])

        
        
        
        
def search_contacts():
  found=0
  search_name=input('Search Contact with name: ')
  with open("contacts.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
      contact_details=dict(row)
      if contact_details['name'].lower()==search_name.lower():
        print(contact_details['name'],' : ',contact_details['number'],'\n')
        found+=1
    if found==0:
      print("*SEARCH FAILED*\nContact doesn't exist")
        
        
        
        
        
while(1):
  print_choices()
  choice=int(input("Enter your Choice: "))
  if choice == 1: insert_info()
  elif choice == 2: delete_info()
  elif choice == 3: search_contacts()
  elif choice == 4: display_contacts()
  else: exit()