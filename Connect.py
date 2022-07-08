import mysql.connector
from mysql.connector import errorcode
import json

with open("info.json","r") as file:
    inform = json.load(file)

class Connect:
    infoConnection = f'[*]Conecting in :\n[+]Host : {inform["Host"]}\n[+]User : {inform["Username"]}\n[+]DataBase : {inform["DataBase"]}\n'
    def __init__(self) -> None:
        try:
            print(self.infoConnection)

            self.__connection = mysql.connector.connect(
                host = inform["Host"],
                user = inform["Username"],
                password = inform["Password"],
                database = inform["DataBase"]
            )
            
            print("[+] Connected Successfully!\n")
        
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("[-]Something is wrong with your user name or password.")
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                print("[-]Database does not exist.")
            else:
                print(f"[-]{error}")
            
        except Exception as log:
            with open("log.txt","w") as file:
                file.write(f"INIT \n{'*'*100}\n\n{log}\n\n{'*'*100}")
            raise log
    @property
    def connection(self):
        return self.__connection