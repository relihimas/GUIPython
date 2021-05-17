import pyodbc
import pandas as pd
from cryptography.fernet import Fernet


class Acesso:
    def __init__(self):
        self.server = 'DESKTOP-5F7OCN9'
        self.database = 'Teste'
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
        paramsemail = (usuario, senha)
        self.cursor.execute(prcdcheckemail, paramsemail)
        rc = self.cursor.fetchval()
        self.cnxn.commit()
        self.cursor.close()
        return rc

    def cadastroUserLogin(self, usuario, senha, permissao):
        chave = Fernet.generate_key()
        usuario_encoded = usuario.encode("UTF-8")
        senha_encoded = senha.encode("UTF-8")
        cipher_suite = Fernet(chave)
        ciphered_user_text = cipher_suite.encrypt(usuario_encoded)
        ciphered_senha_text = cipher_suite.encrypt(senha_encoded)
        prcdcadastrologin = 'EXEC prcd_insertUser @varUser = ?, @varPsswrd = ?, @varPermissao = ?, @varKey = ?'
        paramslogin = (ciphered_user_text, ciphered_senha_text, permissao, chave)
        self.cursor.execute(prcdcadastrologin, paramslogin)
        self.cnxn.commit()
        self.cursor.close()
