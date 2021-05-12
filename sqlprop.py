import pyodbc
import pandas as pd

class Acesso:
    def __init__(self):
        self.server = '#####'
        self.database = '#####'
        self.username = ''
        self.password = ''
        self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.cnxn.cursor()

    def enviousuario(self, nome, endereco, cidade, companhia, data):
        self.cursor.execute("INSERT INTO Usuario (Nome, Endereço, Cidade, Companhia, DTCadastro) values(?, ?, ? ,? ,?)",
                                    nome, endereco, cidade, companhia, data)
        self.cnxn.commit()
        self.cursor.close()

    def procedure_cadastrousuario(self, nome, endereco, cidade, companhia, data):
        prcdcadastrousuario = 'EXEC prcd_cadastrousuario @varNome = ?, @varEndereco = ?, @varCidade = ?, @varCompanhia = ?, @varData = ?;'
        params = (nome, endereco, cidade, companhia, data)
        self.cursor.execute(prcdcadastrousuario, params)
        self.cnxn.commit()
        self.cursor.close()

    def checklogin(self, usuario, senha):
        prcdcheckemail = 'EXEC prcd_checagemEmail @varUsuario = ?, @varSenha = ?'
        paramsemail = ("rachid", "12345")
        self.cursor.execute(prcdcheckemail, paramsemail)
        rc = self.cursor.fetchval()
        self.cnxn.commit()
        self.cursor.close()
        return rc

# envio = Acesso()
# envio.checklogin("rachid", "12345")


# def envioclientetipo(self, nome, endereco, cidade, companhia, data):
#     for index, row in self.arq.iterrows():
#         self.cursor.execute(
#             "INSERT INTO clienteTipo (Nome, Endereço, Cidade, Companhia, DTCadastro) values(?, ?, ? ,? ,?)",
#             row.Nome, row.Endereço, row.Cidade, row.Companhia, row.Data)
#     self.cnxn.commit()
#     self.cursor.close()
