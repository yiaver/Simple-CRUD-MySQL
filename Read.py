from Connect import Connect

class Read(Connect):
    def __init__(self) -> None:
        super().__init__()

def viewAllTables(self) -> None:
        """
        Show all Tables from a DataBase.
        """
        cursor = self.connection1.cursor()
        cursor.execute("SHOW TABLES;")
        result = [x[0] for x in cursor.fetchall()]
        return result

def readOnlyColumns(self,table:str) -> dict:
    """
    Read all columns names and types of a table.
    """
    try:
        cursor = self.connection1.cursor()
        cursor.execute(f"SHOW COLUMNS FROM {table};")
        rawcolumns = [x for x in cursor.fetchall()]
        columns = [x[0] for x in rawcolumns]
        cursor.close()
        return {"columns":columns,"rawColumns":rawcolumns}
    except Exception as log:
            with open("log.txt","w") as file:
                file.write(f"Read , readOnlyColumns: \n{'*'*100}\n\n{log}\n\n{'*'*100}")
            raise log

def read(self,table:str,columns:str,**kwargs) -> list:
    """
    Reads content of all selected columns of a table.

    You may use the kwarg where="condtions" to set WHERE conditions.
    """
    try:
        if kwargs.get("where"):
                cursor = self.connection1.cursor()
                condition = kwargs.get("where")
                cursor.execute(f"SELECT {columns}  FROM {table} WHERE {condition};")
                result = cursor.fetchall()
                cursor.close()
                return result

        cursor = self.connection1.cursor()
        cursor.execute(f"SELECT {columns} FROM {table};")
        result = cursor.fetchall()
        cursor.close()
        return result

    except Exception as log:
            with open("log.txt","w") as file:
                file.write(f"Read , read: \n{'*'*100}\n\n{log}\n\n{'*'*100}")
            raise log