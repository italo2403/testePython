from PyQt5 import uic, QtWidgets
import mysql.connector
import sys

sql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cad"
)

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    print("Nome", linha1)
    print("Telefone", linha2)
    cursor = sql.cursor()
    entrada_Dados = "INSERT INTO cada(nome,fone) VALUES(%s,%s)"
    dados = (str(linha1), str(linha2))
    cursor.execute(entrada_Dados, dados)
    sql.commit()
    # criando o limpar após o dado ser inserido no banco
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")


def listando_segundatela():
    listar.show()  # Exibir a segunda tela

    cursor = sql.cursor()
    listar_Dados = "SELECT * FROM cada"
    cursor.execute(listar_Dados)
    dados_lidos = cursor.fetchall()
    listar.tableWidget.setRowCount(len(dados_lidos))
    listar.tableWidget.setColumnCount(3) # Corrigido o número de colunas para 2
    for i in range(0,len(dados_lidos)):
        for j in range(0,3): # Corrigido o número de colunas para 2
            listar.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
        

def fechar_aplicacao():
    sql.close()
    app.quit()


app = QtWidgets.QApplication(sys.argv)
formulario = uic.loadUi("formulario.ui")
# Importando a tela Listar
listar = uic.loadUi("listar.ui")
formulario.pushButton.clicked.connect(funcao_principal)
# Chamando a função para exibir a segunda tela
formulario.pushButton_2.clicked.connect(listando_segundatela)

formulario.show()

# Conectar evento de fechamento da janela
formulario.closeEvent = fechar_aplicacao

sys.exit(app.exec_())
