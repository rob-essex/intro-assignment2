# Rob Mennell - UoE Launching into Comp Sci Nov 2021 - Assignment 2

master_list = [] # creates a directory
company_count = 1 #historical count of companies input into the master list, used for unique Company ID


def run_app():
  """runs the application under a while loop until user exits"""
  
  while True: 
    selection = main_menu() #matches user input to desired function
    if selection.lower() == "search":
      search_company()
    elif selection.lower() == "sort":
      sort_companies()
    elif selection.lower() == "add":
      add_company()
    elif selection.lower() == "update":
      update_company()
    elif selection.lower() == "delete":
      delete_company()
    elif selection.lower() == "exit":
      print("\nSession Closed. Thank you.\n")
      break
    else:
      print("\n\nInvalid entry - please try again\n")
      main_menu()


def main_menu():
  """prompts user for action"""
  
  menu_select = input("""Welcome to Company Directory 1.0
  Select your action below:
  To SEARCH for a company, type SEARCH
  To SORT and LIST stored companies, type SORT
  To ADD a new company, type ADD
  To UPDATE a company, type UPDATE
  To DELETE a company, type DELETE
  To EXIT the application, type EXIT
  
  >:""")
  
  return menu_select


def search_company():
  """returns the index of the target company dictionary"""
  
  search_index = ""
  search_name = input("Type desired Company Name: ")
  for company in master_list: #searches across the company dictionaries
    if company['Company Name'].lower() == search_name.lower():
      search_index = master_list.index(company)
      for c in company: #display key/value pairs for found company
        print(c,": ",company[c])
      return search_index
          
  if search_index == "": #indicate if no match, return to main menu
    print("\n\nCompany not found.\n")


def sort_companies():
  """prints all companies in master_list according to user sort criteria"""
  
  sort_type = input("""How would you like to sort and list the directory?
  
  To sort alphabetically by COMPANY NAME, type COMPANY
  To sort alphabetically by POC NAME, type POC
  To sort according to highest Estimated REVENUE, type REVENUE
  
  >:""")
  if sort_type.lower() == "company": #sort ascending by company
    for company in sorted(master_list, key = lambda company: company["Company Name"]):
      for c in company:
        print(c,": ", company[c]) #prints key/value pairs for each company
      print("\n--------\n") #spacer
  elif sort_type.lower() == "poc": #sort ascending by POC
    sorted(master_list, key = lambda company: company["POC Name"])
    for company in sorted(master_list, key = lambda company: company["POC Name"]):
      for c in company:
        print(c,": ", company[c])
      print("\n--------\n")
  elif sort_type.lower() == "revenue": #sort descending by revenue
    for company in sorted(master_list, key = lambda company: company["Est Annual Revenue"], reverse=True):
      for c in company:
        print(c,": ", company[c])
      print("\n--------\n")
  else: #if invalid input received
    print("Please try again.")
    sort_company()


def add_company():
  """appends new company information to master_list"""
  
  new_company = input_company_info("") #passes null argument to indicate that this is a new company
  master_list.append(new_company) #appends new company dict to master_list
  
  print("\n\nNew company saved to directory:\n")

  for c in new_company: #prints confirmation company information
    print(c,": ",new_company[c])


def update_company():
  """updates an existing company record"""
  
  update_index = search_company() #assigns search result index for update
  if update_index is None: #return to main menu if no result found
    print("\n\nReturning to menu.\n")
      
  else:
    update_yn = input("\n\nWould you like to update this company? Y/N:  ") #prompt to update company
    
    if update_yn.lower() == "y":
      update_dict = input_company_info(update_index) #collect new information for selected company
      master_list[update_index] = update_dict #replace existing company dict with updated dict
      print("\n\nRecord successfully updated to: ")
      for c in update_dict:
        print(c,": ",update_dict[c])
          
    else:
      print("Returning to main menu.")


def input_company_info(comp_id):
  """helper function that collects user input for company information, returns dict"""
  
  global company_count #global value maintains count of all companies ever added
  
  if comp_id == "": #detects if this is a new company without existing ID
    Company_ID = company_count #assigns unique ID to company - not editable by user
    company_count += 1
  else:
    Company_ID = master_list[comp_id]["Company ID"] #if existing company, keeps same ID
  
  ## begin prompting user for company information
  Company_Name = input("Type Company Name: ") 
  while True: #loop to handle ValueError
    try:
      DUNS_Number = int(input("Type Company DUNS Number: "))
      break
    except ValueError:
      print("Please enter a valid DUNS Number.")
  POC_Name = input("Type Main Contact Name: ")
  POC_Phone = input("Type Main Contact Phone Number: ")
  POC_Email = input("Type Main Contact Email: ")
  while True: #loop to handle ValueError
    try:
      Est_Annual_Revenue = float(input("Type estimated Annual Revenue in USD: "))
      break
    except ValueError:
      print("Please enter a valid number for estimated Annual Revenue in USD:" )
  
  ## assemble all user input data into a dictionary
  company_dict = {"Company ID":Company_ID,"Company Name":Company_Name,"DUNS Number":DUNS_Number,"POC Name":POC_Name,"POC Phone":POC_Phone,"POC Email":POC_Email,"Est Annual Revenue":Est_Annual_Revenue}
  
  return company_dict #return company dictionary


def delete_company():
  """deletes company dictionary from master_list"""
  
  del_index = search_company() 
  if del_index is None: #if no company found, returns to main menu
    print("Returning to main menu.\n")
  else:
    delete_yn = input("Do you want to delete this company? Y/N:  ")
    if delete_yn.lower() == "y":
      del master_list[del_index]
      print("Record deleted.")
    else:
      print("Returning to main menu.")

run_app()