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
B - Pay as you go caps
C - Travelcards
D - River Bus services
E - IFS Cloud Cable Car
Please type a,b,c,d or e here: """)

# New bus and tram prices
    if general_question == 'a' or general_question == 'A':
        print("""For Bus and tram as an Adult
- 7 Day and Weekly Cap = £23.30
- Monthly = £89.50	
- Annual =  £932 """)
        print() # Empty space
        
# Pay as you go caps
    elif general_question == 'b' or general_question == 'B':
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
        print() # Empty space

# Travelcards
# Adult Travelcard prices increased by an average of 3.8%.
    elif general_question == 'c' or general_question == 'C':
        print("""Travelcards
Adult Travelcard prices increased by an average of 3.8%.
Zone(s)	                    One Day Anytime	    One Day     Off-peak	7 Day	    Monthly	Annual
Zone 1 only	                £14.40	            £14.40	    £38.40	    £147.50	    £1,536
Zone 1 and 2	            £14.40	            £14.40	    £38.40	    £147.50	    £1,536
Zone 1, 2 and 3	            £14.40	            £14.40	    £45.20	    £173.60	    £1,808
Zone 1, 2, 3 and 4	        £14.40	            £14.40	    £55.20	    £212.00	    £2,208
Zone 1, 2, 3, 4 and 5	    £20.30	            £14.40	    £65.70	    £252.30	    £2,628
Zone 1, 2, 3, 4, 5 and 6	£20.30	            £14.40	    £70.30	    £270	    £2,812
""")
        print() # Empty space
        
# River Bus services
# Pay as you go fares increased on all Uber boats by Thames Clippers.
    elif general_question == 'd' or general_question == 'D':
        print("""River Bus services
River   Zones	    Adult	Child
Central	            £7.70	£3.85
East	            £4.80	£2.40
West	            £4.80	£2.40
Central and East	£8.70	£4.35
Central and West	£8.70	£4.35
West to East	    £13.50	£6.75        """)
        print() # Empty space

# IFS Cloud Cable Car

    elif general_question == 'e' or general_question == 'E':
        print("""IFS Cloud Cable Car: pay as you go and cash fares increased by an overall average of 9.2%.
The adult single pay as you go fare will increase by £1 to £6. The child single fare will remain at half of the adult fare.
Ticket type	Adult	Child
One way (ticket office)	£6.00	£3.00
One way (online, pay as you go)	£5.00	£2.50
Round trip (ticket office)	£12.00	£6.00
Round trip (online)	£10.00	£5.00""")
        print() # Empty space
