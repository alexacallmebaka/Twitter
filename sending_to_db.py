import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    db='mydatabase',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def if_exists(user):
    try:
        with conn.cursor() as cursor:
            # Create a new record
            sql = "SELECT Name, COUNT(*) FROM Item_Info WHERE Name = %s GROUP BY Name"
            cursor.execute(sql, (user))

        # execute statement same as above  
        msg = cursor.fetchone()  
        # check if it is empty and print error
        if not msg:
            print('It does not exist')
    finally:
        conn.close()

def insert_to(user,pswd):
    try:
        with conn.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, (user, pswd))

        # Commit changes
        conn.commit()

        print("Record inserted successfully")
    finally:
        conn.close()

def update_with(user, pswd):
    try:
        with conn.cursor() as cursor:
            # Update a record
            sql = "UPDATE `users` SET `password`=%s WHERE `email`=%s"
            cursor.execute(sql, (user, pswd))

        # Commit changes
        conn.commit()

        print("Record updated successfully")
    finally:
        conn.close()

def get_user(username):
    try:
        with conn.cursor() as cursor:
            # Read data from database
            sql = "SELECT * FROM `users` WHERE `user` == %s"
            cursor.execute(sql(username))
            # Fetch user & pass
            value = cursor.fetchall()
    #hash the password
    finally:
        conn.close()
    return value