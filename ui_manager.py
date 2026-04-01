import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,
QLabel, QPushButton, QWidget, QMessageBox, QStackedLayout, 
QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import (QFont)
from PyQt6.QtCore import Qt
from info_estudiantes import info_estudiantes
from info_proyecto import info_proyecto


#Ya ni se que arquitectura apliqué en este modulo, solo espero que no se rompa
#Actualizacion: maybe sea monolito, no se
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.lbl_Oferta = QLabel("Oferta actual: ")
        self.contenedor_participantes = QWidget()
        
    def initialize_ui(self):
        self.setFixedSize(1280,720)
        self.setWindowTitle("Proyecto Sistemas Operativos")
        self.generate_window()
        self.show()

        #Parametros para la simulación
        
        

    def generate_window(self):
        estudiantes = info_estudiantes()
        descripcion = info_proyecto()
        

        #Botones para cambiar pestañas
        button_1 = QPushButton("Mostrar Estudiantes")
        button_1.clicked.connect(self.change_window)
        button_2 = QPushButton("Mostrar Descripción")
        button_2.clicked.connect(self.change_window)
        button_3 = QPushButton("Iniciar Simulador de Subastas")
        button_3.clicked.connect(self.change_window)
        button_4 = QPushButton("Ver Log")
        #button_4.clicked.connect(self.change_window)

        buttons_group = QVBoxLayout()
        buttons_group.addWidget(button_1)
        buttons_group.addWidget(button_2)
        buttons_group.addWidget(button_3)
        buttons_group.addWidget(button_4)
        buttons_group.setAlignment(Qt.AlignmentFlag.AlignTop)
        buttons_group.setSpacing(0)
        buttons_group.setContentsMargins(0, 10, 0, 0)
        
        container_buttons = QWidget()
        container_buttons.setLayout(buttons_group)
        container_buttons.setObjectName("Grupo_Botones")
        
        #Pagina 0: Inicio
        titulo_0 = QLabel("¡Bienvenido/a!")
        titulo_0.setProperty("tipo", "subtitulo")

        lbl_tutorial =QLabel("Use el menú de la izquierda para poder usar el programa")
        lbl_tutorial.setWordWrap(True)
        lbl_tutorial.setProperty("tipo", "contenido")

        page0_layout = QVBoxLayout()
        page0_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        page0_layout.setContentsMargins(30, 30, 30, 30)
        page0_layout.addWidget(titulo_0)
        page0_layout.addWidget(lbl_tutorial)

        container_0 = QWidget()
        container_0.setLayout(page0_layout)
        container_0.setProperty("tipo","stacked_widgets")

        #Pagina 1: Estudiantes
        titulo_1 = QLabel("Estudiantes:")
        titulo_1.setProperty("tipo", "subtitulo")

        page1_layout = QVBoxLayout()
        page1_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        page1_layout.setContentsMargins(30, 30, 30, 30)
        page1_layout.addWidget(titulo_1)
        for estudiante in estudiantes.lista_estudiantes:
            label_estudiante = QLabel(" - "+estudiante)
            label_estudiante.setProperty("tipo", "contenido")
            page1_layout.addWidget(label_estudiante)

        container_1 = QWidget()
        container_1.setLayout(page1_layout)
        container_1.setProperty("tipo","stacked_widgets")


        #Pagina 2: Descripcion
        titulo_2 = QLabel("Descripción:")
        titulo_2.setProperty("tipo", "subtitulo")

        lbl_desc = QLabel(descripcion.descripcion)
        lbl_desc.setProperty("tipo", "contenido")
        lbl_desc.setWordWrap(True)

        page2_layout = QVBoxLayout()
        page2_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        page2_layout.setContentsMargins(30, 30, 30, 30)
        page2_layout.addWidget(titulo_2)
        page2_layout.addWidget(lbl_desc)
        
        container_2 = QWidget()
        container_2.setLayout(page2_layout)
        container_2.setProperty("tipo","stacked_widgets")


        #Pagina 3: Simulador subasta
        titulo_3 = QLabel("Simulador Subasta")
        titulo_3.setProperty("tipo", "subtitulo")

        lbl_pregunta = QLabel("¿Desea iniciar la subasta?")
        lbl_pregunta.setProperty("tipo", "contenido")
        lbl_pregunta.setWordWrap(True)

        button_si = QPushButton("Si")
        button_si.clicked.connect(self.simulador)
        button_no = QPushButton("No")
        button_no.clicked.connect(self.simulador)

        hb_opciones = QHBoxLayout()
        hb_opciones.addWidget(button_si)
        hb_opciones.addWidget(button_no)

        page3_layout = QVBoxLayout()
        page3_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        page3_layout.setContentsMargins(30, 30, 30, 30)
        page3_layout.addWidget(titulo_3)
        page3_layout.addWidget(lbl_pregunta)
        page3_layout.addLayout(hb_opciones)

        container_3 = QWidget()
        container_3.setLayout(page3_layout)
        container_3.setProperty("tipo","stacked_widgets")


        #Pagina 4: Simulación (como conecto esta interfaz con los hilos?)
        #diosmio ayudame
        #titulo_4 = QLabel("Simulación Iniciada")
        #titulo_4.setProperty("tipo", "subtitulo")

        
        #self.lbl_Oferta.setProperty("tipo", "contenido")
        #self.lbl_Oferta.setWordWrap(True)

        #self.page4_layout = QVBoxLayout()
        #self.page4_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        #self.page4_layout.setContentsMargins(30, 30, 30, 30)
        #self.page4_layout.addWidget(titulo_4)
        #self.page4_layout.addWidget(self.lbl_Oferta)
        #self.page4_layout.addLayout(hb_opciones)


        #Stacked Layout para ir cambiando de pestañas
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(container_0)
        self.stacked_layout.addWidget(container_1)
        self.stacked_layout.addWidget(container_2)
        self.stacked_layout.addWidget(container_3)


        #HBox para agregar botones y pestañas        
        main_hbox = QHBoxLayout()
        main_hbox.addWidget(container_buttons, 1)
        main_hbox.addLayout(self.stacked_layout, 3)
        main_hbox.setSpacing(20)
        

        #VBox que funciona como la estructura principal del programa
        main_title = QLabel("Proyecto Sistemas Operativos")
        main_title.setProperty("tipo", "titulo")
        main_layout = QVBoxLayout()
        main_layout.addWidget(main_title,1, alignment=Qt.AlignmentFlag.AlignCenter)        
        main_layout.addLayout(main_hbox,7)
        centerWidget = QWidget()
        centerWidget.setLayout(main_layout)
        self.setCentralWidget(centerWidget)
        

    def change_window(self):
        button = self.sender()
        button_txt = button.text().lower()
        match button_txt:
            case "mostrar estudiantes":
                self.stacked_layout.setCurrentIndex(1)
            case "mostrar descripción":
                self.stacked_layout.setCurrentIndex(2)
            case "iniciar simulador de subastas":
                self.stacked_layout.setCurrentIndex(3)
    

    def simulador(self):
        button = self.sender()
        button_txt = button.text().lower()
        match button_txt:
            case "si":
                self.stacked_layout.setCurrentIndex(0)
                self.iniciar_simulacion()
            case "no":
                self.stacked_layout.setCurrentIndex(0)
    
    #pues el plan es pasarle las referencias al GridLayout y a la oferta actual para que 
    #la clase subastaGUI pueda modificarla...
    #pero a saber como se puede hacer eso
    def iniciar_simulacion(self):
        self.contenedor_participantes.setParent(None)
        self.contenedor_participantes.deleteLater()
        self.contenedor_participantes = QWidget()
        grid_participantes = QGridLayout(self.contenedor_participantes)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    window = MainWindow()
    
    sys.exit(app.exec())