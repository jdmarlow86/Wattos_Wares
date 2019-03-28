import sqlite3
from sqlite3 import Error


def main():
    database = '/Users/J&E/Desktop/MissionU/Wattos_Wares.sqlite'
 
    # create a database connection
    conn = sqlite3.connect(database)


def AllPlanets ():
    database = '/Users/J&E/Desktop/Wattos_Wares/Wattos_Wares.db'
 
    # create a database connection
    conn = sqlite3.connect(database)
    with conn:
        print("1. These are all planets Watto supplies")
        cur = conn.cursor()
        cur.execute("SELECT * FROM PLANETS")
 
        rows = cur.fetchall()
 
        for row in rows:
            print(row)

    print("\n")
if __name__ == '__AllPlanets__':
    AllPlanets()
    
def AllClients ():
    database = '/Users/J&E/Desktop/MissionU/Wattos_Wares.db'
 
    # create a database connection
    conn = sqlite3.connect(database)
    with conn:
        print("1. These are all clients Watto serves")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Clients")
 
        rows = cur.fetchall()
 
        for row in rows:
            print(row)

        print("\n")
if __name__ == '__AllClients__':
    AllClients()
