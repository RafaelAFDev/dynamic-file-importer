<h2><b>Dynamic File Importer</b></h2>
O Dynamic File Importer é um projeto desenvolvido em Python que permite importar arquivos para bancos de dados de forma dinâmica, utilizando a biblioteca Polars.

<h3><b>Requisitos</b></h3>
Antes de utilizar o Dynamic File Importer, certifique-se de que o seu ambiente de desenvolvimento possui:

Python 3.7 (Ou superior)</br>
Biblioteca Polars</br>
Biblioteca compatível com o servidor SQL que receberá os dados</br>

<h3><b>Utilização</b></h3>
Para utilizar o Dynamic File Importer, siga os seguintes passos:</br>

Baixe o código fonte do projeto.</br>
Com base no arquivo config.json, atualize os parâmetros conforme o desejado. A seguir as descrições de cada parâmetro:

<b>conn_string</b>: String de conexão com o servidor que receberá os dados, padrão Sqlalchemy</br>
<b>files</b>: Objeto dict que receberá um ou mais objetos dicts contendo os parâmetros próprios de cada arquivo a ser importado</br>
<b>file1</b>: Objeto dict que receberá os parâmetros próprios do arquivo a ser importado</br>
<b>path</b>: Diretório do arquivo a ser importado, aceita padrão glob</br>
<b>sheet_name</b>: Nome da guia a ser importada, somente para casos de bases em Excel</br>
<b>separator</b>: Define o delimitador de texto, para arquivo txt e csv</br>
<b>quote_char</b>: Define o caractere utilizado para encapsulamento dos campos em arquivos txt e csv</br>
<b>encoding</b>: Define o encoding do arquivo a ser importado</br>
<b>skip_header</b>: Define a quantidade de linhas a serem desconsideradas caso o arquivo contenha um cabeçalho</br>
<b>skip_footer</b>: Define a quantidade de linhas a serem desconsideradas caso o arquivo contenha um rodapé</br>
<b>fields</b>: Objeto dict que receberá os nomes das colunas no arquivo e na tabela de destino, preenchimento padrão "NomeDaColunaNoArquivo": "NomeDaColunaCorrespondenteNaTabelaSQL"
<b>file_required</b>: Define se é obrigatória a existência do arquivo a cada execução com os preenchimentos "yes" ou "no". Em caso de obrigatoriedade, o script retornará erro se o arquivo não existir no diretório informado, caso contrário apenas será ignorada sua ausência</br>
<b>target_table</b>: Define o nome da tabela que armazenará os dados importados</br>
<b>delete_file</b>: Define se o arquivo será deletado após a importação dos dados com os preenchimentos "yes" ou "no"</br>
<b>move_file</b>: Define o diretório de destino do arquivo após a importação dos dados. Caso não queira movimentar o arquivo basta manter o parâmetro vazio</br>

Execute o arquivo main.py informando o caminho para o arquivo config.json, como no exemplo abaixo:
python main.py --config /caminho/para/o/arquivo/config.json

<h3><b>Arquivos</b></h3>
O projeto Dynamic File Importer é composto pelos seguintes arquivos:</br>

<b>main.py</b>: arquivo principal do projeto, que importa os arquivos e realiza a inserção no banco de dados.</br>
<b>config/__init__.py</b>: arquivo responsável por ler o arquivo config.json.</br>
<b>filehandler/__init__.py</b>: arquivo que contém a classe FileHandler, responsável por realizar a leitura dos arquivos e a inserção no banco de dados.</br>
<b>config.json</b>: arquivo que contém as configurações para importação dos arquivos.

<h3><b>Considerações finais</b></h3>
O Dynamic File Importer é um projeto simples e fácil de utilizar, que pode ser facilmente adaptado para atender às necessidades de diferentes projetos. Se você tiver alguma dúvida ou sugestão de melhoria, sinta-se à vontade para entrar em contato com o autor do projeto.