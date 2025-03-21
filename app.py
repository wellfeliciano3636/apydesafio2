#-*- coding: utf-8 -*-

# from flask import Flask

# app = Flask(__name__)

#@app.route("/pagar")
#def exibei_mensagem():
#     return "<h1>Pagar as pessoas, faz bem as pessoas!!!</h1>"

#@app.route("/fenandapix")
#def manda_o_pix():
#      return "<h2>Se a tela apagou, tá devendo!!!</h2>"
     
#@app.route("/comida")
#def comida():
#     return "<h2>Tomato a milanesa</h2>"


# se o arquivo app.py for o arquivo principal da nossa aplocaçao, rode a api no modo de depuraçao
#if __name__ == "__main__":
#    app.run(debug=True)


#app.run()
# ----------------------------------------------------------------------------


import sqlite3  # Biblioteca para interagir com o banco de dados SQLite
from flask import Flask, request, jsonify  # Importamos Flask para criar a API e request/jsonify para manipular requisições e respostas

# Criamos a aplicação Flask
# O Flask precisa saber qual é o arquivo principal do programa, então passamos "_name_" como referência
app = Flask(__name__)

# Criamos uma rota para o endpoint "/femandaopix"
# Quando acessarmos http://127.0.0.1:5000/femandaopix, essa função será chamada automaticamente
@app.route("/femandaopix")
def manda_o_pix():
    # Quando o usuário acessar essa rota no navegador, ele verá essa mensagem HTML na tela
    # Essa mensagem será exibida como um cabeçalho de segundo nível (<h2>)
    return "<h2>SE TEM DOR DE CUTUVELO, TÁ DEVENDO</h2>"

# Função para inicializar o banco de dados SQLite
# Ela cria o banco de dados caso ele ainda não exista e garante que a estrutura esteja configurada corretamente

def init_db():
    # Abrimos uma conexão com o banco de dados "database.db"
    # O comando "with" garante que a conexão será fechada automaticamente após a execução
    with sqlite3.connect("database.db") as conn:
        # Criamos uma tabela chamada "LIVROS", caso ela ainda não exista
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    titulo TEXT NOT NULL, 
                    categoria TEXT NOT NULL, 
                    autor TEXT NOT NULL, 
                    image_url TEXT NOT NULL 
                )
            """
        ) 

init_db()

@app.route("/doar", methods=["POST"])
def doar():

    dados = request.get_json()
   # print(f" AQUI ESTÃO OS DADOS RETORNADOS DO CLIENTE {dados}")
 
    titulo = dados.get("titulo") 
    categoria = dados.get("categoria") 
    autor = dados.get("autor") 
    image_url = dados.get("image_url") 


    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400  
    

    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
            INSERT INTO LIVROS (titulo, categoria, autor, image_url)
            VALUES ('{titulo}', '{categoria}', '{autor}', '{image_url}')
            """) 
        
        conn.commit()

        return jsonify({"mensagem": "Livro cadastrado com sucesso"}), 201

@app.route("/livros", methods=["GET"])
def lista_livros():

    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("SELECT * FROM LIVROS")

        livros_formatados = []

        for item in livros:
            dicionario_livros ={
                "id":item[0],
                "titulo":item[1],
                "categoria":item[2],
                "autor":item[3],
                "image_url":item[4],
            }
        livros_formatados.append(dicionario_livros)
    

    return jsonify(livros_formatados),200
    

if __name__ == "__main__":
    app.run(debug=True)

