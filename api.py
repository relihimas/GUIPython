from flask import Flask, request
from consultadadosAPI import insertusuario


app = Flask("MGNDados")

@app.route("/olamundo", methods=["GET"])
def olamundo():
    return {"ola": "mundo"}

@app.route("/cadastro", methods=["POST"])
def cadastrousuario():
    body = request.get_json()

    usuario = insertusuario(body["nome"], body["email"], body["senha"])

    if("nome" not in body):
        return {"status": 400, "mensagem": "O parâmetro nome é obrigatório"}

    return response(200, "Usuario criado", "user", usuario)

def response(status, mensagem, nome_do_conteudo, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response

app.run()
