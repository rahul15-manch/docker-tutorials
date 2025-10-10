import pymysql 

def create_connection():
    return pymysql.connect(
        host='localhost',
        user="root",
        password="Rahul@_123",
        database="userinfo"
    )
def create_table(connection):
    cursor=connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS names (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100)''')
    connection.commit()
    cursor.close()
def insert_name(connection, name):
    cursor=connection.cursor()
    cursor.execute("INSERT INTO names (name) VALUES (%s)", (name,))
    connection.commit()
    cursor.close()
def fetch_all_names(connection):
    cursor=connection.cursor()
    cursor.execute("SELECT name FROM names")
    names=[row[0] for row in cursor.fetchall()]
    cursor.close()
    return names
def main():
    connection=create_connection()
    create_table(connection)

    while True:
        print("1. Add Name")
        print("2. Showw All names")
        print("3. Exit")
        choice=input("Enter your choice: ")
        if choice=="1":
            name=input("Enter name to add: ")
            insert_name(connection, name)
            print(f"Name '{name}' added  to the database successfully.")
        elif choice=="2":
            names=fetch_all_names(connection)
            if names:
                print("Names in the database:")
                for name in names:
                    print(f"- {name}")
            else:
                print("No names found in the database.")
        elif choice=="3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    connection.close()
if __name__=="__main__":
    main()

        