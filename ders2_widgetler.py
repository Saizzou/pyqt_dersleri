from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# sistemsel argümanlara ulasim icin gerekli
import sys

''' 
Subclass QMainWindow MainWindow'un icerigini düzenlemek icin olusturuldu.
QMainWindow arayüzü olusturan elemandir. MainWindows bizim tanimladigimiz
Ana Pencere ismi. MainWindow yerine AnaPence adinda class ismide verebilirdik.
'''
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #layout = arayuz demektir. Widget = eklenti demektir.
        #Karmasa olmasin diye degisken isimlerinin birkacini
        #inglizce olarak biraktim. Aradaki farki rahat görün diye.

        self.setWindowTitle("Ikinci Ders Uygulamasi")

        arayuz = QVBoxLayout() #Icerik Alani olusturduk
        eklentiler = [QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit]
            #Tüm Widgetleri bir listeye ekledik

        for e in eklentiler:
            layout.addWidget(e())
            #Widget Listemizdeki herseyi layput Alanina ekliyoruz.

        widget = QWidget()
        widget.setLayout(arayuz)
        self.setCentralWidget(widget)
        # QWidget bizim eklenti fonksiyonumuz. Bunu sabit isme atadik.
        # Eklenti Fonksiyonuna arayüz ekle dedik ve Fonksiyon'a arayüzü eklemis
        # olduk. Eklenti Fonksiyonunu ortalanmis Eklenti olarak belirledik.

'''        
Burada PyQT5 kütüphanesinden uygulama calistiricisini cagiriyoruz.
icine ise sistemsel argümanlari atiyoruz böylece uygulamamiz sistemimiz
ile beraber calisabilir bir ortam olusturmus oluyoruz. Eger Uygulama
sadece kendi icinde calisacak ise yani bilgisayarimiz ile herhangi bir
bilgi alisverisi yapmayacak ise QApplication() seklinde de kullanilabilir.
'''
app = QApplication(sys.argv)

pencere = MainWindow()
pencere.show()
'''
Sadece bir Pencere fonksiyonu cagirmamiz yetmez!! Standart olarak
pencereleri olusturdugumuz an bu pencereler arka planda calisir
ve show() komutu ile pencereyi görünür yapmis oluyoruz!
'''

# Uygulama döngüsünü baslatiyoruz.
app.exec_()
'''
Uygulama kapanana kadar app.exec_() altindaki satirlara döngü
yüzünden erisemez! app.exec_() altinda olan kodlamalar sadece
Uygulama kapatilirsa okunur yada calistirilir!
'''