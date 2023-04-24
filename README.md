<h2><b>Dynamic File Importer</b></h2></br>
O Dynamic File Importer é um projeto desenvolvido em Python que permite importar arquivos para bancos de dados de forma dinâmica, utilizando a biblioteca Polars.

Requisitos
Antes de utilizar o Dynamic File Importer, certifique-se de que o seu ambiente de desenvolvimento possui:

Python 3.7 (Ou superior)
Biblioteca Polars
Biblioteca compatível com o servidor SQL que receberá os dados

Utilização
Para utilizar o Dynamic File Handler, siga os seguintes passos:

Baixe o código fonte do projeto.

Com base no arquivo config.json, atualize os parâmetros conforme o desejado. A seguir as descrições de cada parÂmetro:

conn_string: String de conexão com o servidor que receberá os dados, padrão Sqlalchemy
files: Objeto dict que receberá um ou mais objetos dicts contendo os parâmetros próprios de cada arquivo a ser importado
file1: Objeto dict que receberá os parâmetros próprios do arquivo a ser importado
path: Diretório do arquivo a ser importado, aceita padrão glob
sheet_name: Nome da guia a ser importada, somente para casos de bases em Excel
separator: Define o delimitador de texto, para arquivo txt e csv
quote_char: Define o caractere utilizado para encapsulamento dos campos em arquivos txt e csv
encoding: Define o encoding do arquivo a ser importado
skip_header: Define a quantidade de linhas a serem desconsideradas caso o arquivo contenha um cabeçalho
skip_footer: Define a quantidade de linhas a serem desconsideradas caso o arquivo contenha um rodapé
fields: Objeto dict que receberá os nomes das colunas no arquivo e na tabela de destino, preenchimento padrão "NomeDaColunaNoArquivo": "NomeDaColunaCorrespondenteNaTabelaSQL"
file_required: Define se é obrigatória a existência do arquivo a cada execução com os preenchimentos "yes" ou "no". Em caso de obrigatoriedade, o script retornará erro se o arquivo não existir no diretório informado, caso contrário apenas será ignorada sua ausência.
target_table: Define o nome da tabela que armazenará os dados importados
delete_file: Define se o arquivo será deletado após a importação dos dados com os preenchimentos "yes" ou "no".
move_file: Define o diretório de destino do arquivo após a importação dos dados. Caso não queira movimentar o arquivo basta manter o parâmetro vazio

Execute o arquivo main.py informando o caminho para o arquivo config.json, como no exemplo abaixo:
python main.py --config /caminho/para/o/arquivo/config.json

Arquivos
O projeto Dynamic File Importer é composto pelos seguintes arquivos:

main.py: arquivo principal do projeto, que importa os arquivos e realiza a inserção no banco de dados.

config/__init__.py: arquivo responsável por ler o arquivo config.json.

filehandler/__init__.py: arquivo que contém a classe FileHandler, responsável por realizar a leitura dos arquivos e a inserção no banco de dados.

config.json: arquivo que contém as configurações para importação dos arquivos.

Considerações finais
O Dynamic File Importer é um projeto simples e fácil de utilizar, que pode ser facilmente adaptado para atender às necessidades de diferentes projetos. Se você tiver alguma dúvida ou sugestão de melhoria, sinta-se à vontade para entrar em contato com o autor do projeto.