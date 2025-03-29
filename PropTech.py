import sys

# Section 1: Personal Particulars Form
def name(): # To gather name
    name_input = input("""What is your name?
Type your response here: """)
    while True:
        if name_input.replace(" ","").isalpha() is True:
            break
        elif name_input.replace(" ","").isalpha() is False:
            print("""
Please enter a valid name.""")
            name_input = input("""
What is your name?
Type your response here: """)
    return name_input.title()

def age(): # To gather age
    while True:
        try:
            age_input = int(input("""
Please enter your age, as of 2023.
Type your response here: """))
            if age_input > 0:
                break
            elif age_input <= 0:
                print("\nPlease enter a valid age.")
        except ValueError:
            print("\nPlease enter a valid age.")
    return age_input

def citizenship(): # To gather Citizenship Status
    citizenship_input = input("""
Please select your citizenship status (1, 2 or 3):
[1] Singaporean
[2] Singapore PR
[3] Non-Singaporean
Type your response here: """)
    while True:
        if citizenship_input == "1":
            citizenship_input = "Singaporean"
            return citizenship_input
        elif citizenship_input == "2":
            citizenship_input = "Singapore PR"
            return citizenship_input
        elif citizenship_input == "3":
            citizenship_input = "Non-Singaporean"
            return citizenship_input
        else:
            citizenship_input = input("""Please enter 1, 2 or 3:
Enter your response here: """)

def marital_status(): # To gather Marital Status
    marital_status_input = input("""
Please select your marital status:
[1] Single
[2] Married
Type your response here: """)
    while True:
        if marital_status_input == "1":
            marital_status_input = "Single"
            return marital_status_input
        elif marital_status_input == "2":
            marital_status_input = "Married"
            return marital_status_input
        else:
            marital_status_input = input("""Please enter 1 or 2:
Enter your response here: """)


# Welcome Menu
menu_input = input("""--- Welcome to PropTech! ---

To begin, enter Y: """).upper()

# If the user enters Y, the program will continue running.

# If the user enters anything other than Y, an error message will loop.
    
while True:
    if menu_input == "Y":
        break
    else:
        menu_input = input("""Please enter Y to begin.
Enter your choice here: """).upper()

# PDPA Declaration

print("""
---PDPA Declaration---
        
By using this tool, you hereby agree that PropTech may collect, use and disclose your personal data that you provide in this Form for the purposes of providing property search results and eligibility for housing grants.
        
If you are providing someone else’s personal data or using PropTech on behalf of someone else, you hereby declare that you have obtained consent from the named individual(s) for the collection, use, and disclosure of his/her personal data by you to PropTech.
            
PropTech respects the privacy of individuals and recognises the importance of the personal data you have entrusted to us and believe that it is our responsibility to properly manage, protect, process and disclose your personal data. We will collect, use and disclose your personal data in accordance with the Personal Data Protection Act 2012.""")
    
PDPA_input = input("""[Y] Yes, I agree.
[N] No, I do not agree.
Please enter Y or N.
Enter your choice: """).upper()

# If the user agrees to the PDPA, the program will continue running.

# If the user does not agree to the PDPA, the program will end.

# If the user enters anything other than Y/N, an error message will loop.

while True:
    if PDPA_input == "Y":
        break
    elif PDPA_input == "N":
        print("""
Thank you for using PropTech. 
We hope to see you next time.""")
        sys.exit()
    else:
        PDPA_input = input("""Please enter Y or N
Enter your choice here: """).upper()


# Personal Particulars Form
# The Personal Particulars Form will gather the user's Name, Age, Citizenship Status, and Marital Status.
print("""
--- Section 1: Personal Particulars Form ---""")  
name_input = name()
age_input = age()
citizenship_input = citizenship()
marital_status_input = marital_status()

# A summary of the personal particulars will be printed for the user's confirmation.

# If the user enters Y, the program will continue running.

# If the user enters N, he/she will be able to select certain fields to amend.

# If the user enters anything other than Y, an error message will loop.

while True:   
    particulars_confirmation = input((f"""\nThank you for your input, {name_input}. Kindly confirm your details:
Name: {name_input}
Age: {age_input}
Citizenship: {citizenship_input}
Marital Status: {marital_status_input}
    
[Y] Yes, the details are correct.
[N] No, I would like to amend some field(s).
Please enter Y or N.
Type your response here: """)).upper()
    
    if particulars_confirmation == "Y":
        break
    elif particulars_confirmation == "N":
        amendment_choice = input("""
Please select the field to amend (1, 2, 3 or 4).
[1] Name
[2] Age
[3] Citizenship
[4] Marital Status
Enter your choice here: """)   
        while True:
            if amendment_choice == "1":
                name_input = name()
                break
            elif amendment_choice == "2":
                age_input = age()
                break
            elif amendment_choice == "3":
                citizenship_input = citizenship()
                break
            elif amendment_choice == "4":
                marital_status_input = marital_status()
                break
            else:
                amendment_choice = input("""Please enter 1, 2, 3 or 4:
Enter your response here: """)
    else:
        print("\nPlease enter Y or N.")
        

# Section 2: Property Search 
# open the new file and read its contents
with open('new-properties.txt', 'r') as f1:
    new_contents = f1.read()

# open the existing file and read its contents
with open('property-listing.txt', 'r') as f2:
    existing_contents = f2.read()
    
# write both into a new file
with open("all-properties.txt", "w") as f3:
    f3.write(existing_contents)
    f3.write(new_contents)

# open and read property-attributes.txt
with open('property-attributes.txt', 'r') as f:
    attrs = [line.strip() for line in f]

# open and read all-properties.txt
with open('all-properties.txt', 'r') as f:
    lines = [line.strip() for line in f]

# create a nested dictionary using the attrs list and the lines list
properties = {}
for i in range(len(lines)):
    if lines[i] == '--------------------':
        continue
    elif "Property" in lines[i]:
        prop_num = lines[i]
        properties[prop_num] = {}
    else:
        key_val = lines[i].split(':')
        key = attrs[int(key_val[0])-1].replace(str(int(key_val[0])) + '.', '')
        val = key_val[1].strip()
        if key in ['floor_size', 'TOP', 'bedrooms', 'bathroom', 'asking_price']:
            val = int(val)
        properties[prop_num][key] = val
        
properties

def filter_properties(properties):
    filtered_properties = properties.copy()
    selected_filters = []
    towns = list(set([prop["town"] for prop in filtered_properties.values()]))
    town_filter_applied = False
    property_types = list(set([prop["property_type"] for prop in filtered_properties.values()]))
    pt_filter_applied = False
    bedrooms = list(set([prop["bedrooms"] for prop in filtered_properties.values()]))
    bedroom_filter_applied = False
    budget_filter_applied = False
    
    while True:
        print("""\nPlease select your filters:
[1] Town/District
[2] Property Type
[3] Bedrooms
[4] Budget
[5] Apply filters and return results
[6] Return to previous page
              """)
        filter_option = input("Enter your choice (1-6): ")

        if filter_option == "1" and not town_filter_applied:
            while True:
                print("\nPlease select the town/district (press Enter if you have no preference): ")
                for i, town in enumerate(towns):
                    print(f"[{i+1}] {town}")
                town_choices = input("\nEnter your choice(s), separated by commas: ")
                try:
                    if town_choices == "":
                        town_choices = ["No preference"]
                    else:
                        town_choices = [towns[int(i)-1] for i in town_choices.split(",")]
                        if len(town_choices) != len(set(town_choices)):
                            print("Duplicate entries are not allowed.")
                            continue
                    selected_filters.append(f"Town/District: {town_choices}")
                    print("Selected filters:", ", ".join(selected_filters))
                    edit_choice = input("Confirm Town/District filters? (Disclaimer: Once confirmed, you will not be able to edit unless you restart the program.)\nEnter [E] to edit or enter any other keys to continue: ")
                    if edit_choice.upper() == "E":
                        selected_filters.pop()
                        continue
                    filtered_properties = {prop_id: prop for prop_id, prop in filtered_properties.items()
                                           if prop["town"] in town_choices or "No preference" in town_choices}
                    
                except (ValueError, IndexError):
                    print("Invalid input. Please enter your choice again.")
                    continue
                break
            town_filter_applied = True
            
        elif filter_option == "2" and not pt_filter_applied:
            while True:
                print("\nPlease select the property type (press Enter if you have no preference): ")
                for i, property_type in enumerate(property_types):
                    print(f"[{i+1}] {property_type}")
                property_choices = input("\nEnter your choice(s), separated by commas: ")
                try:
                    if property_choices == "":
                        property_choices = ["No preference"]
                    else:
                        property_choices = [property_types[int(i)-1] for i in property_choices.split(",")]
                        if len(property_choices) != len(set(property_choices)):
                            print("Duplicate entries are not allowed.")
                            continue
                    selected_filters.append(f"Property Type: {property_choices}")
                    print("Selected filters:", ", ".join(selected_filters))
                    edit_choice = input("Confirm Property Type filters? (Disclaimer: Once confirmed, you will not be able to edit unless you restart the program.)\nEnter [E] to edit or enter any other keys to continue: ")
                    if edit_choice.upper() == "E":
                        selected_filters.pop()
                        continue
                    filtered_properties = {prop_id: prop for prop_id, prop in filtered_properties.items()
                                           if prop["property_type"] in property_choices or "No preference" in property_choices}
                except (ValueError, IndexError):
                    print("Invalid input. Please enter your choice again.") 
                    continue
                break
            pt_filter_applied = True

        elif filter_option == "3" and not bedroom_filter_applied:          
            while True:
                try:
                    print("\nPlease select the number of bedrooms: ")
                    for i, bedroom in enumerate(bedrooms):
                        print(f"[{i+1}] {bedroom}")
                    bedroom_choices = input("\nEnter your choice(s), separated by commas: ").split(",")
                    if len(bedroom_choices) != len(set(bedroom_choices)):
                        print("Duplicate entries are not allowed.")
                        continue
                    elif all(choice.isdigit() and int(choice) in range(1, len(bedrooms) + 1) for choice in bedroom_choices):
                        selected_filters.append(f"No. of Bedrooms: {bedroom_choices}")
                        print("Selected filters:", ", ".join(selected_filters))
                        edit_choice = input("Confirm Bedroom filters? (Disclaimer: Once confirmed, you will not be able to edit unless you restart the program.)\nEnter [E] to edit or enter any other keys to continue: ")
                        if edit_choice.upper() == "E":
                            selected_filters.pop()
                            continue
                        filtered_properties = {prop_id: prop for prop_id, prop in filtered_properties.items()
                                                if str(prop["bedrooms"]) in bedroom_choices}

                    else: 
                        print("Invalid input. Please enter your choice again.")
                        continue
                except (ValueError, IndexError):
                    print("Invalid input. Please enter your choice again.")
                    continue
                break
            bedroom_filter_applied = True
                
        elif filter_option == "4" and not budget_filter_applied:
            while True:
                try:
                    budget = float(input("\nPlease enter your budget (SGD): $"))
                    if budget < 0:
                        print("Budget cannot be negative. Please enter your choice again.")
                        continue
                    selected_filters.append(f"Budget: ${float(budget):,.2f}")
                    print("Selected filters:", ", ".join(selected_filters))
                    edit_choice = input("Confirm Budget filters? (Disclaimer: Once confirmed, you will not be able to edit unless you restart the program.)\nEnter [E] to edit or enter any other keys to continue: ")
                    if edit_choice.upper() == "E":
                        selected_filters.pop()
                        continue
                    filtered_properties = {prop_id: prop for prop_id, prop in filtered_properties.items()
                                           if prop["asking_price"] <= int(budget)}
    
                except (ValueError, IndexError):
                    print("Invalid input. Please enter your choice again.")
                    continue
                break
            budget_filter_applied = True
            
        elif filter_option == "5":
            if len(selected_filters)>0:
                print("Selected filters:", ", ".join(selected_filters))
            else:
                print("Selected filters: NIL")
            break
        
        elif filter_option == "6":
            return properties

        else:
            print("Invalid input. Please enter your choice again.")
            continue
        
    if filtered_properties:
        print("Here are the properties that match your search criteria:")
        print("{:<12} {:<30} {:<20} {:<15} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10}  {:<15}".format(
            "Property", "Address", "Area", "Town", "Postal Code", "Property Type", "Size", "TOP", "Bedrooms", "Bathroom", "Asking Price"))
        print("-" * 170)          
        for i, prop in filtered_properties.items():
            print("{:<12} {:<30} {:<20} {:<15} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10} ${:<15,}".format(i, prop['address'], prop['area'], prop['town'], prop['postal_code'],
            prop['property_type'], prop['floor_size'], prop['TOP'], prop['bedrooms'], prop['bathroom'], prop['asking_price']))
    else:
        print("No properties match your search criteria.")


def search_properties(properties):
    while True:
        print("\n--- Section 2: Property Search ---")

        user_search = input("\nSelect an option:\n[1] View Available Properties\n[2] Filter Properties\n[3] Exit Property Search\n\nEnter your choice (1-3): ")
        if user_search == "1":
            print("\n{:<12} {:<30} {:<20} {:<15} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10} {:<15}".format(
                "Property", "Address", "Area", "Town", "Postal Code", "Property Type", "Size", "TOP", "Bedrooms", "Bathrooms","Asking Price"))
            print("-" * 170)
            for key, value in properties.items():
                print("{:<12} {:<30} {:<20} {:<15} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10} ${:<15,}".format(
                    key, value['address'], value['area'], value['town'], value['postal_code'],
                    value['property_type'], value['floor_size'], value['TOP'], value['bedrooms'], value['bathroom'], value['asking_price']))
        
        elif user_search == "2":
            filter_properties(properties)
        
        elif user_search == "3":
            break
        
        else:
            print("Invalid input. Please try again.")
            continue
        
        
# Section 3: Housing Grants Eligibility
properties_details_dict = {
"Property 1": {
    "Remaining Lease": 86,
    "Flat Type": "4 room"
},
"Property 2": {
    "Remaining Lease": 75,
    "Flat Type": "4 room"
},
"Property 3": {
    "Remaining Lease": 77,
    "Flat Type": "5 room"
},
"Property 4": {
    "Remaining Lease": 56,
    "Flat Type": "3 room"
},
"Property 5": {
    "Remaining Lease": 71,
    "Flat Type": "5 room"
},
"Property 6": {
    "Remaining Lease": 93,
    "Flat Type": "Condominium"
},
"Property 7": {
    "Remaining Lease": 93,
    "Flat Type": "Condominium"
},
"Property 8": {
    "Remaining Lease": 75,
    "Flat Type": "5 room"
},
"Property 9": {
    "Remaining Lease": 54,
    "Flat Type": "3 room"
},
"Property 10": {
    "Remaining Lease": 992,
    "Flat Type": "Condominium"
}}

remaining_lease = 0
flat_type = ""

def grant_property_details():
    while True:
        grant_property_choice = input("\nPlease select a property to check for Grants Eligibility. \n[1] Property 1 \n[2] Property 2 \n[3] Property 3 \n[4] Property 4 \n[5] Property 5 \n[6] Property 6 \n[7] Property 7 \n[8] Property 8 \n[9] Property 9 \n[10] Property 10 \nType your response here: ")
        global remaining_lease
        global flat_type
        if grant_property_choice == "1":
            remaining_lease = properties_details_dict['Property 1']["Remaining Lease"]
            flat_type = properties_details_dict['Property 1']["Flat Type"]
            break
        elif grant_property_choice == "2":
            remaining_lease = properties_details_dict['Property 2']["Remaining Lease"]
            flat_type = properties_details_dict['Property 2']["Flat Type"]
            break
        elif grant_property_choice == "3":
            remaining_lease = properties_details_dict['Property 3']["Remaining Lease"]
            flat_type = properties_details_dict['Property 3']["Flat Type"]
            break
        elif grant_property_choice == "4":
            remaining_lease = properties_details_dict['Property 4']["Remaining Lease"]
            flat_type = properties_details_dict['Property 4']["Flat Type"]
            break
        elif grant_property_choice == "5":
            remaining_lease = properties_details_dict['Property 5']["Remaining Lease"]
            flat_type = properties_details_dict['Property 5']["Flat Type"]
            break
        elif grant_property_choice == "6":
            remaining_lease = properties_details_dict['Property 6']["Remaining Lease"]
            flat_type = properties_details_dict['Property 6']["Flat Type"]
            break
        elif grant_property_choice == "7":
            remaining_lease = properties_details_dict['Property 7']["Remaining Lease"]
            flat_type = properties_details_dict['Property 7']["Flat Type"]
            break
        elif grant_property_choice == "8":
            remaining_lease = properties_details_dict['Property 8']["Remaining Lease"]
            flat_type = properties_details_dict['Property 8']["Flat Type"]
            break
        elif grant_property_choice == "9":
            remaining_lease = properties_details_dict['Property 9']["Remaining Lease"]
            flat_type = properties_details_dict['Property 9']["Flat Type"]
            break
        elif grant_property_choice == "10":
            remaining_lease = properties_details_dict['Property 10']["Remaining Lease"]
            flat_type = properties_details_dict['Property 10']["Flat Type"]
            break
        else:
            print("\nPlease enter a valid option.")
    return remaining_lease, flat_type


# Functions - Housing Grants for Married Individuals
proximity_housing_grant_families_amount = [30000, 20000]

def housing_grants_married():
    proximity_housing_grant_married()
    family_housing_grants()

def proximity_housing_grant_married():
    print("\n--- Proximity Housing Grant ---")
    if citizenship_input == "Singaporean" or citizenship_input == "Singapore PR":
        proximity_grant_married_condition_family_member()
    else:
        print("\nYou are not eligible for the Proximity Housing Grant for Families.")

def proximity_grant_married_condition_family_member():    
    while True:  
        family_citizenship = input("\nDo you have at least one other family member who is a Singaporean Citizen or Singapore PR? \n[1] Yes \n[2] No \nType your response here: ")  
        if family_citizenship == "1":
            proximity_grant_married_condition_history()
            break
        elif family_citizenship == "2":
            print("\nYou are not eligible for the Proximity Housing Grant for Families.")
            break
        else:
            print("\nPlease enter a valid option.")
 
def proximity_grant_married_condition_history():
    while True:
        phg_eligibility = input("\nHave you taken the Proximity Housing Grant in the past? \n[1] Yes \n[2] No \nType your response here: ")
        if phg_eligibility == "1":
            print("\nYou are not eligible for the Proximity Housing Grant for Families.")
            break
        elif phg_eligibility == "2":
            proximity_grant_married_condition_distance()
            break
        else:
            print("\nPlease enter a valid option.")
     
def proximity_grant_married_condition_distance():
    while True:
        proximity_condition = input("\nAre you living with or near your parents/children? \n[1] With \n[2] Near \n[3] None of the above \nType your response here: ")
        if proximity_condition == "1" or proximity_condition == "2":
            break
        elif proximity_condition == "3":
            print("\nYou are not eligible for the Proximity Housing Grant for Families.")
            break
        else:
            print("\nPlease enter a valid option.")

    if proximity_condition == "1" and remaining_lease >= 20: 
        print("\nYou are eligible to apply for the Proximity Housing Grant for Families, of ${:,}".format(proximity_housing_grant_families_amount[0]))
        
    elif proximity_condition == "2" and remaining_lease >= 20 and flat_type == "2 room" or flat_type == "3 room" or flat_type == "4 room" or flat_type == "5 room":           
        while True:
            try:
                proximity_distance = float(input("\nHow far away do you live from them (in km)? \nType your response here: "))
                break
            except:
                print("\nPlease enter a valid option.")
        if proximity_distance <= 4:
            print("\nYou are eligible to apply for the Proximity Housing Grant for Families, of ${:,}".format(proximity_housing_grant_families_amount[1]))
        else: 
            print("\nYou are not eligible for the Proximity Housing Grant for Families.")


cpf_housing_grant_families_flattype = ["2 to 4 room", "5 room"]
cpf_housing_grant_families_amount_singaporeans = [50000, 40000]
cpf_housing_grant_families_amount_singaporeanandpr = [40000, 30000]

stepup_cpf_housing_grant_amount= [15000]

def family_housing_grants():
    print("\n--- Family Housing Grants ---")
    if citizenship_input == "Non-Singaporean":
        print("\nYou are not eligible for any grants.")
        sys.exit()
    while True:
        household_status = input("\nAre you a first-time grant applicant? \n[1] Yes \n[2] No \nType your response here: ")
        if household_status == "1" and age_input >= 21:
            cpf_housing_grant_families()
            break
        elif household_status == "1" and age_input < 21:
            print("\nYou are not eligible for the CPF Housing Grant for Families.")
            break
        elif household_status == "2":
            stepup_cpf_housing_grant()
            break
        else:
            print("\nPlease enter a valid option.")


def cpf_housing_grant_families():
    print("\n--- CPF Housing Grant ---")
    while True:
        try:
            monthly_household_income = int(input("Please enter your Monthly Household Income: $"))
            if monthly_household_income > 0 and monthly_household_income <= 14000:
                break
            elif monthly_household_income > 14000:
                print("\nYou are not eligible for the CPF Housing Grant for Families.")
                sys.exit()
            elif monthly_household_income <= 0:
                print("\nPlease enter a positive numeric value.")
        except ValueError:
            print("\nPlease enter a positive numeric value.")

    while True:
        spouse_citizenship = input("Is your spouse a: \n[1] Singaporean \n[2] Singapore PR \n[3] Non-Singaporean \nType your response here: ")

        if citizenship_input == "Singaporean" and spouse_citizenship == "1":
            cpf_housing_grant_eligibility_singaporeans()
            break
                    
        elif citizenship_input == "Singaporean" and spouse_citizenship == "2":
            cpf_housing_grant_eligibility_singaporeanandpr()
            break

        elif citizenship_input == "Singapore PR" and spouse_citizenship == "1":
            cpf_housing_grant_eligibility_singaporeanandpr()
            break

        elif citizenship_input == "Singapore PR" and spouse_citizenship == "2":
            print("\nYou are not eligible for the CPF Housing Grant for Families.")
            break

        elif spouse_citizenship == "3":
            print("\nYou are not eligible for the CPF Housing Grant for Families.")
            break
        
        else:
            print("\nPlease enter a valid option.")


def cpf_housing_grant_eligibility_singaporeans():
    if remaining_lease > 20 and flat_type == "2 room" or flat_type == "3 room" or flat_type == "4 room":
        print("\nYou are eligible to apply for the CPF Housing Grant for Families ({:s}), of ${:,}.".format(cpf_housing_grant_families_flattype[0], cpf_housing_grant_families_amount_singaporeans[0]))
    elif remaining_lease > 20 and flat_type == "5 room":
        print("\nYou are eligible to apply for the CPF Housing Grant for Families ({:s}), of ${:,}.".format(cpf_housing_grant_families_flattype[1], cpf_housing_grant_families_amount_singaporeans[1]))
    else:
        print("\nYou are not eligible for the CPF Housing Grant for Families.")


def cpf_housing_grant_eligibility_singaporeanandpr():
    if remaining_lease > 20 and flat_type == "2 room" or flat_type == "3 room" or flat_type == "4 room":
        print("\nYou are eligible to apply for the CPF Housing Grant for Families ({:s}), of ${:,}.".format(cpf_housing_grant_families_flattype[0], cpf_housing_grant_families_amount_singaporeanandpr[0]))
    elif remaining_lease > 20 and flat_type == "5 room":
        print("\nYou are eligible to apply for the CPF Housing Grant for Families ({:s}), of ${:,}.".format(cpf_housing_grant_families_flattype[1], cpf_housing_grant_families_amount_singaporeanandpr[1]))
    else:
        print("\nYou are not eligible for the CPF Housing Grant for Families.")


def stepup_cpf_housing_grant():
    print("\n--- Step-Up CPF Housing Grant ---")
    while True:
        try:
            monthly_household_income = int(input("\nPlease enter your Monthly Household Income: $"))
            if monthly_household_income > 0:
                break
            elif monthly_household_income < 0:
                print("\nPlease enter a positive numeric value.")
        except ValueError:
            print("\nPlease enter a positive numeric value.")

    if monthly_household_income <= 7000:
        while True:
            employment_status = input("\nHave you or your spouse worked continuously for at least 12 months prior to today and/or are you or your spouse currently working? \n[1] Yes \n[2] No \nType your response here: ")
            if employment_status == "1" and remaining_lease > 20:
                print("\nYou are eligible for the Step-Up CPF Housing Grant of ${:,}.".format(stepup_cpf_housing_grant_amount[0]))
                break
            elif employment_status == "2":
                print("\nYou are not eligible for the Step-Up CPF Housing Grant.")
                break
            elif employment_status != "1" or employment_status != "2":
                print("\nPlease enter a valid option.")
    else:
        print("\nYou are not eligible for the Step-Up CPF Housing Grant.")


# Functions - Housing Grants for Single Individuals
cpf_housing_grant_singles_flattype = ["2 to 4 room", "5 room"]
cpf_housing_grant_singles_amount = [25000, 20000]

proximity_housing_grant_singles_amount = [15000, 10000]
        
def housing_grants_singles():
    if citizenship_input == "Non-Singaporean" or citizenship_input == "Singapore PR" or remaining_lease <= 20:
        print("\nYou are not eligible for any grants.")
    elif citizenship_input == "Singaporean" and remaining_lease > 20:
        proximity_housing_grant_singles()
        cpf_housing_grant_singles()
    else:
        print("\nYou are not eligible for any grants.")

def proximity_housing_grant_singles():
    print("\n--- Proximity Housing Grant ---")
    while True:
        phg_eligibility = input("Have you taken the Proximity Housing Grant in the past? \n[1] Yes \n[2] No \nType your response here: ")
        if phg_eligibility == "1":
            print("\nYou are not eligible for the Proximity Housing Grant.")
            break
        elif phg_eligibility == "2":
            proximity_grant_single_condition_family_member()
            break
        else:
            print("\nPlease enter a valid option.")


def proximity_grant_single_condition_family_member():
    while True:
        proximity_condition = input("\nAre you living with or near your parents/children? \n[1] With \n[2] Near \n[3] None of the above \nType your response here: ")
        if proximity_condition == "1":
            print("\nYou are eligible to apply for the Proximity Housing Grant for Singles, of ${:,}.".format(proximity_housing_grant_singles_amount[0]))
            break
        elif proximity_condition == "2" and flat_type == "2 room" or flat_type == "3 room" or flat_type == "4 room" or flat_type == "5 room":
            proximity_grant_single_condition_distance()
            break
        elif proximity_condition == "3":
            print("\nYou are not eligible for the Proximity Housing Grant for Singles.") 
            break
        else:
            print("\nPlease enter a valid option.")


def proximity_grant_single_condition_distance():
    while True:
        try:
            proximity_distance = float(input("\nHow far away do you live from them (in km)? \nType your response here: "))
            if proximity_distance <= 4 and proximity_distance > 0:
                print("\nYou are eligible to apply for the Proximity Housing Grant for Singles, of ${:,}.".format(proximity_housing_grant_singles_amount[1]))
                break
            elif proximity_distance > 4:
                print("\nYou are not eligible for the Proximity Housing Grant for Singles.")
                break
            else:
                print("\nPlease enter a positive numeric value.")
        except ValueError:
            print("\nPlease enter a positive numeric value.")

def cpf_housing_grant_singles():
    print("\n--- CPF Housing Grant ---")
    while True:
        household_status = input("Are you a first-time grant applicant? \n[1] Yes \n[2] No \nType your response here: ")
        if household_status == "1" or household_status == "2":
            break
        else:
            print("\nPlease enter a valid option.")
          
    if household_status == "1":
        while True:
            try:
                monthly_household_income = int(input("\nPlease enter your Monthly Household Income: $"))
                if monthly_household_income > 0:
                    break
                else:
                    print("\nPlease enter a positive numeric value.")   
            except ValueError:
                print("\nPlease enter a positive numeric value.")
                
        if monthly_household_income <= 7000:
                if flat_type == "2 room" or flat_type == "3 room" or flat_type == "4 room":
                    print("\nYou are eligible to apply for the CPF Housing Grant for Singles ({:s}), of ${:,}.".format(cpf_housing_grant_singles_flattype[0], cpf_housing_grant_singles_amount[0]))
                elif flat_type == "5 room":
                    print("\nYou are eligible to apply for the CPF Housing Grant for Singles ({:s}), of ${:,}.".format(cpf_housing_grant_singles_flattype[1], cpf_housing_grant_singles_amount[1]))
                else:
                    print("\nYou are not eligible for the CPF Housing Grant for Singles.")
        else:
            print("\nYou are not eligible for the CPF Housing Grant for Singles.")

    elif household_status == "2":
        print("\nYou are not eligible for the CPF Housing Grant for Singles.")


def grant_eligibility():
    print("\n--- Section 3: Housing Grants Eligibility ---")
    if grant_property_details()[1] == "Condominium":
        print("\nCondominiums are not eligible for HDB Grants.")
    else:
        if marital_status_input == "Married":
            housing_grants_married()
        elif marital_status_input == "Single":
            housing_grants_singles()


# Section 4: Search for Amenities Nearby the Chosen Property
amenities_dict = {
"Property 1": {
    "Malls": "The Seletar Mall",
    "Schools": "Sengkang Primary School,Fernvale Primary School,Pei Hwa Secondary School,My First Skool @ 51 Fernvale Link",
    "Transportation": "Fernvale LRT Station",
    "Others": "Fernvale Community Club,ActiveSG Gym,Sengkang Sports Centre"
},
"Property 2": {
    "Malls": "Yew Tee Point,Yew Tee Square",
    "Schools": "Unity Primary School,Yew Tee Primary School,Kranji Primary School",
    "Transportation": "Yew Tee MRT Station,Choa Chu Kang MRT Station",
    "Others": "Yew Tee Community Club,Yew Tee Neighbourhood Police Station"
},
"Property 3": {
    "Malls": "Sun Plaza",
    "Schools": "Northoaks Primary School,Endeavour Primary School",
    "Transportation": "Sembawang MRT Station",
    "Others": "Masjid Assyafaah,Giant Express,Canberra Community Club"
},
"Property 4": {
    "Malls": "West Coast Plaza,Clementi Mall",
    "Schools": "Nan Hua Primary School,Kent Ridge Secondary School,International Community School",
    "Transportation": "Clementi MRT Station",
    "Others": "Ayer Rajah Food Centre,Sheng Siong Supermarket,Clementi ActiveSG Stadium"
},
"Property 5": {
    "Malls": "Gek Poh Shopping Centre,Pioneer Mall, Jurong Point",
    "Schools": "Westwood Primary School,West Grove Primary School,Pioneer Primary School,MOE Kindergarten @ Westwood",
    "Transportation": "Boon Lay MRT Station",
    "Others": "Sheng Siong Hypermarket,Gek Poh Ville Community Centre"
},
"Property 6": {
    "Malls": "IMM Shopping Mall,JEM,Westgate",
    "Schools": "Fuhua Primary School,Yuhua Primary School,Shuqun Secondary School,My First Skool @ Westgate",
    "Transportation": "Jurong East MRT Station",
    "Others": "Jurong East Swimming Complex,The Chevrons"
},
"Property 7": {
    "Malls": "IMM Shopping Mall,JEM,Westgate",
    "Schools": "Fuhua Primary School,Yuhua Primary School,Shuqun Secondary School,My First Skool @ Westgate",
    "Transportation": "Jurong East MRT Station",
    "Others": "Jurong East Swimming Complex,The Chevrons"
},
"Property 8": {
    "Malls": "Admiralty Place,888 Plaza",
    "Schools": "Greenwood Primary School,Woodlands Ring Primary School,Woodlands Ring Secondary School",
    "Transportation": "Woodlands South MRT Station,Admiralty MRT Station,Woodlands MRT Station",
    "Others": "NTUC Fairprice,Giant Hypermart"
},
"Property 9": {
    "Malls": "Bedok Mall",
    "Schools": "Yu Neng Primary School,Red Swastika Secondary School",
    "Transportation": "Bedok MRT Station",
    "Others": "Kaki Bukit Community Centre,Bedok Town Park,NTUC @ Bedok Mall"
},
"Property 10": {
    "Malls": "United Square Shopping Mall,Velocity @ Novena Square,Square 2",
    "Schools": "NIL",
    "Transportation": "Newton MRT Station,Novena MRT Station,Little India MRT Station",
    "Others": "NTUC Fairprice,Cold Storage"
}}


def search_amenities():
    print("\n--- Section 4: Search for Amenities Nearby Chosen Property ---")
    while True: 
        # To allow users to select a particular property to search for its nearby amenities,
        # and loop if users enter a value that is not within 1 to 10.
        amenity_property_choice = input("\nPlease select a property to search for its nearby amenities. \n[1] Property 1 \n[2] Property 2 \n[3] Property 3 \n[4] Property 4 \n[5] Property 5 \n[6] Property 6 \n[7] Property 7 \n[8] Property 8 \n[9] Property 9 \n[10] Property 10 \nType your response here: ")
        if amenity_property_choice == "1":
            chosen_property = "Property 1"
            break
        elif amenity_property_choice == "2":
            chosen_property = "Property 2"
            break
        elif amenity_property_choice == "3":
            chosen_property = "Property 3"
            break
        elif amenity_property_choice == "4":
            chosen_property = "Property 4"
            break
        elif amenity_property_choice == "5":
            chosen_property = "Property 5"
            break
        elif amenity_property_choice == "6":
            chosen_property = "Property 6"
            break
        elif amenity_property_choice == "7":
            chosen_property = "Property 7"
            break
        elif amenity_property_choice == "8":
            chosen_property = "Property 8"
            break
        elif amenity_property_choice == "9":
            chosen_property = "Property 9"
            break
        elif amenity_property_choice == "10":
            chosen_property = "Property 10"
            break
        else: 
            print("\nPlease enter a valid option.")

    while True:
        # To allow users to select the type of amenities they are interested in, 
        # and loop if users enter a value that is not from 1 to 4.
        chosen_amenity = input("\nSelect an option:\n[1] View nearby Malls \n[2] View nearby Schools \n[3] View nearby Transportations \n[4] Others \nType your response: ")
        if chosen_amenity == "1":
            chosen_amenity = "Malls"
            break
        elif chosen_amenity == "2":
            chosen_amenity = "Schools"
            break
        elif chosen_amenity == "3":
            chosen_amenity = "Transportation"
            break
        elif chosen_amenity == "4":
            chosen_amenity = "Others"
            break
        else:
            print("\nPlease enter a valid option.")
        
    # To extract the key (ie. Chosen Property) from the amenities_dict.
    # For example, if the user selected 'Property 1', it will extract and
    # property_dict will only contain the dictionary of amenities of 'Property 1'.
    property_dict = dict((k,amenities_dict[k]) for k in [chosen_property] if k in amenities_dict)
    
    # To filter out the Chosen Amenity within the Chosen Property.
    output = property_dict[chosen_property][chosen_amenity]
    
    # A header to allow users to identify which Amenity and Property they have chosen.
    print("\n{} nearby {} is/are as listed: ".format(chosen_amenity, chosen_property))
    
    # To print each Amenity in a separate line for better readability.
    for each_amenity in output.split(","):
        print(each_amenity)
    
    while True:
        # To allow users to repeat the process of searching for more Amenities.
        repeat_search_amenity = input("\nWould you like to search for more amenities? \n[1] Yes \n[2] No \nType your response: ")
        if repeat_search_amenity == "1":
            search_amenities()
            break
        elif repeat_search_amenity == "2":
            break
        else:
            print("\nPlease enter a valid option.")
            
            
def proptech():
    while True:
        print(f"""\nHow can we help you today, {name_input}?
[1] Property Search
[2] Check Grant(s) Eligiblity
[3] Search for Nearby Amenities
[4] Exit Program
""")
        proptech_option = input("Enter your choice (1-4): ")
        if proptech_option == "1":
            search_properties(properties)
        elif proptech_option == "2":
            grant_eligibility()
        elif proptech_option == "3":
            search_amenities()
        elif proptech_option == "4":
            print("\nThank you for using PropTech!")
            sys.exit()
        else:
            print("\nInvalid input. Please try again.")
            continue
        
proptech()