Para conseguir inicializar a aplicacão, siga os seguintes passos:

1 - Abra o terminal da sua IDE.

2 - <b>Crie um ambiente virtual</b> na pasta da aplicacão com o código: <b>`python -m venv venv`</b> (útil para isolar a aplicacão do computador no geral, evitando possíveis bugs)

3 - <b>Ative o ambiente virtual</b> com o código: <b>`.\venv\Scripts\activate`</b>

4 - <b>Instale as dependencias necessárias</b> com o código: <b>`pip install flask flask-cors sqlite3`</b>. Caso ocorra algum erro, instale-as separadamente, ex: pip install flask, pip install flask-cors, pip install sqlite3. 

5 - Igualmente, <b>inicialize o banco de dados</b> com o código: <b>`python inicializar.py`</b>.

6 - Outrossim, <b>inicialize o arquivo principal</b> com o código: <b>`python main.py`</b>.

7 - <b>Entre no seu navegador e digite na barra de URL's</b> o seguinte link: <b>`http://127.0.0.1:5000`</b>.
<br>
<br>
<br>
Para sair da aplicacão, siga os seguintes passos:
<br>
<br>
1 - <b>Para parar a aplicacão</b>, aperte: <b>`Ctrl` + `C`</b> no terminal.
<br>
<br>
2 - <b>Para sair do ambiente virtual</b>, digite <b>`deactivate`</b>.
