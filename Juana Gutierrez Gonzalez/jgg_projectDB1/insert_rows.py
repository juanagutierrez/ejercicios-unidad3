"""JUANA GUTIERREZ GONZALEZ
 GITI9072  juanizg7@gmail.com
 1215100194"""

import psycopg2
from config import config

def insert_vendor(vendor_name):

    """ insert a new vendor into the vendors table """

    #In case the primary key of the table is an auto-generated column,
    #you can get the generated ID back after inserting the row. To do this,
    #in the INSERT statement, you use the RETURNING id clause.

    sql = """INSERT INTO vendors(vendor_name)
                 VALUES(%s) RETURNING vendor_id;"""

    conn = None
    vendor_id = None
    try:
        # read database configuration
        params = config()

        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)

        # create a new cursor
        cur = conn.cursor()

        # execute the INSERT statement (sql = sentence, vendor_name= tablename to insert rows)
        cur.execute(sql, (vendor_name,))

        # get the generated id back
        vendor_id = cur.fetchone()[0]

        # commit the changes to the database
        conn.commit()

        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id

def insert_vendor_list(vendor_list):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,vendor_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # insert one vendor
    insert_vendor("3M Co.")
    # insert multiple vendors
    insert_vendor_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])