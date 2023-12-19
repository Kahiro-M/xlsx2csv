import pathlib
import pandas as pd

def toCsv(inputFile):
    outputFile = inputFile.rsplit('.', 1)[0] + '.csv'
    pd.read_excel(inputFile).to_csv(outputFile)



# 使用例
inputFile = input("変換したいファイルのパスを入力してください: ")

toCsv(inputFile)
