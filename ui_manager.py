import sys
import threading
from PyQt6.QtWidgets import (QApplication, QFrame, QMainWindow,
QLabel, QProgressBar, QPushButton, QWidget, QMessageBox, QStackedLayout, 
QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt6.QtGui import (QFont)
from PyQt6.QtCore import Qt, pyqtSlot
from info_estudiantes import info_estudiantes
from info_proyecto import info_proyecto
from SubastaGUI import SubastaGUI
from Producto import Producto


# Ya ni se que arquitectura apliqué en este modulo, solo espero que no se rompa
# Actualizacion: monolito. por ahora no se rompe

#TODO:  a saber

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lbl_Oferta = QLabel("Oferta actual: ")
        self.contenedor_participantes = QWidget()
        self.widgets_participantes = {}
        self.initialize_ui()
       
        
    def initialize_ui(self):
        self.setFixedSize(1280,720)
        self.setWindowTitle("Proyecto Sistemas Operativos")
        self.generate_window()
        self.show()

        # Parametros para la simulación
        
        

    def generate_window(self):
        estudiantes = info_estudiantes()
        descripcion = info_proyecto()
        
    
        # Botones para cambiar pestañas
        button_1 = QPushButton("Mostrar Estudiantes")
        button_1.clicked.connect(self.change_window)
        button_2 = QPushButton("Mostrar Descripción")
        button_2.clicked.connect(self.change_window)
        button_3 = QPushButton("Iniciar Simulador de Subastas")
        button_3.clicked.connect(self.change_window)
        button_4 = QPushButton("Limpiar log")
        button_4.clicked.connect(self.limpiar_log)

        buttons_group = QVBoxLayout()
        buttons_group.addWidget(button_1)
        buttons_group.addWidget(button_2)
        buttons_group.addWidget(button_3)
        buttons_group.addWidget(button_4)
        buttons_group.setAlignment(Qt.AlignmentFlag.AlignTop)
        buttons_group.setSpacing(15)
        buttons_group.setContentsMargins(15, 15, 15, 15)
        
        self.container_buttons = QWidget()
        self.container_buttons.setLayout(buttons_group)
        self.container_buttons.setObjectName("Grupo_Botones")
        
        # Pagina 0: Inicio
        titulo_0 = QLabel("¡Bienvenido/a!")
        titulo_0.setProperty("tipo", "subtitulo")

        lbl_tutorial =QLabel("Use el menú de la izquierda para poder usar el programa.")
        lbl_tutorial.setWordWrap(True)
        lbl_tutorial.setProperty("tipo", "contenido")

        page0_layout = QVBoxLayout()
        page0_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        page0_layout.setContentsMargins(30, 30, 30, 30)
        page0_layout.setSpacing(20)
        page0_layout.addWidget(titulo_0)
        page0_layout.addWidget(self.generar_divisor())
        page0_layout.addWidget(lbl_tutorial)

        container_0 = QWidget()
        container_0.setLayout(page0_layout)
        container_0.setProperty("tipo","stacked_widgets")

        # Pagina 1: Estudiantes
        titulo_1 = QLabel("Estudiantes:")
        titulo_1.setProperty("tipo", "subtitulo")

        vbox_estudiantes = QVBoxLayout()
        vbox_estudiantes.setSpacing(5)

        page1_layout = QVBoxLayout()
        page1_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        page1_layout.setContentsMargins(30, 30, 30, 30)
        page1_layout.setSpacing(20)
        page1_layout.addWidget(titulo_1)
        page1_layout.addWidget(self.generar_divisor())
        page1_layout.addLayout(vbox_estudiantes)

        for estudiante in estudiantes.lista_estudiantes:
            label_estudiante = QLabel(" - "+estudiante)
            label_estudiante.setProperty("tipo", "contenido")
            vbox_estudiantes.addWidget(label_estudiante)

        container_1 = QWidget()
        container_1.setLayout(page1_layout)
        container_1.setProperty("tipo","stacked_widgets")


        # Pagina 2: Descripcion
        titulo_2 = QLabel("Descripción:")
        titulo_2.setProperty("tipo", "subtitulo")

        lbl_desc = QLabel(descripcion.descripcion)
        lbl_desc.setProperty("tipo", "contenido")
        lbl_desc.setWordWrap(True)

        page2_layout = QVBoxLayout()
        page2_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        page2_layout.setContentsMargins(30, 30, 30, 30)
        page2_layout.setSpacing(20)
        page2_layout.addWidget(titulo_2)
        page2_layout.addWidget(self.generar_divisor())
        page2_layout.addWidget(lbl_desc)
        
        container_2 = QWidget()
        container_2.setLayout(page2_layout)
        container_2.setProperty("tipo","stacked_widgets")


        # Pagina 3: Simulador subasta
        titulo_3 = QLabel("Simulador Subasta")
        titulo_3.setProperty("tipo", "subtitulo")

        subasta_desc = "Esta es una simulación de una subasta electrónica donde se competirá por ganar un Iphone X. \n" \
        "Esta simulación usará hilos que actuaran como postores en una subasta. Se pondrá a prueba el uso de locks " \
        "para modificar variables dentro de una sección critica.\n" \
        "¿Desea iniciar la subasta?"

        lbl_pregunta = QLabel(subasta_desc)
        lbl_pregunta.setProperty("tipo", "contenido")
        lbl_pregunta.setWordWrap(True)

        button_si = QPushButton("Si")
        button_si.clicked.connect(self.simulador)
        button_no = QPushButton("No")
        button_no.clicked.connect(self.simulador)

        hb_opciones = QHBoxLayout()
        hb_opciones.addWidget(button_si)
        hb_opciones.addWidget(button_no)
        hb_opciones.setSpacing(30)
        hb_opciones.setContentsMargins(30, 30, 30, 30)

        page3_layout = QVBoxLayout()
        page3_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        page3_layout.setContentsMargins(30, 30, 30, 30)
        page3_layout.setSpacing(20)
        page3_layout.addWidget(titulo_3)
        page3_layout.addWidget(self.generar_divisor())
        page3_layout.addWidget(lbl_pregunta)
        page3_layout.addStretch(1)
        page3_layout.addLayout(hb_opciones)

        container_3 = QWidget()
        container_3.setLayout(page3_layout)
        container_3.setProperty("tipo","stacked_widgets")


        # Página 4: Tablero de Subasta
        self.page4_layout = QVBoxLayout()
        self.page4_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.page4_layout.setSpacing(40)
        
        # 1. Barra de tiempo
        self.lbl_reloj = QLabel("Tiempo restante: --s")
        self.lbl_reloj.setProperty("tipo","subtitulo")
        self.barra_progreso = QProgressBar()
        self.vbox_tiempo = QVBoxLayout()
        self.vbox_tiempo.addWidget(self.lbl_reloj)
        self.vbox_tiempo.addWidget(self.barra_progreso)
        self.vbox_tiempo.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.vbox_tiempo.setSpacing(10)

        self.lbl_oferta_grande = QLabel("Oferta Actual: $0")
        self.lbl_oferta_grande.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_oferta_grande.setProperty("tipo","titulo")
        
        self.grid_bots = QGridLayout()
        self.grid_bots.setSpacing(5)
        
        self.page4_layout.addWidget(self.lbl_oferta_grande)
        self.page4_layout.addLayout(self.vbox_tiempo)
        self.page4_layout.addWidget(self.generar_divisor())
        self.page4_layout.addLayout(self.grid_bots)
        self.page4_layout.setContentsMargins(30, 30, 30, 30)

        container_4 = QWidget()
        container_4.setLayout(self.page4_layout)
        container_4.setProperty("tipo","stacked_widgets")


        # Pagina 5: Ganador:
        titulo_5 = QLabel("Ganador:")
        titulo_5.setProperty("tipo", "subtitulo")

        self.lbl_ganador = QLabel("El/La postor/a ___ ha ganado un ___ por el valor de___")
        self.lbl_ganador.setProperty("tipo", "contenido")
        self.lbl_ganador.setWordWrap(True)

        button_fin = QPushButton("Regresar")
        button_fin.clicked.connect(self.change_window)
        
        page5_layout = QVBoxLayout()
        page5_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        page5_layout.setContentsMargins(30, 30, 30, 30)
        page5_layout.setSpacing(20)
        page5_layout.addWidget(titulo_5)
        page5_layout.addWidget(self.generar_divisor())
        page5_layout.addWidget(self.lbl_ganador)
        page5_layout.addStretch(1)
        page5_layout.addWidget(button_fin)
        
        container_5 = QWidget()
        container_5.setLayout(page5_layout)
        container_5.setProperty("tipo","stacked_widgets")


        # Stacked Layout para ir cambiando de pestañas
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(container_0)
        self.stacked_layout.addWidget(container_1)
        self.stacked_layout.addWidget(container_2)
        self.stacked_layout.addWidget(container_3)
        self.stacked_layout.addWidget(container_4) 
        self.stacked_layout.addWidget(container_5)


        # HBox para agregar botones y pestañas        
        main_hbox = QHBoxLayout()
        main_hbox.addWidget(self.container_buttons, 1)
        main_hbox.addLayout(self.stacked_layout, 3)
        main_hbox.setSpacing(20)
        

        # VBox que funciona como la estructura principal del programa
        main_title = QLabel("Proyecto Sistemas Operativos")
        main_title.setProperty("tipo", "titulo")
        main_layout = QVBoxLayout()
        main_layout.addWidget(main_title,1, alignment=Qt.AlignmentFlag.AlignLeft)        
        main_layout.addLayout(main_hbox,7)
        centerWidget = QWidget()
        centerWidget.setLayout(main_layout)
        self.setCentralWidget(centerWidget)
        

    # Deberia darles un id en vez de comparar nombres
    def change_window(self):
        button = self.sender()
        button_txt = button.text().lower()
        match button_txt:
            case "mostrar estudiantes":
                print("Botón pestaña de estudiantes presionado")
                self.stacked_layout.setCurrentIndex(1)
            case "mostrar descripción":
                print("Botón pestaña de descripción presionado")
                self.stacked_layout.setCurrentIndex(2)
            case "iniciar simulador de subastas":
                print("Botón pestaña de simulador presionado")
                self.stacked_layout.setCurrentIndex(3)
            case "regresar":
                print("Botón pestaña de inicio presionado")
                self.stacked_layout.setCurrentIndex(0)
    
    def generar_divisor(self):
    # Linea horizontal divisora de contenido:
        linea = QFrame()
        linea.setProperty("tipo","linea_divisora")
        linea.setFrameShape(QFrame.Shape.HLine)
        return linea
    
    def crear_card_participante(self, id_bot, nombre):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.StyledPanel)
        frame.setStyleSheet("background-color: #192d56; border: 2px solid #455575; border-radius: 10px; padding: 10px;")
        
        vbox = QVBoxLayout(frame)
        lbl_nombre = QLabel(f"🤖 {nombre}")
        lbl_nombre.setStyleSheet("font-weight: bold; border: none; color: white; font-family: 'Arial';")
        lbl_monto = QLabel("Oferta: $0")
        lbl_monto.setStyleSheet("border: none; color: white; font-family: 'Arial';")
        lbl_estado = QLabel("Esperando...")
        lbl_estado.setStyleSheet("border: none; color: white; font-family: 'Arial';")
        
        vbox.addWidget(lbl_nombre)
        vbox.addWidget(lbl_monto)
        vbox.addWidget(lbl_estado)
        
        # Guardamos la referencia del frame para iluminarlo
        self.widgets_participantes[id_bot] = (lbl_monto, lbl_estado, lbl_nombre, frame)
        
        pos = len(self.widgets_participantes) - 1
        self.grid_bots.addWidget(frame, pos // 3, pos % 3)
    
    @pyqtSlot(int)
    def actualizar_reloj(self, segundos):
        self.lbl_reloj.setText(f"Tiempo restante: {segundos}s")
        self.barra_progreso.setValue(segundos)

    @pyqtSlot(int, int, str)
    def actualizar_ui_bot(self, id_bot, monto, estado):
        if id_bot in self.widgets_participantes:
            lbl_monto, lbl_estado, lbl_nombre, frame = self.widgets_participantes[id_bot]
            lbl_monto.setText(f"Oferta: ${monto}")
            lbl_estado.setText(f"Estado: {estado}")

            if estado == "Aceptada":
                # 1. Resetear todos los demás frames a gris
                for _, _, n, f in self.widgets_participantes.values():
                    n.setStyleSheet("color: white; border: none")
                    f.setStyleSheet("border-radius: 10px; border: 2px solid #455575;")
                
                # 2. Iluminar SOLO este frame
                frame.setStyleSheet("border: 2px solid #6de0ff; border-radius: 10px;")
                lbl_estado.setStyleSheet("color: green; font-weight: bold; border: none;")
                lbl_nombre.setStyleSheet("color: #6de0ff; border: none;")
            else:
                lbl_estado.setStyleSheet("color: red; border: none;")


    @pyqtSlot(int, str)
    def actualizar_global(self, monto, nombre):
        self.lbl_oferta_grande.setText(f"Oferta Actual: ${monto} ({nombre}).")


    @pyqtSlot(str, int ,str)
    def finalizar_interfaz(self, ganador, precio, producto):
        self.container_buttons.setEnabled(True)
        self.lbl_ganador.setText(f"El/La postor/a {ganador} ha ganado un {producto} por el valor de {precio} dolares.")
        self.stacked_layout.setCurrentIndex(5)
    

    def limpiar_grid(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater() 
                else:
                    self.limpiar_grid(item.layout()) 


    def simulador(self):
        button = self.sender()
        button_txt = button.text().lower()
        match button_txt:
            case "si":
                print("Botón pestaña de iniciar simulación presionado")
                self.stacked_layout.setCurrentIndex(4)
                self.iniciar_simulacion()
            case "no":
                print("Botón pestaña de inicio presionado")
                self.stacked_layout.setCurrentIndex(0)

    
    def limpiar_log(self):
        try:
            open('log_subasta.txt', 'w').close() # Esto crea un Log aunque no exista y lo limpia...
            print("Log limpiado exitosamente!")
            QMessageBox.information(self,"Información","Log Limpiado Exitosamente!")
        except:
            print("¡No se pudo limpiar el log!")
            QMessageBox.critical(self, "¡Error","No se pudo limpiar el log!")
            

    def iniciar_simulacion(self):
        self.container_buttons.setEnabled(False)
        self.stacked_layout.setCurrentIndex(4)
        self.limpiar_grid(self.grid_bots)
        self.widgets_participantes.clear()
        
        # Configurar barra de progreso
        duracion_total = 15 
        self.barra_progreso.setMaximum(duracion_total)
        self.barra_progreso.setValue(duracion_total)

        prod = Producto("Iphone X", 100, "Iphone X")
        self.subasta_logica = SubastaGUI(prod, 1, duracion_total)
        
        # Conexiones
        self.subasta_logica.sig_actualizar_bot.connect(self.actualizar_ui_bot)
        self.subasta_logica.sig_actualizar_global.connect(self.actualizar_global)
        self.subasta_logica.sig_ganador.connect(self.finalizar_interfaz)
        self.subasta_logica.sig_nuevo_bot.connect(self.crear_card_participante)
        self.subasta_logica.sig_tiempo_restante.connect(self.actualizar_reloj) # Conexión del reloj
        
        # Registrar bots iniciales
        nombres = ["Juanito", "Pedrito", "Maria"]
        from Participantes import Participante
        for i, nombre in enumerate(nombres):
            p = Participante(i+1, nombre)
            self.crear_card_participante(p.id_participante, p.nombre)
            self.subasta_logica.registrar_participante(p)

        threading.Thread(target=self.subasta_logica.simular_subasta, daemon=True).start()
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    try:
        with open("style.qss", "r") as f:
            _style = f.read()
            app.setStyleSheet(_style)
    except:
        print("No se encontro ninguna hoja de estilos tipo qss")
    window = MainWindow()
    
    sys.exit(app.exec())