import random
import sqlite3

con = sqlite3.connect('RPS_Dataset.db') #Database
cur = con.cursor()
name = input('Enter your name : ') #Name of the player
global user_score
global com_score
user_score = 0
com_score = 0


try:
    cur.execute(f"CREATE TABLE {name} (r int DEFAULT 0.0, p int DEFAULT 0.0, s int DEFAULT 0.0,name str)")
    cur.execute(f"INSERT INTO {name} (name) VALUES ('{name}')")
except:
    pass

# Commands for updating the database
def update_rock():
    cur.execute(f"SELECT * FROM {name} ")
    r = cur.fetchall()
    cur.execute(f"UPDATE {name} SET r = {r[0][0]} + 1 WHERE name = '{name}'")
def update_paper():
    cur.execute(f"SELECT * FROM {name} ")
    p = cur.fetchall()
    cur.execute(f"UPDATE {name} SET p = {p[0][1]} + 1 WHERE name = '{name}'")
def update_scissor():
    cur.execute(f"SELECT * FROM {name} ")
    s = cur.fetchall()
    cur.execute(f"UPDATE {name} SET s = {s[0][2]} + 1 WHERE name = '{name}'")

# Gradual machine learning based on data
def machine_guess():
    cur.execute(f"SELECT * FROM {name} ")
    times = cur.fetchall()
    rock = times[0][0]; paper = times[0][1]; scissor = times[0][2]
    user_probablity = [rock, paper, scissor]
    user_probablity.sort()
    if user_probablity[2] == rock:
        return 'paper'
    elif user_probablity[2] == paper:
        return 'scissor'
    else:
        return 'rock'

# Main part of the game
def win_or_lose(user,machine):
    if user == 'rock':
        update_rock()
        if machine == 'paper':
            global com_score
            com_score += 1 
            return 'Computer Wins!'
        elif machine == 'scissor':
            global user_score
            user_score = user_score + 1
            return 'You Win!'
        else:
            return "It's a tie!"
    elif user == 'paper':
        update_paper()
        if machine == 'scissor':
            
            com_score = com_score + 1
            return 'Computer Wins!'
        elif machine == 'rock':
            
            user_score = user_score + 1
            return 'You Win!'
        else:
            return "It's a tie!"
    elif user == 'scissor':
        update_scissor()
        if machine == 'rock':
            com_score = com_score + 1
            return 'Computer Wins!'
        elif machine == 'paper':
            user_score = user_score + 1
            return 'You Win!'
        else:
            return "It's a tie!"
    else:
        return 'Invalid input!'


# The arena
for i in range(0, 11):
    print("------------------------")
    your = input("Enter your choice (rock/paper/scissor) : ")
    print(f"Computer chose : {machine_guess()}")
    print(f">> {win_or_lose(your, machine_guess())} <<")
    print(f"Your Score : {user_score}")
    print(f"Computer's Score : {com_score}")

if com_score > user_score:
    print("------------------------")
    print("Final Results : Computer Wins!!")
    print(f"Computer : {com_score} -- {name} : {user_score}")
    print("------------------------")
elif user_score > com_score:
    print("------------------------")
    print("Final Results : You Win!!")
    print(f"{name} : {user_score} -- Computer : {com_score}")
    print("------------------------")
else:
    print("------------------------")
    print("Final Results : It's a tie!")
    print(f"{name} : {user_score} -- Computer : {com_score}")
    print("------------------------")


con.commit()
con.close()
