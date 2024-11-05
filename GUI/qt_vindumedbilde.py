from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
import sys

# Lager en klasse, Vindu, som skal arve fra klassen QWidget.
# Denne klassen er tenkt å inneholde all kode for å lage GUI for vinduet vårt.
class Vindu(QWidget):

    def __init__(self):
        super().__init__()                      
        self.setWindowTitle('Enkelt vindu')     
        self.resize(300, 300)                  

        label1 = QLabel()                      
        label1.setText("Hello world!")          

        label_img = QLabel()                    
        pixmap = QPixmap('pony.jpg')            
        label_img.setPixmap(pixmap) 
                    




app = QApplication(sys.argv)                   
vindu = Vindu()                                
vindu.show()                                    
sys.exit(app.exec())                            

# To be continued..