from pathlib import Path
import PySimpleGUI as ui
import Helper as h
import pandas as pd

def RetrieveActivity(file):
    return pd.read_excel(io=file, sheet_name="Activity Log")
def RetrievePeople(file):
    return pd.read_excel(io=file, sheet_name="People")
def RetrieveAll(file):
    return pd.ExcelFile(file)

class ActivityModel():

    pass

class DatabaseManager(object):
    def __init__(self, file):
        temp = pd.ExcelFile(file)
        self.crm_file = temp

class ActivityManager(DatabaseManager):
    def __init__(self, crm_file):
        super().__init__(file=crm_file)
        self.sheet_name = "Activity Log"
        temp = pd.read_excel(io=self.crm_file, sheet_name=self.sheet_name).drop(columns=["Unnamed: 0"])
        self.df = temp

    def WriteActivity(self, note: str):
        NewEntry = pd.DataFrame({
            'ID': [self.df.index.max() + 2],
            'IDPerson': 2,
            'Notes': note
        })
        self.df = pd.concat([self.df, NewEntry], ignore_index=True)
        self.df.to_excel(self.crm_file, sheet_name=self.sheet_name)


if __name__ == "__main__":
    crm_file = h.choose_crm_file()
    # ActivityLog = RetrieveActivity(crm_file)
    # People=RetrievePeople(crm_file)
    Activity = ActivityManager(crm_file)
    Activity.WriteActivity("NEW NOTE!")