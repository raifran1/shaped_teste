# Teste

Para realizar o teste primeiro siga os passos abaixo para rodar o projeto.

## Criando um Ambiente Virtual Python e Instalando os Requisitos

### Passo 1: Instale o virtualenv

Se você ainda não tem o virtualenv instalado, pode instalá-lo usando o pip. Abra uma janela do terminal e execute o seguinte comando:

```bash
pip install virtualenv
```

### Passo 2: Crie um ambiente virtual

Navegue até o diretório raiz do seu projeto no seu terminal e execute o seguinte comando:

```bash
virtualenv venv
```

### Passo 3: Ative o ambiente virtual

Antes de poder usar o ambiente virtual, você precisa ativá-lo. Para fazer isso, execute o seguinte comando:

```bash
source venv/bin/activate
```

### Passo 4: Instale os requisitos

Com o ambiente virtual ativo, você pode agora instalar os pacotes necessários usando o arquivo requirements.txt.

```bash
pip install -r requirements.txt
```

### Passo 5: Rodando o Serviço

Com o ambiente virtual ativo, e com pacotes instalados agora é só rodar o serviço.

```bash
python manage.py runserver
```

### Passo 6: Rodando os Testes

Com o ambiente virtual ativo, e com pacotes instalados agora é só rodar o serviço.

```bash
python manage.py test
```

## Sobre as atualizações (Resumo)

### Paginação da lista de noticias

Foi configurado a paginação padrão do Django Rest Framework, baseado no parâmetro 'page' para navegar entre as páginas.
Por padrão no settings configuramos 100 resultados para a primeira página

### Nova api para gerar um link temporário para acessar dados de alguma matéria

Existem dois endpoints que são descritos abaixo:

#### POST
 `/api/link/` - Recebe um JSON no formato `{ "news_pk": <id> }` onde `<id>` vai ser o id da matéria a ser gerado o link

#### GET
`/api/link/<code_link>/` - Esse método recebe um código em sua url em que caso esteja válido e existente irá retornar o obj de uma notícia

