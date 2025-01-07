import os

from gui import Gui

if __name__ == '__main__':
    # cx_Oracle.init_oracle_client(os.getcwd() + '\oracle_client')

    LOCATION = os.getcwd() + r'\oracle_client'
    os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

    Gui()
    pass
