import pathlib
import pandas as pd

def toCsv(inputFile):
    outputFile = inputFile.rsplit('.', 1)[0] + '.csv'
    pd.read_excel(inputFile, dtype=str).fillna('').replace('nan','').to_csv(outputFile,encoding="utf_8_sig",index=False)



# 使用例
inputFile = input("変換したいファイルのパスを入力してください: ")

toCsv(inputFile)
