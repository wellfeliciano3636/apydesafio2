# Api Livros Doados Vnw

Essa e uma API simples com flesk e SQlite para fin de estudo na escola Vai na Web, ela permite cadastrar os livros doados.

## Como rodar o projeto?

1. faça o clone do repositorio:
```bash
git clone <LINK_do_REPOSITORIO>
cd Nome_do_projeto
```

2. Criar um ambiente virtual (Obrigatório):

**Windows**
```bash
python -m venv venv
source venv/Scripts/activate
```

**Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Instale as dependencias:
```bash
pip install -r requirements.txt
```

4. Inicie o servidor:
```bash
python app.py
```
> A API estará disponível em http://127.0.0.1:5000/

### Endpoints

### POST /doar
 
endpoints para cadastro das informacoes do livro doado.

**Envio (json)**
```json
{
    "titulo":"Ainda estou devendo aqui",
    "categoria":"Drama",
    "Autor":"Fernanda",
    "image_url":"https://exemplo.com"
}
```