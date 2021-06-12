import random

def AutomatedDoor(percept):
    percepts =[]
    table = {
        #Let, The door is Closed. And there are some possible situations that may arise.
        # Right corner shows the possible decisions that may be taken upon situation. 
        (('Neither', 'CLOSED'),): 'CLOSED',
        (('Front', 'CLOSED'),): 'OPEN',
        (('REAR', 'CLOSED'),): 'CLOSED',
        (('Both', 'CLOSED'),): 'CLOSED',

        #Let, The door is Opened. And there are some possible situations that may arise.
        # Right corner shows the possible decisions that may be taken upon situation. 
        (('Neither', 'OPEN'),): 'CLOSED',
        (('Front', 'OPEN'),): 'OPEN',
        (('REAR', 'OPEN'),): 'OPEN',
        (('Both', 'OPEN'),): 'OPEN',
        
    }

    percepts.append(percept)
    action = table[tuple(percepts)]

    return action


Person_A, Person_B,Person_loc,Absence = 'Front', 'Rear','Both','Neither'

situation = random.choice([Person_B, Person_A,Person_loc,Absence])
status = random.choice(['OPEN', 'CLOSED'])

percept = (situation, status)
action = AutomatedDoor(percept)
print("Door Current Status",status," Situation: ", situation, " and Changed Status: ", action)

