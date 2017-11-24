"""JUANA GUTIERREZ GONZALEZ
 GITI9072  juanizg7@gmail.com
 1215100194"""

import psycopg2
from config import config

def create_tables():

    """ create tables in the postgresql database"""
    commands = (
        """
          CREATE TABLE log (
                  id SERIAL PRIMARY KEY NOT NULL, 
                  ts TIMESTAMP NOT NULL,
                  phrase VARCHAR (128) NOT NULL,
                  letters VARCHAR (32) NOT NULL,
                  ip VARCHAR (16) NOT NULL,
                  browser_string VARCHAR (256) NOT NULL,
                  rsults VARCHAR (64) NOT NULL
          ) 
        """,

        """
          CREATE TABLE vendors(
                  vendor_id SERIAL PRIMARY KEY NOT NULL,
                  vendor_name VARCHAR (255) NOT NULL 
          )
        """,

        """
          CREATE TABLE parts(
                  part_id SERIAL PRIMARY KEY,
                  part_name VARCHAR (255) NOT NULL 
          )
        """,

        """
          CREATE TABLE parts_drawnings(
                  part_id INTEGER PRIMARY KEY,
                  file_extension VARCHAR (5) NOT NULL,
                  drawning_date BYTEA NOT NULL,
                  FOREIGN KEY (part_id)
                      REFERENCES parts(part_id)
                      ON UPDATE CASCADE ON DELETE CASCADE 
          )
        """,

        """
          CREATE TABLE vendor_parts(
                  vendor_id INTEGER NOT NULL,
                  part_id INTEGER NOT NULL,
                  PRIMARY KEY (vendor_id, part_id),
                  FOREIGN KEY (vendor_id)
                      REFERENCES vendors(vendor_id)
                      ON UPDATE CASCADE ON DELETE CASCADE,
                  FOREIGN KEY (part_id)
                      REFERENCES parts(part_id)
                      ON UPDATE CASCADE ON DELETE CASCADE
          )
        """
    )

    conn = None
    try:
        # read the connection parameters
        params = config()

        # connect to the
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        #create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the psql database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()