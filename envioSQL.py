import pyodbc
import pandas as pd

class Acesso:
    def __init__(self):
        self.server = '#####'         #Database server
        self.database = '#####'       #Database
        self.username = ''
        self.password = ''
        self.arq = pd.read_excel(
            "C:\\Users\\Rachid Elihimas\\OneDrive - MGN - Gestão de Negócios\\Área de Trabalho\\Outros\\testeSSIS.xlsx")
        self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.cnxn.cursor()

    def envioclientetipo(self):
        for index, row in self.arq.iterrows():
            self.cursor.execute("INSERT INTO clienteTipo (Nome, Endereço, Cidade, Companhia, DTCadastro) values(?, ?, ? ,? ,?)",
                                    row.Nome, row.Endereço, row.Cidade, row.Companhia, row.Data)
        self.cnxn.commit()
        self.cursor.close()

envio = Acesso()
envio.envioclientetipo()
