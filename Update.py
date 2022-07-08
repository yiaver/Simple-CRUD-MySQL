from Connect import Connect

class Update(Connect):
    def __init__(self) -> None:
        super().__init__()

def updateTableValues(self,table:str,values:str,condition:str) -> bool:
    """
    Updates all values of a table in the range of the condition.
    """
    try:

        cursor = self.connection1.cursor()
        cursor.execute(f"UPDATE {table} SET {values} WHERE {condition};")
        print(f"Sucess!")
        cursor.close()
        return True

    except Exception as log:
            with open("log.txt","w") as file:
                file.write(f"Update , updateTableValues: \n{'*'*100}\n\n{log}\n\n{'*'*100}")
            raise log