import random
import time

slot_1 = " "
slot_2 = " "
slot_3 = " "
slot_4 = " "
slot_5 = " "
slot_6 = " "
slot_7 = " "
slot_8 = " "
slot_9 = " "

win = 0

print("")
print("")
        

row_1 = f" {slot_1} | {slot_2} | {slot_3} "
row_2 = f" {slot_4} | {slot_5} | {slot_6} "
row_3 = f" {slot_7} | {slot_8} | {slot_9} "
bar = "-----------"

possible_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
string_slots = ['1', '2', '3', '4', '5', '6', '7' ,'8', '9']

def condition(cond1, cond2, slots, figure, slot):
    if cond1 == cond2:
        slots.remove(cond2)
        return figure
    return slot

def check(slot1, slot2, slot3, figure, result, statement):
    if slot1 == figure and slot2 == figure and slot3 == figure:
        print(statement)
        return True
    return result

def block(slot1, slot2, slot3, place1, place2, place3, figure, ai):
    if slot1 == figure and slot2 == figure and slot3 == " ":
        return place3
    if slot1 == figure and slot3 == figure and slot2 == " ":
        return place2
    if slot2 == figure and slot3 == figure and slot1 == " ":
        return place1
    return ai

print(f" 1 | 2 | 3 ")
print(bar)
print(f" 4 | 5 | 6 ")
print(bar)
print(f" 7 | 8 | 9 ")

while win == 0:
    print("")
    print("")
    if possible_slots == []:
        if win != True:
            print("Tie!")
            win = True
        break
    user = input("Choose a slot: ")
    while user not in string_slots:
        user = input("Choose again: ")
    user = int(user)
    slot_1 = condition(user, 1, possible_slots, "X", slot_1)
    slot_2 = condition(user, 2, possible_slots, "X", slot_2)
    slot_3 = condition(user, 3, possible_slots, "X", slot_3)
    slot_4 = condition(user, 4, possible_slots, "X", slot_4)
    slot_5 = condition(user, 5, possible_slots, "X", slot_5)
    slot_6 = condition(user, 6, possible_slots, "X", slot_6)
    slot_7 = condition(user, 7, possible_slots, "X", slot_7)
    slot_8 = condition(user, 8, possible_slots, "X", slot_8)
    slot_9 = condition(user, 9, possible_slots, "X", slot_9)
    
    row_1 = f" {slot_1} | {slot_2} | {slot_3} "
    row_2 = f" {slot_4} | {slot_5} | {slot_6} "
    row_3 = f" {slot_7} | {slot_8} | {slot_9} "
    
    print("")
    print("")
    
    
    print(row_1)
    print(bar)
    print(row_2)
    print(bar)
    print(row_3)
    
    win = check(slot_1, slot_2, slot_3, "X", win, "You Won!")
    win = check(slot_4, slot_5, slot_6, "X", win, "You Won!")
    win = check(slot_7, slot_8, slot_9, "X", win, "You Won!")
    
    win = check(slot_1, slot_4, slot_7, "X", win, "You Won!")
    win = check(slot_2, slot_5, slot_8, "X", win, "You Won!")
    win = check(slot_3, slot_6, slot_9, "X", win, "You Won!")
    
    win = check(slot_1, slot_5, slot_9, "X", win, "You Won!")
    win = check(slot_3, slot_5, slot_7, "X", win, "You Won!")
    if win == True:
        break
    
    
    time.sleep(1)
    
    
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    
    
    
    if possible_slots == []:
        print("Tie!")
        break
        win = True
    
    ai = random.randint(1, 9)
    while ai not in possible_slots:
        ai = random.randint(1, 9)
    
    ai = block(slot_1, slot_2, slot_3, 1, 2, 3, "X", ai)
    ai = block(slot_4, slot_5, slot_6, 4, 5, 6, "X", ai)
    ai = block(slot_7, slot_8, slot_9, 7, 8, 9, "X", ai)
    
    ai = block(slot_1, slot_4, slot_7, 1, 4, 7, "X", ai)
    ai = block(slot_2, slot_5, slot_8, 2, 5, 8, "X", ai)
    ai = block(slot_3, slot_6, slot_9, 3, 6, 9, "X", ai)
    
    ai = block(slot_1, slot_5, slot_9, 1, 5, 9, "X", ai)
    ai = block(slot_3, slot_5, slot_7, 3, 5, 7, "X", ai)
    
    
    
    
    ai = block(slot_1, slot_2, slot_3, 1, 2, 3, "O", ai)
    ai = block(slot_4, slot_5, slot_6, 4, 5, 6, "O", ai)
    ai = block(slot_7, slot_8, slot_9, 7, 8, 9, "O", ai)
    
    ai = block(slot_1, slot_4, slot_7, 1, 4, 7, "O", ai)
    ai = block(slot_2, slot_5, slot_8, 2, 5, 8, "O", ai)
    ai = block(slot_3, slot_6, slot_9, 3, 6, 9, "O", ai)
    
    ai = block(slot_1, slot_5, slot_9, 1, 5, 9, "O", ai)
    ai = block(slot_3, slot_5, slot_7, 3, 5, 7, "O", ai)
    
    
    slot_1 = condition(ai, 1, possible_slots, "O", slot_1)
    slot_2 = condition(ai, 2, possible_slots, "O", slot_2)
    slot_3 = condition(ai, 3, possible_slots, "O", slot_3)
    slot_4 = condition(ai, 4, possible_slots, "O", slot_4)
    slot_5 = condition(ai, 5, possible_slots, "O", slot_5)
    slot_6 = condition(ai, 6, possible_slots, "O", slot_6)
    slot_7 = condition(ai, 7, possible_slots, "O", slot_7)
    slot_8 = condition(ai, 8, possible_slots, "O", slot_8)
    slot_9 = condition(ai, 9, possible_slots, "O", slot_9)
    
    row_1 = f" {slot_1} | {slot_2} | {slot_3} "
    row_2 = f" {slot_4} | {slot_5} | {slot_6} "
    row_3 = f" {slot_7} | {slot_8} | {slot_9} "
    
    
    print(row_1)
    print(bar)
    print(row_2)
    print(bar)
    print(row_3)

    win = check(slot_1, slot_2, slot_3, "O", win, "You Lost!")
    win = check(slot_4, slot_5, slot_6, "O", win, "You Lost!")
    win = check(slot_7, slot_8, slot_9, "O", win, "You Lost!")
    win = check(slot_1, slot_4, slot_7, "O", win, "You Lost!")
    win = check(slot_2, slot_5, slot_8, "O", win, "You Lost!")
    win = check(slot_3, slot_6, slot_9, "O", win, "You Lost!")
    win = check(slot_1, slot_5, slot_9, "O", win, "You Lost!")
    win = check(slot_3, slot_5, slot_7, "O", win, "You Lost!")


