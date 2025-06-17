import pathlib
import pandas as pd
import enc
import sys

def toXlsx(inputFile):
    # 出力ファイル名を .xlsx に変更
    outputFile = pathlib.Path(inputFile).with_suffix('.xlsx')

    # CSVを読み込んでXLSXに変換
    pd.read_csv(inputFile, dtype=str, encoding=enc.detectEncoding(inputFile)).to_excel(outputFile,index=False)


if __name__ == '__main__':
    print('====== csv -> xlsx ======')
    if(len(sys.argv)<2):
        # 使用例
        inputFile = input("変換したいCSVファイルのパスを入力してください: ")
    else:
        inputFile = sys.argv[1]
    toXlsx(inputFile)