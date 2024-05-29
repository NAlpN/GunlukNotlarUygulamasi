import sys
import json
from PyQt5 import QtWidgets, QtGui
from gunluk import Ui_MainWindow

class GUNLUK(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(GUNLUK, self).__init__()
        self.gunluk = Ui_MainWindow()
        self.gunluk.setupUi(self)

        self.gorevleri_yukle()

        font = QtGui.QFont()
        font.setFamily("Bold")
        font.setPointSize(8)
        self.gunluk.yaz.setFont(font)
        
        self.setStyleSheet("background-color: #E2DCD7; color: white;")
        self.gunluk.yaz.setStyleSheet("""
            QLineEdit {
                background-color: #F1D4E4;
                color: Bold;
                font-family: Arial;
                font-weight: black;
                font-size: 12pt;
                border: 2px solid #444444;
                border-radius: 15px;
                padding: 5px;
            }
        """)

        self.list_widget_style(self.gunluk.gorevler)
        self.list_widget_style(self.gunluk.tamamlananGorevler)

        self.buton_style(self.gunluk.gorevEkle)
        self.buton_style(self.gunluk.gorevSil)
        self.buton_style(self.gunluk.tamamlananGorevler_2)        

        self.gunluk.gorevEkle.clicked.connect(self.gorev_ekle)
        self.gunluk.gorevSil.clicked.connect(self.gorev_sil)
        self.gunluk.tamamlananGorevler_2.clicked.connect(self.tamamlanan_gorevler)

    def list_widget_style(self, list_widget):
        list_widget.setStyleSheet("""
            QListWidget {
                background-color: #6A367A; 
                color: white;  
                font-family: Arial;
                font-weight: bold;
                font-size: 10pt;
                border: 2px solid #444444;
                border-radius: 15px; 
                padding: 5px;
            }
            QListWidget::item {
                padding: 5px;
            }
            QListWidget::item:selected {
                background-color: #384D67; 
                border-radius: 15px; 
            }
        """)

    def buton_style(self, button):
        button.setStyleSheet("""
            QPushButton {
                background-color: #AA64AA;
                border: 2px solid #AA64AA;
                border-radius: 15px;
                color: white;
                padding: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #E6B3E6;
                border: 2px solid #E6B3E6;
            }
            QPushButton:pressed {
                background-color: #AA7AAA;
                border: 2px solid #AA7AAA;
            }
        """)

    def gorevleri_yukle(self):
        try:
            with open("C:/Users/alpnn/Masaüstü/Python-Dosyaları/Günlük/gorevler.json", "r") as f:
                tasks = json.load(f)
                for task in tasks:
                    self.gunluk.gorevler.addItem(task)
        except FileNotFoundError:
            pass

    def gorevleri_kaydet(self):
        tasks = [self.gunluk.gorevler.item(i).text() for i in range(self.gunluk.gorevler.count())]
        with open("C:/Users/alpnn/Masaüstü/Python-Dosyaları/Günlük/gorevler.json", "w") as f:
            json.dump(tasks, f)

    def gorev_ekle(self):
        gorev_yaz = self.gunluk.yaz.text()
        if gorev_yaz:
            self.gunluk.gorevler.addItem(gorev_yaz)
            self.gunluk.yaz.clear()
            self.gorevleri_kaydet()
    
    def tamamlanan_gorevler(self):
        tamamlanan_gorev = self.gunluk.gorevler.selectedItems()
        if tamamlanan_gorev:
            for item in tamamlanan_gorev:
                self.gunluk.tamamlananGorevler.addItem(item.text())
                self.gunluk.gorevler.takeItem(self.gunluk.gorevler.row(item))
            self.gorevleri_kaydet()

    def gorev_sil(self):
        silinen_gorev = self.gunluk.gorevler.selectedItems()
        if silinen_gorev:
            for item in silinen_gorev:
                self.gunluk.gorevler.takeItem(self.gunluk.gorevler.row(item))
        silinen_gorev2 = self.gunluk.tamamlananGorevler.selectedItems()
        if silinen_gorev2:
            for item in silinen_gorev2:
                self.gunluk.tamamlananGorevler.takeItem(self.gunluk.tamamlananGorevler.row(item))
        self.gorevleri_kaydet()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = GUNLUK()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()