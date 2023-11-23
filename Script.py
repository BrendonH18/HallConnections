from pathlib import Path
import PySimpleGUI as ui
import Helper as h



if __name__ == "__main__":
    crm_file = h.choose_crm_file()
    print(crm_file)