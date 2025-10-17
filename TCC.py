import mysql.connector
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QPainterPath
from PyQt5.QtCore import Qt
from datetime import datetime
# ===================== CONEXÃO =======================
def connect():
    return mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        port='3306',
        database='bd_tcc_g1s'
    )

# ===================== LOGIN =======================
def login():
    global menu

    email = login_window.txt_email.text()
    senha = login_window.txt_senha.text()

    conn = connect()
    cursor = conn.cursor()

    try:
        sql = f"SELECT * FROM tb_login WHERE email = '{email}' AND senha = '{senha}' AND tipo = 'adm'"
        cursor.execute(sql)
        resultado = cursor.fetchone() 

        if resultado:  
            menu = uic.loadUi("frm_menu_adm.ui")
            menu.btn_exercicios.clicked.connect(open_menu_ex)
            menu.btn_progresso.clicked.connect(open_prog)
            menu.btn_relatorios.clicked.connect(open_rela)
            menu.btn_pagamentos.clicked.connect(open_pag)
            menu.btn_usuarios.clicked.connect(open_menu_user)
            menu.btn_usuarios2.clicked.connect(open_menu_user)
            menu.btn_medicos.clicked.connect(open_menu_med)
            menu.btn_medicos2.clicked.connect(open_menu_med)
            menu.btn_voltar.clicked.connect(voltar_menu_user)
            menu.btn_sair.clicked.connect(voltar_login)
            
           
            menu.show()
            
        else:
            QMessageBox.critical(login_window, "Erro no Login", "Email ou senha incorretos.")

    except Exception as erro:
        QMessageBox.critical(login_window, "Erro", f"Ocorreu um erro: {erro}")
    finally:
        cursor.close()
        conn.close()


# ===================== ABRIR TELAS PRINCIPAIS =======================
# ===================== ABRIR TELAS PRINCIPAIS =======================
def open_pag():
    global menu_pag
    menu_pag = uic.loadUi("frm_pagamentos.ui")  # carrega a tela do Qt Designer

    # conecta os botões do menu
    
    menu_pag.btn_usuarios.clicked.connect(open_menu_user)
    menu_pag.btn_usuarios2.clicked.connect(open_menu_user)
    menu_pag.btn_medicos.clicked.connect(open_menu_med)
    menu_pag.btn_medicos2.clicked.connect(open_menu_med)
    menu_pag.btn_voltar.clicked.connect(voltar_menu_pag)
    menu_pag.btn_sair.clicked.connect(voltar_menu_pag)
    menu_pag.btn_pesquisar.clicked.connect(pesquisar_list_pagamento)
    carregar_tabela_pagamentos()
    menu_pag.show()
def open_config():
    global menu_config
    menu_config = uic.loadUi("frm_config.ui")

def open_rela():
    global menu_rela
    menu_rela = uic.loadUi("frm_relatorio_men.ui")

    plotar_grafico_plano(menu_rela.widget_grafico_up)
    plotar_grafico_grau(menu_rela.widget_grafico_pg)
    plotar_grafico_crescimento(menu_rela.widget_grafico_uc)

   
    menu_rela.btn_usuarios.clicked.connect(open_menu_user)
    menu_rela.btn_usuarios2.clicked.connect(open_menu_user)
    menu_rela.btn_medicos.clicked.connect(open_menu_med)
    menu_rela.btn_medicos2.clicked.connect(open_menu_med)
    menu_rela.btn_sair.clicked.connect(voltar_menu_rela)
    menu_rela.btn_voltar.clicked.connect(voltar_menu_rela)
    menu_rela.show()
def open_prog():
    global menu_prog
    menu_prog = uic.loadUi("frm_progresso.ui")
    carregar_tabela_progresso()
   
    menu_prog.btn_usuarios.clicked.connect(open_menu_user)
    menu_prog.btn_usuarios2.clicked.connect(open_menu_user)
    menu_prog.btn_medicos.clicked.connect(open_menu_med)
    menu_prog.btn_medicos2.clicked.connect(open_menu_med)
    menu_prog.btn_voltar.clicked.connect(voltar_menu_prog)
    menu_prog.btn_sair.clicked.connect(voltar_menu_prog)
    menu_prog.btn_pesquisar.clicked.connect(pesquisar_tabela_progresso)
    menu_prog.tb_progresso.horizontalHeader().sectionDoubleClicked.connect(ajustar_largura_coluna_prog)
    menu_prog.show()
def open_menu_user():
    global menu_user
    menu_user = uic.loadUi("frm_usuarios.ui")
    carregar_tabela_usuarios()
    menu_user.tb_user.horizontalHeader().sectionDoubleClicked.connect(ajustar_largura_coluna_user)
    
    menu_user.btn_usuarios.clicked.connect(open_menu_user)
    menu_user.btn_usuarios2.clicked.connect(open_menu_user)
    menu_user.btn_medicos.clicked.connect(open_menu_med)
    menu_user.btn_medicos2.clicked.connect(open_menu_med)
    menu_user.btn_voltar.clicked.connect(voltar_menu_user)
    menu_user.btn_sair.clicked.connect(voltar_menu_user)
    menu_user.btn_pesquisar.clicked.connect(pesquisar_list_user)
    menu_user.show()
def open_menu_med():
    global menu_med
    menu_med = uic.loadUi("frm_medicos.ui")  
   
    menu_med.btn_usuarios.clicked.connect(open_menu_user)
    menu_med.btn_usuarios2.clicked.connect(open_menu_user)
    menu_med.btn_medicos.clicked.connect(open_menu_med)
    menu_med.btn_medicos2.clicked.connect(open_menu_med)
    menu_med.btn_cadastro.clicked.connect(open_cad_med)
    menu_med.btn_listagem.clicked.connect(open_list_med)
    menu_med.btn_voltar.clicked.connect(voltar_menu_med)
    menu_med.btn_sair.clicked.connect(voltar_menu_med)
    menu_med.show()
# ===================== MÉDICOS =======================
def open_list_med():
    global menu_med_list
    menu_med_list = uic.loadUi("frm_listagem_medicos.ui")
    carregar_tabela_medicos()
    menu_med_list.tb_medicos.horizontalHeader().sectionDoubleClicked.connect(ajustar_largura_coluna_med)
    
    menu_med_list.btn_usuarios.clicked.connect(open_menu_user)
    menu_med_list.btn_usuarios2.clicked.connect(open_menu_user)
    menu_med_list.btn_medicos.clicked.connect(open_menu_med)
    menu_med_list.btn_medicos2.clicked.connect(open_menu_med)
    menu_med_list.btn_voltar.clicked.connect(voltar_menu_med_list)
    menu_med_list.btn_pesquisar.clicked.connect(pesquisar_list_med)
    menu_med_list.btn_sair.clicked.connect(voltar_menu_med_list)
    menu_med_list.show()

def open_cad_med():
    global menu_med_cad
    menu_med_cad = uic.loadUi("frm_cadastro_medicos.ui")
    
    menu_med_cad.btn_usuarios.clicked.connect(open_menu_user)
    menu_med_cad.btn_usuarios2.clicked.connect(open_menu_user)
    menu_med_cad.btn_medicos.clicked.connect(open_menu_med)
    menu_med_cad.btn_medicos2.clicked.connect(open_menu_med)
    menu_med_cad.btn_voltar.clicked.connect(voltar_menu_med_cad)
    menu_med_cad.btn_enviar.clicked.connect(insert_medico)
    menu_med_cad.btn_foto.clicked.connect(carregar_foto)
    menu_med_cad.btn_editar.clicked.connect(editar_medico)
    menu_med_cad.btn_excluir.clicked.connect(excluir_medico)
    menu_med_cad.btn_pesquisar.clicked.connect(buscar_medico)
    menu_med_cad.btn_sair.clicked.connect(voltar_menu_med_cad)
    menu_med_cad.show()
# ===================== EXERCÍCIOS =======================
def open_menu_ex():
    global menu_ex_window
    menu_ex_window = uic.loadUi("frm_menu_exercicios.ui")
    
    menu_ex_window.btn_usuarios.clicked.connect(open_menu_user)
    menu_ex_window.btn_usuarios2.clicked.connect(open_menu_user)
    menu_ex_window.btn_medicos.clicked.connect(open_menu_med)
    menu_ex_window.btn_medicos2.clicked.connect(open_menu_med)
    menu_ex_window.btn_voltar.clicked.connect(voltar_menu_ex)
    menu_ex_window.btn_add_exercicio.clicked.connect(open_add_exercicio)
    menu_ex_window.btn_edit_exercicio.clicked.connect(open_edit_exercicio)
    menu_ex_window.btn_listagem_exercicio.clicked.connect(open_list_exercicio)
    menu_ex_window.btn_sair.clicked.connect(voltar_menu_ex) 
    menu_ex_window.show()
def open_add_exercicio():
    global add_window
    add_window = uic.loadUi("frm_add_exercicios.ui")
    
    add_window.btn_usuarios2.clicked.connect(open_menu_user)
    add_window.btn_medicos2.clicked.connect(open_menu_med)
    
    add_window.btn_usuarios.clicked.connect(open_menu_user)
    add_window.btn_medicos.clicked.connect(open_menu_med)
    add_window.btn_enviar.clicked.connect(insert_exercicio)
    add_window.btn_voltar.clicked.connect(voltar_menu_add)
    add_window.btn_aqv.clicked.connect(up_aqv)
    add_window.btn_foto.clicked.connect(carregar_foto_ex)
    add_window.btn_sair.clicked.connect(voltar_menu_add)
    add_window.show()

def open_edit_exercicio():
    global edit_window
    edit_window = uic.loadUi("frm_edit_exercicios.ui")
    
    edit_window.btn_usuarios2.clicked.connect(open_menu_user)
    edit_window.btn_medicos2.clicked.connect(open_menu_med)
    
    edit_window.btn_usuarios.clicked.connect(open_menu_user)
    edit_window.btn_medicos.clicked.connect(open_menu_med)
    edit_window.btn_pesquisar.clicked.connect(pesquisar_exercicio)
    edit_window.btn_salvar.clicked.connect(update_exercicio)
    edit_window.btn_excluir.clicked.connect(delete_exercicio)
    edit_window.btn_voltar.clicked.connect(voltar_menu_edit)
    edit_window.btn_aqv.clicked.connect(up_aqve)
    edit_window.btn_foto.clicked.connect(carregar_foto_exe)
    edit_window.btn_sair.clicked.connect(voltar_menu_edit)

    edit_window.show()

def open_list_exercicio():
    global list_window
    list_window = uic.loadUi("frm_list_exercicios.ui")
    carregar_tabela_exercicios()
    
    list_window.btn_usuarios.clicked.connect(open_menu_user)
    list_window.btn_medicos.clicked.connect(open_menu_med)
    
    list_window.btn_usuarios2.clicked.connect(open_menu_user)
    list_window.btn_medicos2.clicked.connect(open_menu_med)
    list_window.btn_voltar.clicked.connect(voltar_menu_list)
    list_window.btn_pesquisar.clicked.connect(pesquisar_list_exercicio)
    list_window.tableExercicios.horizontalHeader().sectionDoubleClicked.connect(ajustar_largura_coluna_ex)
    list_window.btn_sair.clicked.connect(voltar_menu_list)
    list_window.show()


# ===================== VOLTAR =======================
def voltar_login(): menu.hide()
def voltar_menu_pag(): menu_pag.hide()
def voltar_menu_ex(): menu_ex_window.hide()
def voltar_menu_add(): add_window.hide()
def voltar_menu_edit(): edit_window.hide()
def voltar_menu_list(): list_window.hide()
def voltar_menu_user(): menu_user.hide()
def voltar_menu_med(): menu_med.hide()
def voltar_menu_med_list(): menu_med_list.hide()
def voltar_menu_med_cad(): menu_med_cad.hide()
def voltar_menu_prog(): menu_prog.hide()
def voltar_menu_rela(): menu_rela.hide()

# ===================== FUNÇÕES DE TIPOS =======================
def pegar_tipos(widget):
    tipos = []
    if widget.cb_comunicacao.isChecked(): tipos.append("Comunicação")
    if widget.cb_vocabulario.isChecked(): tipos.append("Vocabulário")
    if widget.cb_raciocinio.isChecked(): tipos.append("Raciocínio")
    if widget.cb_memoria.isChecked(): tipos.append("Memória")
    if widget.cb_autonomia.isChecked(): tipos.append("Autonomia")
    if widget.cb_interacao.isChecked(): tipos.append("Interação Social")
    if widget.cb_coordenacao.isChecked(): tipos.append("Coordenação")
    if widget.cb_percepcao.isChecked(): tipos.append("Percepção")
    if widget.cb_rotina.isChecked(): tipos.append("Rotinas")
    if widget.cb_decisao.isChecked(): tipos.append("Decisão")
    return ",".join(tipos)

def apagar_tipos(widget):
    widget.cb_comunicacao.setChecked(False)
    widget.cb_vocabulario.setChecked(False)
    widget.cb_raciocinio.setChecked(False)
    widget.cb_memoria.setChecked(False)
    widget.cb_autonomia.setChecked(False)
    widget.cb_interacao.setChecked(False)
    widget.cb_coordenacao.setChecked(False)
    widget.cb_percepcao.setChecked(False)
    widget.cb_rotina.setChecked(False)
    widget.cb_decisao.setChecked(False)

# ===================== UPLOAD DE ARQUIVOS =======================
def up_aqv():
    file_path, _ = QFileDialog.getOpenFileName(add_window, "Selecionar Arquivo", "", 
        "Todos os Arquivos (*);;PDF (*.pdf);;Imagens (*.png *.jpg *.jpeg);;Vídeos (*.mp4)")
    if file_path:
        add_window.txt_upaqv.setText(file_path)

def up_aqve():
    file_path, _ = QFileDialog.getOpenFileName(edit_window, "Selecionar Arquivo", "", 
        "Todos os Arquivos (*);;PDF (*.pdf);;Imagens (*.png *.jpg *.jpeg);;Vídeos (*.mp4)")
    if file_path:
        edit_window.txt_upaqv.setText(file_path)

# ===================== CRUD: EXERCÍCIOS =======================
def insert_exercicio():
    nome = add_window.txt_nome.text()
    grau = add_window.cmb_grau.currentText()
    upload = add_window.txt_upaqv.text()
    link = add_window.txt_link.text()
    tipos = pegar_tipos(add_window)
    foto = add_window.caminho_foto if hasattr(add_window, 'caminho_foto') else None

    if not nome or not grau or not tipos:
        QMessageBox.warning(add_window, "Campos obrigatórios", "Preencha todos os campos obrigatórios antes de continuar.")
        return
    if not upload and not link:
        QMessageBox.warning(add_window, "Escolha obrigatória", "Escolha ao menos um: upload de arquivo ou link.")
        return

    if foto:
        with open(foto, 'rb') as arq:
            foto_bin = arq.read()
    else:
            foto_bin = None                              
    try:
        conn = connect()
        cursor = conn.cursor()
        sql = "INSERT INTO tb_exercicios (nome, grau, tipos, arquivo, link, foto) VALUES (%s,%s,%s,%s,%s,%s)"
        
        cursor.execute(sql,(nome,grau,tipos,upload,link,foto_bin))
        conn.commit()
        QMessageBox.information(add_window, "Sucesso", "Exercício cadastrado com sucesso!")
        add_window.txt_nome.clear()
        add_window.txt_upaqv.clear()
        add_window.txt_link.clear()
        add_window.lbl_foto.clear()

        apagar_tipos(add_window)
    except Exception as erro:
        QMessageBox.critical(add_window, "Erro", f"Erro ao inserir dados:\n{erro}")
    finally:
        cursor.close()
        conn.close()

def pesquisar_exercicio():
    id = edit_window.txt_pesquisar.text()
    try:
        conn = connect()
        cursor = conn.cursor()
        sql = "SELECT nome, grau, tipos, arquivo, link, foto FROM tb_exercicios WHERE id_ex = %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        if resultado:
            nome, grau, tipos, arquivo, link, foto_bin = resultado
            edit_window.txt_nome.setText(nome)
            edit_window.cmb_grau.setCurrentText(grau)
            edit_window.txt_upaqv.setText(arquivo)
            edit_window.txt_link.setText(link)

            # Tipos
            tipo_lista = tipos.split(",")
            checkboxes = {
                "Comunicação": edit_window.cb_comunicacao,
                "Vocabulário": edit_window.cb_vocabulario,
                "Raciocínio": edit_window.cb_raciocinio,
                "Memória": edit_window.cb_memoria,
                "Autonomia": edit_window.cb_autonomia,
                "Interação Social": edit_window.cb_interacao,
                "Coordenação": edit_window.cb_coordenacao,
                "Percepção": edit_window.cb_percepcao,
                "Rotinas": edit_window.cb_rotina,
                "Decisão": edit_window.cb_decisao,
            }
            for nome_tipo, checkbox in checkboxes.items():
                checkbox.setChecked(nome_tipo in tipo_lista)

            # Foto
            if foto_bin:
                from PyQt5.QtGui import QPixmap
                from PyQt5.QtCore import QByteArray
                from PyQt5.QtWidgets import QLabel

                pixmap = QPixmap()
                pixmap.loadFromData(foto_bin)
                edit_window.lbl_foto.setPixmap(pixmap.scaled(150, 150))  # ajusta tamanho
            else:
                edit_window.lbl_foto.clear()
        else:
            QMessageBox.information(edit_window, "Não encontrado", "Exercício não encontrado.")
    except Exception as erro:
        QMessageBox.critical(edit_window, "Erro", f"Erro na pesquisa:\n{erro}")
    finally:
        cursor.close()
        conn.close()


def update_exercicio():
    id = edit_window.txt_pesquisar.text()
    nome = edit_window.txt_nome.text()
    grau = edit_window.cmb_grau.currentText()
    upload = edit_window.txt_upaqv.text()
    link = edit_window.txt_link.text()
    tipos = pegar_tipos(edit_window)

    # Foto nova (se o usuário escolher)
    if hasattr(edit_window, 'caminho_foto') and edit_window.caminho_foto:
        with open(edit_window.caminho_foto, 'rb') as arq:
            foto_bin = arq.read()
    else:
        foto_bin = None  # Mantém a mesma do banco

    try:
        conn = connect()
        cursor = conn.cursor()

        if foto_bin:
            sql = """UPDATE tb_exercicios 
                     SET nome=%s, grau=%s, tipos=%s, arquivo=%s, link=%s, foto=%s 
                     WHERE id_ex = %s"""
            cursor.execute(sql, (nome, grau, tipos, upload, link, foto_bin, id))
        else:
            sql = """UPDATE tb_exercicios 
                     SET nome=%s, grau=%s, tipos=%s, arquivo=%s, link=%s 
                     WHERE id_ex = %s"""
            cursor.execute(sql, (nome, grau, tipos, upload, link, id))

        conn.commit()
        QMessageBox.information(edit_window, "Sucesso", "Exercício atualizado com sucesso!")
    except Exception as erro:
        QMessageBox.critical(edit_window, "Erro", f"Erro ao atualizar:\n{erro}")
    finally:
        cursor.close()
        conn.close()

def delete_exercicio():
    id = edit_window.txt_pesquisar.text()
    try:
        conn = connect()
        cursor = conn.cursor()
        sql = f"DELETE FROM tb_exercicios WHERE id_ex = '{id}'"
        cursor.execute(sql)
        conn.commit()
        edit_window.txt_pesquisar.clear()
        edit_window.txt_nome.clear()
        edit_window.cmb_grau.clear()
        edit_window.txt_upaqv.clear()
        edit_window.txt_link.clear()
        apagar_tipos(edit_window)
        QMessageBox.information(edit_window, "Sucesso", "Exercício deletado com sucesso!")
    except Exception as erro:
        QMessageBox.critical(edit_window, "Erro", f"Erro ao deletar:\n{erro}")
    finally:
        cursor.close()
        conn.close()

# ===================== LISTAGEM =======================
def carregar_tabela_progresso():
    try:
        conn = connect()
        cursor = conn.cursor()
        sql = """
        SELECT p.id_user, u.nome, u.sobrenome, p.id_ex, p.autonomia
        FROM tb_user u
        JOIN tb_progresso p ON p.id_user = u.id_user
        WHERE 1=1 """

        cursor.execute(sql)
        resultado = cursor.fetchall()

        menu_prog.tb_progresso.setRowCount(len(resultado))
        menu_prog.tb_progresso.setColumnCount(5)
        menu_prog.tb_progresso.setHorizontalHeaderLabels(["ID", "NOME", "SOBRENOME", "EXERCICIO",  "AUTONOMIA"])

        for row, dados in enumerate(resultado):
            for col, valor in enumerate(dados):
                item = QtWidgets.QTableWidgetItem(str(valor))
                menu_prog.tb_progresso.setItem(row, col, item)

    except Exception as erro:
        QMessageBox.critical(menu_prog, "Erro", f"Erro ao carregar tabela:\n{erro}")
    finally:
        cursor.close()
        conn.close()
def pesquisar_tabela_progresso():
    id_user = menu_prog.txt_id_user.text().strip()
    id_ex = menu_prog.txt_id_ex.text().strip()
    nome = menu_prog.txt_nome.text().strip()
    autonomia = menu_prog.cmb_auto.currentText()

    try:
        conn = connect()
        cursor = conn.cursor()
        sql = """
        SELECT p.id_user, u.nome, u.sobrenome, p.id_ex, p.autonomia
        FROM tb_user u
        JOIN tb_progresso p ON p.id_user = u.id_user
        WHERE 1=1
        """

        if id_user:
            sql += f" AND p.id_user = '{id_user}'"
        if id_ex:
            sql += f" AND p.id_ex = '{id_ex}'"
        if nome:
            sql += f" AND u.nome LIKE '%{nome}%'"
        if autonomia and autonomia != "Todos":
            sql += f" AND p.autonomia = '{autonomia}'"

        cursor.execute(sql)
        resultados = cursor.fetchall()

        menu_prog.tb_progresso.setRowCount(0)
        menu_prog.tb_progresso.setColumnCount(5)
        menu_prog.tb_progresso.setHorizontalHeaderLabels(
            ["ID", "NOME", "SOBRENOME", "EXERCICIO", "AUTONOMIA"]
        )

        for row_num, row_data in enumerate(resultados):
            menu_prog.tb_progresso.insertRow(row_num)
            for col_num, valor in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(valor))
                menu_prog.tb_progresso.setItem(row_num, col_num, item)

        if not resultados:
            QMessageBox.information(menu_prog, "Nenhum resultado", "Nenhum progresso encontrado.")

    except Exception as erro:
        QMessageBox.critical(menu_prog, "Erro", f"Erro na pesquisa:\n{erro}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()

#=====================PAGAMENTOS============================
import os, sys, subprocess
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui     
class ActionButtonsWidget(QtWidgets.QWidget):
    def __init__(self, id_pagamento, caminho_comprovante, parent=None):
        super(ActionButtonsWidget, self).__init__(parent)

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(4)
        layout.setAlignment(QtCore.Qt.AlignCenter)

        # Botões
        self.ver_pdf_button = QtWidgets.QPushButton("📄")
        self.aprovar_button = QtWidgets.QPushButton("✅")
        self.negar_button = QtWidgets.QPushButton("❌")

        button_size = QtCore.QSize(22, 22)
        for btn in (self.ver_pdf_button, self.aprovar_button, self.negar_button):
            btn.setFixedSize(button_size)
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            layout.addWidget(btn, alignment=QtCore.Qt.AlignCenter)

        # Estilo base
        base_style = """
            QPushButton {
                border: none;
                border-radius: 6px;
                font-size: 8px;
                font-weight: bold;
                color: white;
            }
            QPushButton:hover { transform: scale(1.1); }
            QPushButton:pressed { transform: scale(0.95); }
        """

        self.ver_pdf_button.setStyleSheet(base_style + """
            QPushButton { background-color: #add8e6; }
            QPushButton:hover { background-color: #1976D2; }
        """)
        self.aprovar_button.setStyleSheet(base_style + """
            QPushButton { background-color: #88E788; }
            QPushButton:hover { background-color: #2E7D32; }
        """)
        self.negar_button.setStyleSheet(base_style + """
            QPushButton { background-color: #FF7F7F; }
            QPushButton:hover { background-color: #C62828; }
        """)

        # Conexões
        self.ver_pdf_button.clicked.connect(lambda: abrir_pdf(caminho_comprovante))
        self.aprovar_button.clicked.connect(lambda: aprovar_pagamento(id_pagamento))
        self.negar_button.clicked.connect(lambda: negar_pagamento(id_pagamento))

    def sizeHint(self):
        return QtCore.QSize(120, 40)

# ---------------------------
# Tela principal (menu_pag)
# ---------------------------

def carregar_tabela_pagamentos():
    try:
        conn = connect()
        cursor = conn.cursor()

        sql = """
        SELECT 
            p.id_pagamento, 
            p.id_user,
            p.valor,
            p.codigo_pix,
            p.status,
            c.caminho, 
            p.criado_em
        FROM tb_pagamentos p
        LEFT JOIN tb_comprovantes c ON p.id_pagamento = c.id_pagamento
        ORDER BY p.criado_em DESC
        """

        cursor.execute(sql)
        resultado = cursor.fetchall()

        menu_pag.tb_pagamentos.setRowCount(len(resultado))
        menu_pag.tb_pagamentos.setColumnCount(8)
        menu_pag.tb_pagamentos.setHorizontalHeaderLabels([
            "ID", "Usuário", "Valor", "Código PIX",
            "Status", "Comprovante", "Criado em", "AÇÕES"
        ])

        menu_pag.tb_pagamentos.horizontalHeader().setSectionResizeMode(
            7, QtWidgets.QHeaderView.ResizeToContents
        )

        for row, dados in enumerate(resultado):
            id_pagamento, id_user, valor, codigo_pix, status, caminho_comprovante, criado_em = dados

            menu_pag.tb_pagamentos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(id_pagamento)))
            menu_pag.tb_pagamentos.setItem(row, 1, QtWidgets.QTableWidgetItem(str(id_user)))
            menu_pag.tb_pagamentos.setItem(row, 2, QtWidgets.QTableWidgetItem(f"R$ {valor}"))
            menu_pag.tb_pagamentos.setItem(row, 3, QtWidgets.QTableWidgetItem(codigo_pix))
            menu_pag.tb_pagamentos.setItem(row, 4, QtWidgets.QTableWidgetItem(status))
            menu_pag.tb_pagamentos.setItem(row, 5, QtWidgets.QTableWidgetItem("Existe" if caminho_comprovante else "Não Existe"))
            menu_pag.tb_pagamentos.setItem(row, 6, QtWidgets.QTableWidgetItem(str(criado_em)))
            
            # Botões de ação
            action_buttons_widget = ActionButtonsWidget(id_pagamento, caminho_comprovante, menu_pag)

            if status.lower() != "pendente":
                action_buttons_widget.aprovar_button.setVisible(False)
                action_buttons_widget.negar_button.setVisible(False)

                action_buttons_widget.ver_pdf_button.setStyleSheet("""
                    QPushButton {
                        background-color: #9E9E9E;
                        color: white;
                        border: 10px solid #757575;
                        border-radius: 8px;
                        padding: 8px 12px;
                        font-weight: bold;
                        font-size: 12px;
                    }
                    QPushButton:hover {
                        background-color: #757575;
                    }
                """)

            menu_pag.tb_pagamentos.setCellWidget(row, 7, action_buttons_widget)
            menu_pag.tb_pagamentos.setRowHeight(row, 42)
    except Exception as erro:
        QMessageBox.critical(menu_pag, "Erro", f"Erro ao carregar tabela:\n{erro}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()
def pesquisar_list_pagamento():
    id_pagamento = menu_pag.txt_id_user_2.text().strip()
    id_user = menu_pag.txt_id_user.text().strip()
    status = menu_pag.cmb_tipo.currentText()
    plano = menu_pag.cmb_plano.currentText()

    try:
        conn = connect()
        cursor = conn.cursor()
        sql = """
        SELECT 
            p.id_pagamento, 
            p.id_user,
            p.valor,
            p.codigo_pix,
            p.status,
            c.caminho, 
            p.criado_em
        FROM tb_pagamentos p
        LEFT JOIN tb_comprovantes c ON p.id_pagamento = c.id_pagamento
        WHERE 1=1
        """

        if id_pagamento:
            sql += f" AND p.id_pagamento = '{id_pagamento}'"
        if id_user:
            sql += f" AND p.id_user = '{id_user}'"
        if status and status != "Todos":
            sql += f" AND p.status = '{status}'"
        if plano and plano != "Todos":
            sql += f" AND p.valor = '{plano}'"

        sql += " ORDER BY p.criado_em DESC"

        cursor.execute(sql)
        resultados = cursor.fetchall()

        menu_pag.tb_pagamentos.setRowCount(0)
        menu_pag.tb_pagamentos.setColumnCount(8)
        menu_pag.tb_pagamentos.setHorizontalHeaderLabels([
            "ID", "Usuário", "Valor", "Código PIX",
            "Status", "Comprovante", "Criado em", "AÇÕES"
        ])

        for row_num, dados in enumerate(resultados):
            id_pagamento, id_user, valor, codigo_pix, status, caminho_comprovante, criado_em = dados

            menu_pag.tb_pagamentos.insertRow(row_num)
            menu_pag.tb_pagamentos.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(id_pagamento)))
            menu_pag.tb_pagamentos.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(id_user)))
            menu_pag.tb_pagamentos.setItem(row_num, 2, QtWidgets.QTableWidgetItem(f"R$ {valor}"))
            menu_pag.tb_pagamentos.setItem(row_num, 3, QtWidgets.QTableWidgetItem(codigo_pix))
            menu_pag.tb_pagamentos.setItem(row_num, 4, QtWidgets.QTableWidgetItem(status))
            menu_pag.tb_pagamentos.setItem(row_num, 5, QtWidgets.QTableWidgetItem("Existe" if caminho_comprovante else "Não Existe"))
            menu_pag.tb_pagamentos.setItem(row_num, 6, QtWidgets.QTableWidgetItem(str(criado_em)))

            # Botões de ação
            action_buttons_widget = ActionButtonsWidget(id_pagamento, caminho_comprovante, menu_pag)

            if status.lower() != "pendente":
                action_buttons_widget.aprovar_button.setVisible(False)
                action_buttons_widget.negar_button.setVisible(False)

                action_buttons_widget.ver_pdf_button.setStyleSheet("""
                    QPushButton {
                        background-color: #9E9E9E;
                        color: white;
                        border: 1px solid #757575;
                        border-radius: 8px;
                        padding: 8px 12px;
                        font-weight: bold;
                        font-size: 12px;
                    }
                    QPushButton:hover {
                        background-color: #757575;
                    }
                """)

            menu_pag.tb_pagamentos.setCellWidget(row_num, 7, action_buttons_widget)

        if not resultados:
            QMessageBox.information(menu_pag, "Nenhum resultado", "Nenhum pagamento encontrado.")

    except Exception as erro:
        QMessageBox.critical(menu_pag, "Erro", f"Erro na pesquisa:\n{erro}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()

def aprovar_pagamento(id_pagamento):
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("UPDATE tb_pagamentos SET status='aprovado' WHERE id_pagamento=%s", (id_pagamento,))
        cursor.execute("SELECT id_user FROM tb_pagamentos WHERE id_pagamento=%s", (id_pagamento,))
        id_user = cursor.fetchone()[0]
        conn.commit()

        enviar_email_status(id_user, "aprovado")
        carregar_tabela_pagamentos()

    except Exception as erro:
        QMessageBox.critical(menu_pag, "Erro", f"Erro ao aprovar pagamento:\n{erro}")
    finally:
        cursor.close()
        conn.close()


def negar_pagamento(id_pagamento):
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("UPDATE tb_pagamentos SET status='rejeitado' WHERE id_pagamento=%s", (id_pagamento,))
        
        cursor.execute("SELECT id_user FROM tb_pagamentos WHERE id_pagamento=%s", (id_pagamento,))
        id_user = cursor.fetchone()[0]

        conn.commit()

        # Enviar e-mail
        enviar_email_status(id_user, "rejeitado")

        carregar_tabela_pagamentos()
    except Exception as erro:
        QMessageBox.critical(menu_pag, "Erro", f"Erro ao rejeitar pagamento:\n{erro}")
    finally:
        cursor.close()
        conn.close()

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email_status(id_user, status):
    try:
        conn = connect()
        cursor = conn.cursor()
        
        # Buscar email do responsável
        cursor.execute("SELECT email FROM tb_responsavel WHERE id_user = %s LIMIT 1", (id_user,))
        resultado = cursor.fetchone()
        if not resultado:
            print("⚠ Nenhum responsável encontrado para este usuário.")
            return
        
        email_responsavel = resultado[0]

        # Configuração SMTP (igual ao PHP)
        remetente = "contatofelipewmammana@gmail.com"
        senha = "wbhp jekz yzgm behz"  # senha de app do Gmail
        servidor_smtp = "smtp.gmail.com"
        porta_smtp = 587

        # Criar o email
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"Pagamento {status.capitalize()}"
        msg["From"] = "noreply@altus.com.br"
        msg["To"] = email_responsavel

        corpo_html = f"""
        <h3>Status do Pagamento</h3>
        <p><b>Usuário ID:</b> {id_user}</p>
        <p><b>Status:</b> <span style="color:{'green' if status=='aprovado' else 'red'};">{status.upper()}</span></p>
        <p>Verifique no sistema administrativo para mais detalhes.</p>
        """

        corpo_texto = f"Usuário ID: {id_user}\nStatus: {status.upper()}"

        msg.attach(MIMEText(corpo_texto, "plain"))
        msg.attach(MIMEText(corpo_html, "html"))

        # Enviar o email
        with smtplib.SMTP(servidor_smtp, porta_smtp) as server:
            server.starttls()
            server.login(remetente, senha)
            server.sendmail(remetente, email_responsavel, msg.as_string())

        print(f"✅ Email enviado para {email_responsavel} - Status: {status}")

    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()

def abrir_pdf(caminho_comprovante):
    if caminho_comprovante and os.path.exists(caminho_comprovante):
        if sys.platform.startswith("win"):
            os.startfile(caminho_comprovante)
        elif sys.platform.startswith("darwin"):
            subprocess.call(["open", caminho_comprovante])
        else:
            subprocess.call(["xdg-open", caminho_comprovante])
    else:
        QMessageBox.warning(menu_pag, "Erro", "Comprovante não encontrado.")


def ajustar_largura_coluna_ex(indice_coluna):
    list_window.tableExercicios.resizeColumnToContents(indice_coluna)

def ajustar_largura_coluna_user(indice_coluna):
    menu_user.tb_user.resizeColumnToContents(indice_coluna)

def ajustar_largura_coluna_med(indice_coluna):
    menu_med_list.tb_medicos.resizeColumnToContents(indice_coluna)

def ajustar_largura_coluna_prog(indice_coluna):
    menu_prog.tb_progresso.resizeColumnToContents(indice_coluna)


def carregar_tabela_exercicios():
    try:
        conn = connect()
        cursor = conn.cursor()
        sql = "SELECT id_ex, nome, grau, tipos, arquivo, link FROM tb_exercicios"
        cursor.execute(sql)
        resultado = cursor.fetchall()

        list_window.tableExercicios.setRowCount(len(resultado))
        list_window.tableExercicios.setColumnCount(6)
        list_window.tableExercicios.setHorizontalHeaderLabels(["ID", "Nome", "Grau", "Tipo", "Arquivo", "Link"])

        for row, dados in enumerate(resultado):
            for col, valor in enumerate(dados):
                item = QtWidgets.QTableWidgetItem(str(valor))
                list_window.tableExercicios.setItem(row, col, item)

    except Exception as erro:
        QMessageBox.critical(list_window, "Erro", f"Erro ao carregar tabela:\n{erro}")
    finally:
        cursor.close()
        conn.close()
# ===================== PESQUISAR_USER =======================
def pesquisar_list_exercicio():
    id = list_window.txt_pesquisar_id.text()
    nome = list_window.txt_pesquisar_nome.text()
    grau = list_window.cmb_pesquisar_grau.currentText()
    arquivos = list_window.cmb_pesquisar_aqv.currentText()
    tipos = pegar_tipos(list_window)

    try:
        conn = connect()
        cursor = conn.cursor()
        sql = "SELECT id_ex, nome, grau, tipos, arquivo, link FROM tb_exercicios WHERE 1=1"

        if id:
            sql += f" AND id_ex = '{id}'"
        if nome:
            sql += f" AND nome LIKE '%{nome}%'"
        if grau and grau != "Todos":
            sql += f" AND grau = '{grau}'"
        if arquivos and arquivos != "Todos":
            sql += f" AND arquivo LIKE '%{arquivos}%'"
        if tipos:
            for tipo in tipos.split(","):
                sql += f" AND tipos LIKE '%{tipo.strip()}%'"

        cursor.execute(sql)
        resultados = cursor.fetchall()

        list_window.tableExercicios.setRowCount(0)
        list_window.tableExercicios.setColumnCount(6)
        list_window.tableExercicios.setHorizontalHeaderLabels(["ID", "Nome", "Grau", "Tipo", "Arquivo", "Link"])

        for row_num, row_data in enumerate(resultados):
            list_window.tableExercicios.insertRow(row_num)
            for col_num, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                list_window.tableExercicios.setItem(row_num, col_num, item)

        if not resultados:
            QMessageBox.information(list_window, "Nenhum resultado", "Nenhum exercício encontrado.")

    except Exception as erro:
        QMessageBox.critical(list_window, "Erro", f"Erro na pesquisa:\n{erro}")
    finally:
        cursor.close()
        conn.close()
# ===================== USUARIOS =======================
def pesquisar_list_user():
    id = menu_user.txt_pesquisar_id.text()
    nome = menu_user.txt_pesquisar_nome.text()
    sobrenome = menu_user.txt_pesquisar_sobrenome.text()
    idade = menu_user.txt_pesquisar_nome_2.text()  
    grau = menu_user.cmb_pesquisar_grau.currentText()
    
    conn = None
    cursor = None
    try:
        conn = connect()
        cursor = conn.cursor()

        sql = """
        SELECT u.id_user, u.nome, u.sobrenome, u.idade, m.grau, r.telefone
        FROM tb_user u
        LEFT JOIN tb_user_med m ON u.id_user = m.id_user
        LEFT JOIN tb_responsavel r ON u.id_user = r.id_user
        WHERE 1=1
        """

        params = []
        if id:
            sql += " AND u.id_user = %s"
            params.append(id)
        if nome:
            sql += " AND u.nome LIKE %s"
            params.append(f"%{nome}%")
        if sobrenome:
            sql += " AND u.sobrenome LIKE %s"
            params.append(f"%{sobrenome}%")
        if grau and grau != "Todos":
            sql += " AND m.grau = %s"
            params.append(grau)
        if idade:
            sql += " AND u.idade LIKE %s"
            params.append(f"%{idade}%")

        cursor.execute(sql, params)
        resultados = cursor.fetchall()

        menu_user.tb_user.setRowCount(0)
        menu_user.tb_user.setColumnCount(6)
        menu_user.tb_user.setHorizontalHeaderLabels(
            ["ID", "Nome", "Sobrenome", "Idade", "Grau", "Telefone do Responsável"]
        )

        for row_num, row_data in enumerate(resultados):
            menu_user.tb_user.insertRow(row_num)
            for col_num, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem("" if value is None else str(value))
                menu_user.tb_user.setItem(row_num, col_num, item)

        if not resultados:
            QMessageBox.information(menu_user, "Nenhum resultado", "Nenhum usuário encontrado.")

    except Exception as erro:
        QMessageBox.critical(menu_user, "Erro", f"Erro na pesquisa:\n{erro}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def carregar_tabela_usuarios():
    try:
        conn = connect()
        cursor = conn.cursor()

        sql = """
        SELECT u.id_user, u.nome, u.sobrenome, u.idade, m.grau, r.telefone
        FROM tb_user u
        LEFT JOIN tb_user_med m ON u.id_user = m.id_user
        LEFT JOIN tb_responsavel r ON u.id_user = r.id_user
        """
        
        cursor.execute(sql)
        resultado = cursor.fetchall()

        menu_user.tb_user.setRowCount(len(resultado))
        menu_user.tb_user.setColumnCount(6)
        menu_user.tb_user.setHorizontalHeaderLabels(
            ["ID", "Nome", "Sobrenome", "Idade", "Grau", "Telefone do Responsável"]
        )

        for row, dados in enumerate(resultado):
            for col, valor in enumerate(dados):
                item = QtWidgets.QTableWidgetItem("" if valor is None else str(valor))
                menu_user.tb_user.setItem(row, col, item)

    except Exception as erro:
        QMessageBox.critical(menu_user, "Erro", f"Erro ao carregar tabela:\n{erro}")
    finally:
        cursor.close()
        conn.close()


# ===================== MEDICOS LISTAGEM =======================
def pesquisar_list_med():
    id = menu_med_list.txt_id_med.text()
    nome = menu_med_list.txt_pesquisar_nome.text()
    tipo = menu_med_list.cmb_tipo.currentText()
     
    try:
        conn = connect()
        cursor = conn.cursor()
        sql = "SELECT id_med, nome, data_nascimento, telefone, tipo_especialidade, crn FROM tb_medico WHERE 1=1"

        if id:
            sql += f" AND id_med = '{id}'"
        if nome:
            sql += f" AND nome LIKE '%{nome}%'"
        if tipo and tipo != "Todos":
            sql += f" AND tipo_especialidade = '{tipo}'"

        cursor.execute(sql)
        resultados = cursor.fetchall()

        menu_med_list.tb_medicos.setRowCount(0)
        menu_med_list.tb_medicos.setColumnCount(6)
        menu_med_list.tb_medicos.setHorizontalHeaderLabels(["ID", "Nome", "Data_nascimento",  "Telefone", "Tipo" ,"CRM"])

        for row_num, row_data in enumerate(resultados):
            menu_med_list.tb_medicos.insertRow(row_num)
            for col_num, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                menu_med_list.tb_medicos.setItem(row_num, col_num, item)

        if not resultados:
            QMessageBox.information(menu_med_list, "Nenhum resultado", "Nenhum resultado encontrado.")

    except Exception as erro:
        QMessageBox.critical(menu_med_list, "Erro", f"Erro na pesquisa:\n{erro}")
    finally:
        cursor.close()
        conn.close()

def carregar_tabela_medicos():
    try:
        conn = connect()
        cursor = conn.cursor()
        sql = "SELECT id_med, nome, data_nascimento, telefone, tipo_especialidade, crn FROM tb_medico"
        cursor.execute(sql)
        resultado = cursor.fetchall()

        menu_med_list.tb_medicos.setRowCount(len(resultado))
        menu_med_list.tb_medicos.setColumnCount(6)
        menu_med_list.tb_medicos.setHorizontalHeaderLabels(["ID", "Nome", "Data_nascimento",  "Telefone", "Tipo" ,"CRM"])

        for row, dados in enumerate(resultado):
            for col, valor in enumerate(dados):
                item = QtWidgets.QTableWidgetItem(str(valor))
                menu_med_list.tb_medicos.setItem(row, col, item)

    except Exception as erro:
        QMessageBox.critical(menu_med_list, "Erro", f"Erro ao carregar tabela:\n{erro}")
    finally:
        cursor.close()
        conn.close()
# ===================== MEDICOS CADASTRO ====================
def buscar_medico():
    id_pesquisa = menu_med_cad.txt_pesquisar.text()

    if not id_pesquisa:
        QMessageBox.warning(menu_med_cad, "Atenção", "Digite um ID para pesquisar.")
        return

    try:
        conn = connect()
        cursor = conn.cursor()

        sql = """SELECT m.id_med, m.nome, m.data_nascimento, m.telefone, m.tipo_especialidade, 
                        m.crn, m.foto, l.email, l.senha
                 FROM tb_medico m
                 INNER JOIN tb_login l ON m.id_med = l.id_med
                 WHERE m.id_med = %s"""
        cursor.execute(sql, (id_pesquisa,))
        resultado = cursor.fetchone()

        if resultado:
            
            id_medico, nome, data, telefone, tipo, crn, foto_bin, email, senha = resultado


            menu_med_cad.txt_nome.setText(nome)
            menu_med_cad.txt_data.setText(str(data))
            menu_med_cad.txt_telefone.setText(telefone)
            menu_med_cad.cmb_tipo.setCurrentText(tipo)
            menu_med_cad.txt_crn.setText(crn)
            menu_med_cad.txt_email.setText(email)
            menu_med_cad.txt_senha.setText(senha)
            menu_med_cad.txt_senhac.setText(senha)

            
            if foto_bin:
                pixmap = QPixmap()
                pixmap.loadFromData(foto_bin)
                pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

                circular = QPixmap(150, 150)
                circular.fill(Qt.transparent)

                painter = QPainter(circular)
                painter.setRenderHint(QPainter.Antialiasing)
                path = QPainterPath()
                path.addEllipse(0, 0, 150, 150)
                painter.setClipPath(path)
                painter.drawPixmap(0, 0, pixmap)
                painter.end()

                menu_med_cad.lbl_foto.setPixmap(circular)
                menu_med_cad.lbl_foto.setScaledContents(True)
                
                if hasattr(menu_med_cad, 'caminho_foto'):
                    del menu_med_cad.caminho_foto
            else:
                menu_med_cad.lbl_foto.clear()

        else:
            QMessageBox.warning(menu_med_cad, "Não encontrado", "Nenhum médico encontrado com esse ID.")

    except Exception as erro:
        QMessageBox.critical(menu_med_cad, "Erro", f"Erro ao buscar médico:\n{erro}")
    finally:
        cursor.close()
        conn.close()

def editar_medico():
    try:
        id_medico = menu_med_cad.txt_pesquisar.text()
        if not id_medico:
            QMessageBox.warning(menu_med_cad, "Erro", "Selecione um médico para editar.")
            return

        nome = menu_med_cad.txt_nome.text()
        data_str = menu_med_cad.txt_data.text()
        telefone = menu_med_cad.txt_telefone.text()
        email = menu_med_cad.txt_email.text()
        senha = menu_med_cad.txt_senha.text()
        tipo = menu_med_cad.cmb_tipo.currentText()
        crn = menu_med_cad.txt_crn.text()
        foto = menu_med_cad.caminho_foto if hasattr(menu_med_cad, 'caminho_foto') else None

        # Convert the date string to a date object
        try:
            data_nascimento = datetime.strptime(data_str, '%d/%m/%Y').date()
        except ValueError:
            QMessageBox.critical(menu_med_cad, "Erro", "Formato de data inválido. Use DD/MM/AAAA.")
            return
            
        conn = connect()
        cursor = conn.cursor()

        if foto:
            with open(foto, 'rb') as arq:
                foto_bin = arq.read()
        else:
            cursor.execute("SELECT foto FROM tb_medico WHERE id_med = %s", (id_medico,))
            foto_bin = cursor.fetchone()[0]

        sql = """UPDATE tb_medico SET nome=%s, data_nascimento=%s, telefone=%s, tipo_especialidade=%s, crn=%s, foto=%s
                 WHERE id_med=%s"""
        # Pass the date object to the query
        cursor.execute(sql, (nome, data_nascimento, telefone, tipo, crn, foto_bin, id_medico))

        sql_login = "UPDATE tb_login SET email=%s, senha=%s WHERE id_med=%s"
        cursor.execute(sql_login, (email, senha, id_medico))

        conn.commit()
        QMessageBox.information(menu_med_cad, "Sucesso", "Dados do médico atualizados com sucesso!")

    except Exception as erro:
        QMessageBox.critical(menu_med_cad, "Erro", f"Erro ao editar dados:\n{erro}")
    finally:
        cursor.close()
        conn.close()

def excluir_medico():
    try:
        id_medico = menu_med_cad.txt_pesquisar.text()
        if not id_medico:
            QMessageBox.warning(menu_med_cad, "Erro", "Selecione um médico para excluir.")
            return

        confirm = QMessageBox.question(menu_med_cad, "Confirmação", "Tem certeza que deseja excluir este médico?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.No:
            return

        conn = connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tb_login WHERE id_med = %s", (id_medico,))
        cursor.execute("DELETE FROM tb_medico WHERE id_med = %s", (id_medico,))
        conn.commit() 

        QMessageBox.information(menu_med_cad, "Sucesso", "Médico excluído com sucesso!")

        
        menu_med_cad.txt_pesquisar.clear()
        menu_med_cad.txt_nome.clear()
        menu_med_cad.txt_data.clear()
        menu_med_cad.txt_crn.clear()
        menu_med_cad.txt_telefone.clear()
        menu_med_cad.txt_email.clear()
        menu_med_cad.txt_senha.clear()
        menu_med_cad.txt_senhac.clear()
        menu_med_cad.lbl_foto.clear()

    except Exception as erro:
        QMessageBox.critical(menu_med_cad, "Erro", f"Erro ao excluir médico:\n{erro}")
    finally:
        cursor.close()
        conn.close()

def insert_medico():
    nome = menu_med_cad.txt_nome.text()
    data_str = menu_med_cad.txt_data.text()
    telefone = menu_med_cad.txt_telefone.text()
    email = menu_med_cad.txt_email.text()
    senha = menu_med_cad.txt_senha.text()
    senhac = menu_med_cad.txt_senhac.text()
    tipo = menu_med_cad.cmb_tipo.currentText()
    crn = menu_med_cad.txt_crn.text()

    foto = menu_med_cad.caminho_foto if hasattr(menu_med_cad, 'caminho_foto') else None

    
    try:
        data_nascimento = datetime.strptime(data_str, '%d/%m/%Y').date()
    except ValueError:
        QMessageBox.critical(menu_med_cad, "Erro", "Formato de data inválido. Use DD/MM/AAAA.")
        return

    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(f"SELECT id_med FROM tb_medico WHERE crn = '{crn}'")
        if cursor.fetchone():
            QMessageBox.warning(menu_med_cad, "CRM existente", "Já existe um médico cadastrado com esse CRM.")
            return

        cursor.execute(f"SELECT id_med FROM tb_login WHERE email = '{email}'")
        if cursor.fetchone():
            QMessageBox.warning(menu_med_cad, "Email existente", "Já existe um usuário cadastrado com esse email.")
            return
        
        # ... (rest of the photo handling code) ...
        if foto:
            with open(foto, 'rb') as arq:
                foto_bin = arq.read()
        else:
            foto_bin = None

        sql = """INSERT INTO tb_medico (nome, data_nascimento, telefone, tipo_especialidade, crn, foto) VALUES (%s, %s, %s, %s, %s, %s)"""
        # Pass the converted date object
        cursor.execute(sql, (nome, data_nascimento, telefone, tipo, crn, foto_bin))

        id_med = cursor.lastrowid

        sql1 = """INSERT INTO tb_login (id_med, email, senha, tipo) VALUES (%s, %s, %s, 'med')"""
        cursor.execute(sql1, (id_med, email, senha))

        conn.commit()

        QMessageBox.information(menu_med_cad, "Sucesso", "Médico cadastrado com sucesso!")

        menu_med_cad.txt_nome.clear()
        menu_med_cad.txt_data.clear()
        menu_med_cad.txt_crn.clear()
        menu_med_cad.txt_telefone.clear()
        menu_med_cad.txt_email.clear()
        menu_med_cad.txt_senha.clear()
        menu_med_cad.txt_senhac.clear()
        menu_med_cad.lbl_foto.clear()

    except Exception as erro:
        QMessageBox.critical(menu_med_cad, "Erro", f"Erro ao inserir dados:\n{erro}")
    finally:
        cursor.close()
        conn.close()

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5.QtCore import Qt

def carregar_foto():
    fileName, _ = QFileDialog.getOpenFileName(
        None, "Selecionar Foto", "", "Imagens (*.png *.jpg *.jpeg)"
    )
    if fileName:
        
        original = QPixmap(fileName).scaled(150, 150, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        
        circular = QPixmap(150, 150)
        circular.fill(Qt.transparent)

        painter = QPainter(circular)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0, 0, 150, 150)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, original)
        painter.end()

        menu_med_cad.lbl_foto.setPixmap(circular)
        menu_med_cad.lbl_foto.setScaledContents(True)

        
        menu_med_cad.caminho_foto = fileName
def carregar_foto_ex():
    fileName, _ = QFileDialog.getOpenFileName(
        None, "Selecionar Foto", "", "Imagens (*.png *.jpg *.jpeg)"
    )
    if fileName:
        
        original = QPixmap(fileName).scaled(150, 150, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        
        circular = QPixmap(150, 150)
        circular.fill(Qt.transparent)

        painter = QPainter(circular)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0, 0, 150, 150)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, original)
        painter.end()

        add_window.lbl_foto.setPixmap(circular)
        add_window.lbl_foto.setScaledContents(True)

        
        add_window.caminho_foto = fileName    

def carregar_foto_exe():
    fileName, _ = QFileDialog.getOpenFileName(
        None, "Selecionar Foto", "", "Imagens (*.png *.jpg *.jpeg)"
    )
    if fileName:
        
        original = QPixmap(fileName).scaled(150, 150, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        
        circular = QPixmap(150, 150)
        circular.fill(Qt.transparent)

        painter = QPainter(circular)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0, 0, 150, 150)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, original)
        painter.end()

        edit_window.lbl_foto.setPixmap(circular)
        edit_window.lbl_foto.setScaledContents(True)

        
        edit_window.caminho_foto = fileName    

from PyQt5 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as mticker


# ------------------- Classe Base -------------------
class GraficoCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        super(GraficoCanvas, self).__init__(self.fig)
        self.setParent(parent)
        

# ------------------- Helpers -------------------
def add_canvas_to_widget(widget, canvas):
    """Adiciona o canvas ao widget, reutilizando layout se já existir"""
    layout = widget.layout()
    if layout is None:
        layout = QtWidgets.QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(canvas)


# ------------------- Gráficos Estáticos -------------------
def grafico_usuarios_por_plano(widget):
    canvas = GraficoCanvas(widget, width=4, height=4)
    plano_labels = ['Ouro', 'Prata', 'Bronze']
    plano_vals = [64, 99, 49]

    canvas.ax.clear()
    canvas.ax.pie(plano_vals, labels=plano_labels, autopct='%1.1f%%', startangle=90,
                  colors=["#FFD700", "#C0C0C0", "#CD7F32"])
    canvas.ax.set_title("Usuários Por Plano")

    add_canvas_to_widget(widget, canvas)


# ------------------- Banco de Dados -------------------
def obter_usuarios_por_plano():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT plano, COUNT(*) FROM tb_user GROUP BY plano")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return dados


def obter_usuarios_por_grau():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT grau, COUNT(*) FROM tb_user_med GROUP BY grau")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return dados


def obter_crescimento():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DATE_FORMAT(data_cadastro, '%Y-%m') AS mes, COUNT(*) AS total 
        FROM tb_user 
        GROUP BY mes 
        ORDER BY mes;
    """)
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return dados


# ------------------- Gráficos Dinâmicos -------------------
def plotar_grafico_plano(widget):
    dados = obter_usuarios_por_plano()
    if not dados:
        return

    planos, valores = zip(*dados)

    # Mapeamento de cores
    cores = []
    for plano in planos:
        if plano.lower() == "ouro":
            cores.append("#FFD700")  # dourado
        elif plano.lower() == "prata":
            cores.append("#C0C0C0")  # prata
        elif plano.lower() == "bronze":
            cores.append("#CD7F32")  # bronze
        else:
            cores.append("skyblue")  # cor padrão caso venha outro plano

    canvas = GraficoCanvas(widget, width=5, height=4)
    canvas.ax.pie(valores, labels=planos, autopct='%1.1f%%', startangle=90, colors=cores)
    canvas.ax.set_title("Usuários por Plano")

    add_canvas_to_widget(widget, canvas)


def plotar_grafico_grau(widget):
    dados = obter_usuarios_por_grau()
    if not dados:
        return

    graus, valores = zip(*dados)

    canvas = GraficoCanvas(widget, width=5, height=4)
    canvas.ax.bar(graus, valores, color='skyblue')
    canvas.ax.set_title("Usuários por Grau")
    canvas.ax.set_ylabel("Quantidade")

    # Apenas inteiros no eixo Y
    canvas.ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ymin, ymax = min(valores), max(valores)
    canvas.ax.set_ylim(ymin - 1, ymax + 1)

    add_canvas_to_widget(widget, canvas)


def plotar_grafico_crescimento(widget):
    dados = obter_crescimento()
    if not dados:
        return

    meses, valores = zip(*dados)

    canvas = GraficoCanvas(widget, width=6, height=4)
    canvas.ax.plot(meses, valores, color='green', marker='o')
    canvas.ax.set_title("Crescimento de Usuários")
    canvas.ax.set_ylabel("Total de Usuários")
    canvas.ax.set_xlabel("Mês")
    canvas.ax.grid(True)

    # Apenas inteiros no eixo Y
    canvas.ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ymin, ymax = min(valores), max(valores)
    canvas.ax.set_ylim(ymin - 1, ymax + 1)

    add_canvas_to_widget(widget, canvas)



# ------------------- Tela Principal -------------------


# ===================== INICIAR APLICAÇÃO =======================
app = QtWidgets.QApplication([])
login_window = uic.loadUi("frm_login.ui")
login_window.pushButton.clicked.connect(login)
login_window.show()

app.exec()
