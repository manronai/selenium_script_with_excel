import pandas as pd
import openpyxl
from selenium_script_3rd import fetch_today_name
from selenium_script_4th import update_file
today = fetch_today_name()
print(today)
df = pd.read_excel('Excel_copy.xlsx', sheet_name=today)
list_of_today = list(df['Unnamed: 2'][1:])
def save_at_once(longest_sentences, shortest_sentences):
    df.iloc[1:, 3] = longest_sentences
    df.iloc[1:, 4] = shortest_sentences
def save_one_by_one(lg_sent, sh_sent, row):
    df.iloc[row, 3] = lg_sent
    df.iloc[row, 4] = sh_sent
def save_excel_file():
    df.to_excel('Excel_testing.xlsx',sheet_name=today, index=False)
    update_file(today)
def show_df():
    print('long')
    print(df.iloc[1:, 3])
    print('short')
    print(df.iloc[1:, 4])