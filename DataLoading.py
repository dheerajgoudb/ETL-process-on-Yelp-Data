# Importing MySQL Connector
import mysql.connector

# Function to make connection to server and to create a table
def Connection():
    conn = mysql.connector.connect(user='root', password='admin', host='localhost', database='yelp_data')
    cursor = conn.cursor()
    try:
        query = "CREATE TABLE Restaurants (" \
                "name varchar(255) NOT NULL," \
                "type varchar(255)," \
                "address varchar(255)," \
                "rating float," \
                "`review count` int);"
        cursor.execute(query)
        cursor.close()
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return True

# Function to load the data in table
def Load(businesses):
    conn = mysql.connector.connect(user='root', password='admin', host='localhost', database='yelp_data')
    cursor = conn.cursor()
    for b in businesses:
        name = str(b['name'])
        if name.__contains__("'"):
            name = name.replace("'", "''")
        title = str(b['categories'][0]['alias'])
        address = str(b['location']['display_address'][0])
        rating = float(b['rating'])
        review_count = int(b['review_count'])
        query = "INSERT INTO Restaurants " \
                "(name, type, address, rating, `review count`) " \
                "VALUES ('{0}', '{1}', '{2}', {3}, {4});".format(name, title, address, rating, review_count)
        cursor.execute(query)
    cursor.close()
    conn.commit()
    conn.close()
