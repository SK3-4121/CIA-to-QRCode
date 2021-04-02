import os
import sys
import time
import wget
import socket
import qrcode
import tkinter
import colorama
import pyqrcode
import threading
import webbrowser

from pyqrcode import QRCode
from tkinter import *
from PIL import ImageTk, Image

print("Made by SK3#3160 | Open source")

port = input("[*]: What do you the port to be *default is 8000 | and it has to be between 0-9999*: ")
IPAddr = socket.gethostbyname(socket.gethostname())
colorama.init()
cia_name = None
code = None

def check_files():
    try:
        os.system("cls")
        if os.path.exists(str("QR_codes")) and os.path.exists(str("cia")):
            pass
        else:
            os.system("mkdir cias")
            os.system("mkdir QR_codes")
        os.system("cls")
    except:
        pass

def Display_SVG():
    from PySide2 import QtCore, QtGui, QtWidgets
    from PySide2.QtNetwork import QNetworkProxy, QNetworkProxyFactory
    from PySide2.QtWebEngineWidgets import QWebEngineView
    class DisplaySVG(QtWidgets.QWidget):
        "I stole this from: https://stackoverflow.com/questions/63139025/display-svg-file-in-python"
        def __init__(self, url=None, parent=None):
            super().__init__(parent)
            self.resize(600,600) # fix this size
            self.verticalLayout = QtWidgets.QVBoxLayout(self)
            self.webview = QWebEngineView(self)
            self.verticalLayout.addWidget(self.webview)
            self.setWindowTitle("QR Code")
            act = QtWidgets.QAction("Close", self)
            act.setShortcuts([QtGui.QKeySequence(QtCore.Qt.Key_Escape)])
            act.triggered.connect(self.close)
            self.addAction(act)
            cia_file = open(r"QR_codes" + cia_name + ".svg",'r')
            svg = cia_file.read()
            self.webview.setHtml(svg)
    qt_app = QtWidgets.QApplication(sys.argv)
    disp = DisplaySVG()
    disp.show()
    qt_app.exec_()

def start_server():
    def start_se():
        python_command = "python -m http.server " + port
        webbrowser.open("http://" + IPAddr + ":" + port + "/cias")
        os.system(python_command)
    my_thread = threading.Thread(target=start_se)
    my_thread.start()

def gen_qr_code(name):
    global cia_name
    new_name = name[30:9999]
    cia = open("cias\\" + new_name + ".cia",'r')
    n_name = str(cia.name)
    newest_name = n_name[4:9999]
    cia_name = newest_name
    link = str("http://" + IPAddr + ":" + port + "/cias/" + newest_name)
    convert = pyqrcode.create(link)
    convert.svg("QR_codes\\" + newest_name + ".svg", scale=10)

def check_if_link(str):
    first_char = str[0:4]
    if first_char == "http":
        return "link"
    else:
        return "not a link"

def find_problem():
    def fetch_code():
        global code
        if code == "101":
            return "Server/Link was not responding"
    fetch_code()
    print(colorama.Fore.RED + f"[-]: Error {fetch_code()}" + colorama.Fore.RESET)

def install_cia(link):
    global code
    global cia_name
    def check_type(link):
        global code
        global cia_name
        cia_name_n, cia_type = os.path.splitext(link)
        cia_name = cia_name_n
        if str(cia_type) == ".cia":
            return "is cia"
        else:
            code = "101"
            return "other"
    if str(check_type(link)) == "is cia":
        def start_install(link):
            try:
                print(colorama.Fore.BLUE)
                print(wget.download(link,"cias"))
                print(colorama.Fore.RESET)
            except:
                code == "101"
        start_install(link)
    else:
        return "Problem"

print(colorama.Fore.YELLOW)
cia = None
From_cia = input("[*]: Link of cia: ")
print(colorama.Fore.RESET)
check_files()
if check_if_link(From_cia) == "link":
    if install_cia(From_cia) == "Problem":
        find_problem()
    else:
        print(colorama.Fore.GREEN + "\nSuccessfully hosted the cia and converted!" + colorama.Fore.RESET)
        gen_qr_code(cia_name)
        start_server()
        Display_SVG()