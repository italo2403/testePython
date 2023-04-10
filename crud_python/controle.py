from PyQt5 import uic,QtWidgets
import mysql.connector

sql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="cad"
    )

def funcao_principal():
    linha1=formulario.lineEdit.text()
    linha2=formulario.lineEdit_2.text()
    print("Nome",linha1)
    print("Telefone",linha2)
    cursor =sql.cursor()
    entrada_Dados = "INSERT INTO cada(nome,fone) VALUES(%s,%s)"
    dados = (str(linha1),str(linha2))
    cursor.execute(entrada_Dados,dados)
    sql.commit()


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
