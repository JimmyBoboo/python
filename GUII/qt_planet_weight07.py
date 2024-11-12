import sys, random
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QFormLayout, QComboBox, QDoubleSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon


planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

planetbilder = ['GUII/bilder/sun.png', 'GUII/bilder/merkur.png', 'GUII/bilder/venus.jpg', 'GUII/bilder/jorden.png', 'GUII/bilder/mars.png', 'GUII/bilder/mars.png', 'GUII/bilder/jupiter.png',
                'GUII/bilder/saturn.png', 'GUII/bilder/uranus.png', 'GUII/bilder/neptun.png']

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        # Setter tittel og størrelse på vinduet, og legger også til et ikon
        self.setWindowTitle('Planetvekt')
        self.setGeometry(100, 100, 500, 400)
        vinduicon = QIcon('GUII/bilder/sun.png')
        self.setWindowIcon(vinduicon)

        # Oppretter et gridlayout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Lager en label som skal plasseres øverst i layoutet
        self.topplabel =QLabel()
        self.topplabel.setText("Hva er din vekt på en annen planet?")
        self.layout.addWidget(self.topplabel, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)  # 0,0 er koordinatene, 1 er antall rader topplabel skal strekke seg over, og 2 er antall kolonner den skal strekke seg over. alignment sentrerer widgeten .

        # TODO: skjema, bilder, hendelser, metoder

        self.skjema = QFormLayout()
        
        self.meny_combobox = QComboBox()
        self.meny_combobox.setPlaceholderText("Velg en planet...")
        self.meny_combobox.addItem("Tilfeldig planet")
        for planet in planeter:
            self.meny_combobox.addItem(planet)
        self.meny_combobox.activated.connect(self.oppdater_bilde)
        self.skjema.addRow(self.meny_combobox)
        
        
        self.layout.addLayout(self.skjema, 1, 0)
        
        self.vekt_input = QDoubleSpinBox()
        self.vekt_input.setPrefix("Din vekt i kg: ")
        self.vekt_input.setDecimals(1)
        self.skjema.addRow(self.vekt_input)
        
        self.regnutknapp = QPushButton("Regn ut")
        self.regnutknapp.connect(self.regn_ut)
        
        self.skjema.addRow(self.regnutknapp)
        
        # self.layout.addLayout(self.skjema, 1, 0)
        
        self.bildelabel = QLabel()
        self.pixmap = QPixmap("GUII/bilder/sun.png")
        self.pixmap = self.pixmap.scaled(256, 256)
        self.bildelabel.setPixmap(self.pixmap)
        
        self.layout.addWidget(self.bildelabel, 1, 1)
        
        self.bunnlabel = QLabel("Velg en planet og skriv inn vekten din")
        # self.bunnlabel = QLabel("Velg en planet og skriv inn vekten din!")
        # self.layout.addWdiget(self.bunnlabel, 2, 0, 1, alignment=Qt.AlignmentFlag)
        
        
        
        self.show()                                                 # Må være med for at vinduet skal vises

    def oppdater_bilde(self):
        self.pixmap = QPixmap(planetbilder[self.meny_combobox.currentIndex()])
        self.pixmap = self.pixmap.scaled(256, 256)
        self.bildelabel.setPixmap(self.pixmap)    
        
    def regn_ut(self):
        self.planetnummer = self.meny_combobox.currentIndex()
        
        if self.planetnummer == 0:
            self.planetnummer = random.randrange(0, len(planeter))
            self.ny_vekt = beregn_vekt(self.vekt_input.value(), tyngdekraft [self.planetnummer] ) 
            self.bunnlabel.setText(f"Du fikk planeten {planeter[self.planetnummer]}, Din vekt på denne planeten, med tyngdekraft {tyngdekraft[self.planetnummer]}ville vært {self.ny_vekt} kg")
            self.pixmap =QPixmap(planetbilder[self.planetnummer + 1])
            self.pixmap = self.pixmap.scaled(256, 256)
            self.bildelabel.setPixmap(self.pixmap)

        else:
            self.ny_vekt = beregn_vekt(self.vekt_input.value(), tyngdekraft [self.planetnummer -1])
            self.bunnlabel.setText(f"Din vekt på planeten {planeter[self.planetnummer -1]}, med tyngdekraft {tyngdekraft[self.planetnummer -1]} m/s^2 er {self.ny_vekt} kg.")
            
        
def beregn_vekt(din_vekt, planettyngdekraft, jordtyngdekraft=9.07):
    beregn_vekt = din_vekt /jordtyngdekraft * planettyngdekraft
    return round(beregn_vekt, 1)
    
    
# Må alltid med:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    vindu = Hovedvindu()
    sys.exit(app.exec())


