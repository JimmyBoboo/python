import sys 
from PyQt6.QtWidgets import *

class hovedvindu(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 700, 700)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        min_label = QLabel()
        min_label.setText('Dette er en label')
        layout.addWidget(min_label, 0, 0)
        
        min_knapp = QPushButton('Min knapp')
        layout.addWidget(min_knapp, 0, 1)
        
        min_inputlinje = QLineEdit()
        min_inputlinje.setPlaceholderText("Enkel linje, dette er standardtekst")
        layout.addWidget(min_inputlinje, 0, 2)
        
        min_radioknapp = QRadioButton('Radioknapp')
        layout.addWidget(min_radioknapp, 1, 0)
        
        min_sjekkboks = QCheckBox('Avkrysningsboks')
        layout.addWidget(min_sjekkboks, 1, 1)
        
        min_combobox = QComboBox()
        min_combobox.setPlaceholderText('Velg ett av alternativene')
        min_combobox.addItem('Alternativ 1')
        min_combobox.addItem('Alternativ 2')
        min_combobox.addItem('Alternativ 3')
        layout.addWidget(min_combobox, 1, 2)
        
        min_tekst = QTextEdit()
        min_tekst.setPlaceholderText('Brkerinput, flere linjer')
        layout.addWidget(min_tekst, 2, 2)
        
        min_beskjed = QMessageBox()
        min_beskjed.setText('Dette er en beskjed')
        layout.addWidget(min_beskjed, 2, 0)
        
        min_slider = QSlider()
        min_slider.setRange(10, 80)
        layout.addWidget(min_slider, 2, 1)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    vindu = hovedvindu()
    
    sys.exit(app.exec())
