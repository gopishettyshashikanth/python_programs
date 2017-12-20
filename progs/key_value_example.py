import random

stName_list={'Andhra Pradesh':1,'Telangana':2}
no_anms =input("enter number of args") 

for i in range(no_anms):
	state_choice = random.choice(stName_list.keys())
	print state_choice
state_code = stName_list[state_choice]
print state_code
    # if state_choice == 'Andhra Pradesh':
    #             #distNames={'vizag' :30 ,'krishna':40}
    #         elif state_choice == 'Telangana':     
    #             #distNames={'Hyderabad' :10 ,'Medak':20}
    #         #dist_choice = random.choice(distNames.keys())