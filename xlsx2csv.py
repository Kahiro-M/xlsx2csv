import pathlib
import pandas as pd
import sys

def toCsv(inputFile):
    outputFile = inputFile.rsplit('.', 1)[0] + '.csv'
    pd.read_excel(inputFile, dtype=str).fillna('').replace('nan','').to_csv(outputFile,encoding="utf_8_sig",index=False)



if __name__ == '__main__':
    print('====== xlsx -> csv ======')
    if(len(sys.argv)<2):
        # 使用例
        inputFile = input("変換したいxlsxファイルのパスを入力してください: ")
    else:
        inputFile = sys.argv[1]
    toCsv(inputFile)
