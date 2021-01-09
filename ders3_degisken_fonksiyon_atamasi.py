from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Ders 3 Uygulamasi")
        
        # Sabit Yazi ekleme
        yazi1 = QLabel("Baslik Ders 3!")
        font = yazi1.font()
        font.setPointSize(30)
        yazi1.setFont(font)
        yazi1.setAlignment(Qt.AlignVCenter | Qt.AlignTop)
        yazi2 = QLabel("bu yazi degisecek")
        yazi2.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        yazi2.setText("yazi2 degisti") #Bir argümani ayni yerde bir daha tanimlarsak son halini alir
        
        # Resim ekleme
        resim = QLabel("QLabel Resim icinde kullanilir")
        resim.setPixmap(QPixmap('Background-sade.jpg" loading="lazy" width="1920" height="1080'))
        resim.setScaledContents(False)
        
        # Tik ile Isaretleme Kutusu
        kutu1 = QCheckBox()
        kutu1.setCheckState(Qt.Checked)
        kutu1.stateChanged.connect(self.durum)
        
        #Kombobox Eklentisi
        kombo = QComboBox()
        kombo.addItems(["icerik1","icerik2","icerik3"])
        kombo.currentIndexChanged.connect(self.secim_degisti)
        kombo.currentIndexChanged[str].connect(self.yazi_degisti)
        '''combobox'a eklemeyi uygulamadan yapabilirsiniz. Bunun icin
        secim.setInsertPolicy(QComboBox.InsertAlpabetically)
        seklinde bir ekleme yapabilirsiniz. Icerigi sinirlandirmak icinde
        secim.setMaxCoun(10) gibi birsey yapilabilir.'''
        
        #Liste Eklentisi
        liste = QListWidget()
        liste.addItems(["liste1","liste2","liste3"])
        liste.currentItemChanged.connect(self.liste_degisti)
        liste.currentTextChanged.connect(self.liste_yazi)
        
        # Yazi yazma Satiri
        satir = QLineEdit()
        satir.setMaxLength(25)
        satir.setPlaceholderText("Buraya yazi girin")
        # satir.setReadOnly(True) < Yazilamasini önlemek isterseniz
        satir.returnPressed.connect(self.return_basildi)
        satir.selectionChanged.connect(self.satir_secimi)
        satir.textChanged.connect(self.satir_degisti)
        satir.textEdited.connect(self.satir_duzenlendi)

        ekler = [
            yazi1,
            yazi2,
            resim,
            kutu1,
            kombo,
            liste,
            satir
        ]

        arayuz = QVBoxLayout()
        for i in ekler:
            arayuz.addWidget(i)
        #Tum Widgetleri (eklentileri) listeden arayüze aktardik.
        ek = QWidget()
        ek.setLayout(arayuz)
        self.setCentralWidget(ek)

    
    # TANIMLAR
    #Tanimlar daha önce .connect ile baglantili hale geldi. 
    def durum(self, isaret):
        print(isaret == Qt.Checked)
        print("kutucuk durumu: ",isaret)

    def secim_degisti(self, icerik):
        print(icerik)

    def yazi_degisti(self, degisen_yazi):
        print(degisen_yazi)

    def liste_degisti(self, ldegisim):
        print(ldegisim.text())

    def liste_yazi(self, lyazi):
        print(lyazi)

    def return_basildi(self):
        print("Enter Tusuna basildi!")

    def satir_secimi(self):
        print("Satir Secim degisti")

    def satir_degisti(self, yeni_yazi):
        print("Yazi degisti")
        print(yeni_yazi)

    def satir_duzenlendi(self, y_yazi):
        print("Yazi duzenlendi")
        print(y_yazi)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
