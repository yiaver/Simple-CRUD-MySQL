from Connect import Connect

class Delete(Connect):
    def __init__(self) -> None:
        super().__init__()

    def deleteTable(self,table:str) ->bool:
        try:
            cursor = self.__connection.cursor()
            cursor.execute(f"DROP TABLE {table};")
            cursor.close()
            return True

        except Exception as log:
            with open("log.txt","w") as file:
                file.write(f"Delete , deleteTable: \n{'*'*100}\n\n{log}\n\n{'*'*100}")
            raise log
    
    def deleteRow(self,table:str,where:str) ->bool:
        try:
            cursor = self.__connection.cursor()
            cursor.execute(f"DELETE FROM {table} WHERE {where};")
            cursor.close()
            return True

        except Exception as log:
            with open("log.txt","w") as file:
                file.write(f"Delete , deleteRow: \n{'*'*100}\n\n{log}\n\n{'*'*100}")
            raise log

    def TruncateTable(self,table:str):
        try:
            cursor = self.__connection.cursor()
            cursor.execute(f"DELETE FROM {table};")
            cursor.close()
            return True

        except Exception as log:
            with open("log.txt","w") as file:
                file.write(f"Delete , TruncateTable: \n{'*'*100}\n\n{log}\n\n{'*'*100}")
            raise log
