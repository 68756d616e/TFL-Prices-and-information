# TFL Transport for london
# Fares from 1 March 2022
# ...

# Welcome message
print("Welcome to TFL Price list")

print() # Empty space

# General question - Either seperate questions or 1 question with multiple choices
while True:
    general_question = input("""Please choose one of the following!
A - New bus and tram prices
B Pay as you go caps
- Travelcards
- River Bus services
- IFS Cloud Cable Car
Please type here: """)

# New bus and tram prices
    if general_question == 'a' or general_question == 'A':
        print("""For Bus and tram as an Adult
- 7 Day and Weekly Cap = £23.30
- Monthly = £89.50	
- Annual =  £932 """)
        print() # Empty space
        print("""Additional information 
- Pay as you go caps
- For Tube, DLR, London Overground, Elizabeth line and National Rail services
- Adult rate daily and weekly caps increased by an average of 3.8%.""")

# Pay as you go caps
    elif general_question == 'b' or general_question == 'B':
        print("") # Empty space
        print("""Pay as you go caps
- For Tube, DLR, London Overground, Elizabeth line and National Rail services
- Adult rate daily and weekly caps increased by an average of 3.8%.
Zone(s)	                    One Day Anytime	    One Day Off-peak	Monday to Sunday
Zone 1  only	            £7.70	            £7.70	            £38.40
Zone 1  and 2	            £7.70	            £7.70	            £38.40
Zone 1, 2 and 3	            £9.00	            £9.00	            £45.20
Zone 1, 2, 3 and 4	        £11.00	            £11.00	            £55.20
Zone 1, 2, 3, 4 and 5	    £13.10	            £13.10	            £65.70
Zone 1, 2, 3, 4, 5 and 6	£14.10	            £14.10	            £70.30""")

# Pay as you go caps
# For Tube, DLR, London Overground, Elizabeth line and National Rail services
# Adult rate daily and weekly caps increased by an average of 3.8%.

# Travelcards
# Adult Travelcard prices increased by an average of 3.8%.

# River Bus services
# Pay as you go fares increased on all Uber boats by Thames Clippers.

# IFS Cloud Cable Car
