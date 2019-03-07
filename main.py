import sqlite3
import os
import types


class DataBase:
    """
    Description:
        This class handles the all the db operations without
        intervening/mixing with bc's implementation.
    Implementation Detail:
        Uses sqlite3 database for storing.
        The database is stored in the current directory locally.
    """

    def __init__(self, db_name):
        """
        This function creates a new database if db of given name is not existing in the current directory.
        :param db_name: name of the database.
        """
        # uses only db_name to make a db
        self.db_name = db_name

    def get_db_connection(self):
        overwrite_database = None
        # checking if there is an existing db with given name.
        if os.path.exists(self.db_name + ".db"):
            # found an existing instance of the passed db name.
            print("Found an existing database named {}".format(self.db_name))

            # asking user if database can be overwritten.
            ip = input("Do you want to overwrite current database (y/n)??").lower()

            # Following line required when user didn't enter anything(defaults to 'y').
            overwrite_database = 'y' if not ip else ip[0]
        else:
            # permitting control to create a new db when there is no existing db.
            overwrite_database = 'y'

        if overwrite_database == 'y':
            connection = sqlite3.connect(self.db_name)
            return connection
        else:
            return sqlite3.connect(self.db_name)

    def execute_query(self, query):
        connection = self.get_db_connection()
        try:
            connection.execute(query)
        except sqlite3.OperationalError:
            raise Exception("Couldn't execute query. Your query is : \n{}".format(query))

    def add_to_table(self, table_name, values):
        """
        This will add the passed values to the existing table with name as table_name.
        :param table_name: name of the db table in which you want to enter new row.
        :param values: The values which are to be entered in the database.
        :return: None
        """

        # There are two versions of this function based on the data-type of values.
        #     1. When values is of type iterable:
        #          This is used when user knows the order in which data is stored in cols in the database.
        #          This is rarely used in production systems.
        #     2. When values is a dict:
        #          User is unsure of the order of cols in the db.
        #          User passes a dict of {col_name:val for col_name in db.cols}
        #          This will be majorly used.

        query = None
        if type(values) in [type([]), type(()), types.GeneratorType]:
            # adding only tuple, list and generator in options of iterables.

            # creating a base query with only one value.
            query = 'INSERT INTO {} VALUES ({}'.format(table_name, values.pop(0))
            for val in values:
                # adding all the other values in the query.
                query += ", " + val
            # terminating  the query after appending all the vals in the values with a semicolon.
            query += ');'

        elif type(values) == type({}):
            # user is not sure about the order of the cols in the db.

            if len(values) == 1:
                # if only one element is present in the table, order doesn't matter due to reflexive property.
                return self.add_to_table(table_name, [list(values.values())[0]])

            query = "INSERT INTO {}{} VALUES {}".format(
                table_name,
                tuple(values.keys()),
                tuple(values.keys())
            )
            print(query)
        else:
            raise NotImplementedError("Couldn't create row.")

        # we got a query to execute.
        connection = self.get_db_connection()
        connection.execute(query)
        connection.close()

    def __del__(self):
        # deleting the db when db object is deleted.
        os.remove(self.db_name)


class BLock:
    def __init__(self, data, prev_hash, timestamp):
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash(self.timestamp, self.)


class BlockChain:
    """
    This is a minimalistic blockchain implementation that uses sqlite3 database to operate.

    This approach doesn't include pow concept so that it enables user
    to upload files frequently for demonstration of the project in Pragati competition.
    """


    def __init__(self, db_name=None):
        self.genesis_block = None
        self.db_name = "rbc" if db_name is None else db_name  # rbc: Rishabh Bhatnagar's block chain.
        self.create_new_chain()
        self.db = DataBase(self.db_name)

    def create_new_chain(self, genesis_block_data=None):
        if genesis_block_data is None:
            genesis_block_data = "Rishabh Bhatnagar"
    def add_block(self, data, timestamp, prev_hash):
        self.data = data

    pass


bc = BlockChain()
bc.db.add_to_table("test", dict(a=12))
