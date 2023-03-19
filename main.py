import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCalendarWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QDate
from EthqInfo import EthqInfo

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        start_label = QLabel('Başlangıç Tarihi:', self)
        self.start_calendar = QCalendarWidget(self)

        end_label = QLabel('Bitiş Tarihi:', self)
        self.end_calendar = QCalendarWidget(self)

        self.submit_button = QPushButton('Kaydet')
        self.submit_button.clicked.connect(self.submit)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(start_label)
        hbox1.addWidget(self.start_calendar)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(end_label)
        hbox2.addWidget(self.end_calendar)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.submit_button)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Tarih Girişi')
        self.show()


    def submit(self):
        start_date = self.start_calendar.selectedDate().toString('yyyy-MM-dd')
        end_date = self.end_calendar.selectedDate().toString('yyyy-MM-dd')
        print('Başlangıç Tarihi:', start_date)
        print('Bitiş Tarihi:', end_date)
        ethqinfo = EthqInfo
        ethqinfo.infoethq(start_date, end_date)




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
