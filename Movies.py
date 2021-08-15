import  _sqlite3

#SQLITE Connection
con = _sqlite3.connect('movies.db')
cursor = con.cursor()

print("Connected to SQLite")


# Create Table


# con = _sqlite3.connect("movies.db")
# cur=con.cursor()
# print("connected to the database!")
# query="""CREATE TABLE IF NOT EXISTS Movies(
# movieId NUMBER (5) CONSTRAINT ADD_AID_PK PRIMARY KEY,
# Name VARCHAR2 (50),
# Actor VARCHAR2 (50),
# Actress VARCHAR2 (50),
# Director VARCHAR2 (50),
# YOR VARCHAR2 (20)
# );"""

# # cur.execute(query)
# print("table created")


def insertVaribleIntoTable(movieId , Name,Actor , Actress, Director,YOR):
    try:


        sqlite_insert_with_param = """INSERT INTO Movies
                          (movieId , Name, Actor , Actress, Director,YOR)
                          VALUES (?, ?, ?, ?, ?,?);"""

        data_tuple = (movieId , Name,Actor , Actress, Director,YOR)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        con.commit()
        print("Movies inserted successfully into movies table")



    except _sqlite3.Error as error:
        print("Failed to insert  into movies table", error)



# insertVaribleIntoTable(1, 'harrypoter', 'james', 'emma', 'JKR',2010)
# insertVaribleIntoTable(2, 'lucifer', 'joe', 'grace', 'steve',2019)
# insertVaribleIntoTable(3, 'LION king', 'james', 'jake', 'mel',2020)
# insertVaribleIntoTable(12, 'five feets apart', 'coel', 'jinny', 'mel',2019)



def readSqliteTable():
    try:



        sqlite_select_query = """SELECT * from Movies"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("movieId: ", row[0])
            print("Name: ", row[1])
            print("Actor: ", row[2])
            print("Actress: ", row[3])
            print("Director: ", row[4])
            print("YOR: ", row[5])
            print("\n")



    except _sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    # finally:
    #     if con:
    #         con.close()
    #         print("The SQLite connection is closed")





def getMovieInfo(Actor):
    try:

        sql_select_query = """select * from Movies where Actor = ?"""
        cursor.execute(sql_select_query, (Actor,))
        records = cursor.fetchall()
        print("Printing movieId ", Actor)
        for row in records:
            print("movieId: ", row[0])
            print("Name: ", row[1])

            print("Actress: ", row[2])
            print("Director: ", row[3])
            print("YOR: ", row[4])
            print("\n")


    except _sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    # finally:
    #     if con:
    #         con.close()
    #         print("The SQLite connection is closed")


def main():

    print("Intresting  Movies")
    print("What you want to do?  1.Insert a Movie Info 2.See Movies According to the Actor  3.View_All_Movies 4.Exit")

    ch = int(input("Enter Your Choice 1 T0 4 :"))

    if ch == 1:
        movieId=int(input("Enter the Movie id"))
        Name=input("Enter Movie name")
        Actor = input("Enter Actor name")
        Actress = input("Enter Actress name")
        Director = input("Enter Director name")
        YOR= input("Enter Year of realise ")

        insertVaribleIntoTable(movieId , Name,Actor , Actress, Director,YOR)
    elif ch == 2:
        Actor=input("Please Enter the Actor name")
        getMovieInfo(Actor)
    elif ch == 3:
        readSqliteTable()

    else :
        exit()

main()


cursor.close()
con.close()
print("The SQLite connection is closed")
