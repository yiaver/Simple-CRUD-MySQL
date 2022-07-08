from Connect import Connect

class Create(Connect):
    def __init__(self) -> None:
        super().__init__()
    
    def createTable(self,**kwargs):
        """Needed kwargs :
        
        - name = "Name of your table "

        - columns = "name and especifications"

        Examples:
        + name = "MyTable"
        + columns = "id INT NOT NULL AUTO_INCREMENT, name VARCHAR (40) NOT NULL, age INT NOT NULL"
        """
        try:
            cursor = self.__connection.cursor()
            name = kwargs.get("name")
            columns = kwargs.get("columns")
            if name != None and columns != None:
                cursor.execute(f"CREATE TABLE {name} ({columns});")
                print(f"Sucessfully created the Table:{name} !")
                cursor.close()
                return True

        except Exception as log:
            with open("log.txt","w") as file:
                file.write(f"Create , createTable: \n{'*'*100}\n\n{log}\n\n{'*'*100}")
            raise log
    
    def createRow(self,**kwargs):
        """
        Needed kwargs :
        
        - table = "Name of existing table "

        - values = "Value for each column" 

        Examples:
        + table = "MyTable"
        + values = "'yiaver',21"

        ! if your table have a auto _increment id column you dont need to add a value for this column
        """

        try:
            cursor = self.__connection.cursor()
            table = kwargs.get("table")
            values = kwargs.get("values")
            if table != None and values != None:
                cursor.execute(f"INSERT INTO {table} VALUES ({values});")
                print(f"Addiction of Values: {values} in Table: {table} \nWas Sucessfully!")
                cursor.close()
                return True
            else:
                print("Missing kwarg!")
                return False
        
        except Exception as log:
            with open("log.txt","w") as file:
                file.write(f"Create , createRow:\n{'*'*100}\n\n{log}\n\n{'*'*100}")
            raise log
