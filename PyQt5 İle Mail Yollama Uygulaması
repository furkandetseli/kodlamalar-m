from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
import sys

mailim=list()

class giris(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()
        self.sifre=QLineEdit()
        self.mail=QLineEdit()
        self.mailtext=QLabel("Mailinizi giriniz")
        self.sifretext=QLabel("\nŞifrenizi giriniz")
        self.giris=QPushButton("Giriş Yap")
        self.hata=QLabel("")
        v_box=QVBoxLayout()
        v_box.addWidget(self.mailtext)
        v_box.addWidget(self.mail)
        v_box.addStretch()
        v_box.addWidget(self.sifretext)
        v_box.addWidget(self.sifre)
        v3_box=QVBoxLayout()
        v3_box.addStretch()
        v3_box.addWidget(self.giris)
        v3_box.addWidget(self.hata)
        v3_box.addStretch()
        h_box=QHBoxLayout()
        h_box.addLayout(v_box)
        h_box.addLayout(v3_box)
        self.setLayout(h_box)
        self.setWindowTitle("Giriş Paneli")
        self.giris.clicked.connect(self.control)
        self.show()
    def control(self):
        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.mail.text(),self.sifre.text())
            self.hata.setText("Giris Başarılı!")
            self.kaydet()
        except:
            self.hata.setText("Hata!")
    def kaydet(self):
        mailim.append(self.mail.text())
        sorgu="Select * from mailler where mail=?"
        self.cursor.execute(sorgu,(self.mail.text(),))
        liste=self.cursor.fetchall()
        if len(liste)==0:
            sorgu2="Insert into Mailler Values(?,?)"
            self.cursor.execute(sorgu2,(self.mail.text(),self.sifre.text()))
            self.bağlantı.commit()
            self.ana = ana()

        else:
            self.ana = ana()

    def setup(self):
        self.bağlantı=sqlite3.connect("Mailler.db")
        self.cursor=self.bağlantı.cursor()
        sorgu=("CREATE TABLE IF NOT EXISTS Mailler(mail TEXT,şifre TEXT)")
        self.cursor.execute(sorgu)
        self.bağlantı.commit()

class ana(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()
        self.alıcı=QLineEdit()
        self.alıcıtext=QLabel("Alıcı")
        self.konu=QLineEdit()
        self.konutext=QLabel("Konu")
        self.mesaj=QTextEdit()
        self.mesajtext=QLabel("Mesaj")
        self.gönder=QPushButton("Gönder")
        self.temizle=QPushButton("Temizle")
        self.hata=QLabel("")

        v_box=QVBoxLayout()
        v_box.addWidget(self.alıcıtext)
        v_box.addWidget(self.alıcı)

        v1_box=QVBoxLayout()
        v1_box.addWidget(self.konutext)
        v1_box.addWidget(self.konu)

        v2_box=QVBoxLayout()
        v2_box.addWidget(self.mesajtext)
        v2_box.addWidget(self.mesaj)

        v3_box=QVBoxLayout()
        v3_box.addLayout(v_box)
        v3_box.addStretch()
        v3_box.addLayout(v1_box)
        v3_box.addStretch()
        v3_box.addLayout(v2_box)

        v4_box=QVBoxLayout()
        v4_box.addStretch()
        v4_box.addWidget(self.hata)
        v4_box.addWidget(self.gönder)
        v4_box.addWidget(self.temizle)
        v4_box.addStretch()

        h_box=QHBoxLayout()
        h_box.addLayout(v3_box)
        h_box.addLayout(v4_box)
        self.setLayout(h_box)
        self.gönder.clicked.connect(self.send)
        self.temizle.clicked.connect(self.clear)
        self.show()
    def setup(self):
        self.bağlantı=sqlite3.connect("Mailler.db")
        self.cursor=self.bağlantı.cursor()
        sorgu=("CREATE TABLE IF NOT EXISTS Mailler(mail TEXT,şifre TEXT)")
        self.cursor.execute(sorgu)
        self.bağlantı.commit()
    def send(self):
        self.cursor.execute("Select * from Mailler where mail=?",(mailim[0],))
        liste=self.cursor.fetchall()
        maili=liste[0][0]
        sifre=liste[0][1]
        mesaj=MIMEMultipart()
        mesaj["From"]=maili
        mesaj["To"]=self.alıcı.text()
        mesaj["Subject"]=self.konu.text()
        yazı=str(self.mesaj.toPlainText())
        mesajgovde=MIMEText(yazı,"plain")
        mesaj.attach(mesajgovde)
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(maili,sifre)
        try:
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            self.hata.setText("Gönderme başarılı.")
            self.mesaj.clear()
            self.konu.clear()
        except:
            self.hata.setText("Hata, gönderme başarısız...")
    def clear(self):
        self.alıcı.clear()
        self.konu.clear()
        self.mesaj.clear()


app=QApplication(sys.argv)
giris=giris()
sys.exit(app.exec_())

