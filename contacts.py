import csv
      
      
      
      
      
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





def decor_add(func):
    def wrap():
        print("\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
        func()
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n")
    return wrap





def decor_del(func):
    def wrap():
        print("\nddddddddddddddddddddddddddddddddddddd\n")
        func()
        print("ddddddddddddddddddddddddddddddddddddd\n")
    return wrap
      
      
      
      
      
def decor_ser(func):
    def wrap():
        print("\nsssssssssssssssssssssssssssssssssssss\n")
        func()
        print("sssssssssssssssssssssssssssssssssssss\n")
    return wrap      
 
 
 
 
 
def decor_dis(func):
    def wrap():
        print("\nccccccccccccccccccccccccccccccccccccc\n")
        func()
        print("ccccccccccccccccccccccccccccccccccccc\n")
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
  print("\n1.Add Contact\n2.Delete Contact\n3.Search Contact\n4.Display All Conatacts\n5.Exit\n")





@decor_lose
def print_deleted():
    print("Contact Deleted successfully\n")      
    
    
    
      
@decor_add
def insert_info():
   name=input("Enter the name to add: ")
   number=int(input("Enter the Number to add: "))    
   with open('contacts.csv', mode='a') as csv_file:
      fieldnames = ['name', 'number']
      writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
      writer.writerow({'name': name, 'number': number})
      print_added()
      
      
      
      
      
@decor_del      
def delete_info():
    contactlist=[]
    with open("contacts.csv",newline="") as f:
      reader=csv.reader(f)
      username=input("Name of contact: ")
      
      for row in reader: 
            
                if row[0]!=username: 
                    contactlist.append(row) 
      with open("contacts.csv","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(contactlist)
        print_deleted()
        
        
        
        
        
@decor_dis       
def display_contacts():
  with open("contacts.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
      contact_details=dict(row)
      print(contact_details['name'],' : ',contact_details['number'])

        
        
        
        
@decor_ser        
def search_contacts():
  found=0
  search_name=input('Search Contact with name: ')
  with open("contacts.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
      contact_details=dict(row)
      if contact_details['name']==search_name:
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