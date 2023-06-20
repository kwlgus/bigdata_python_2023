# CSV 파일 읽기
import csv

csvfile = '충청북도_푸드뱅크현황.csv' #'부산광역시_시내버스_이용건수.csv'
dirname = './Day03/'

# \ufeff가 붙어있는 경우 encording='utf-8-sig'로 변경
fr = open(f'{dirname}{csvfile}', mode='rt', encoding='utf-8-sig') # 한국어는 기본이 cp949 (코드페이지949)
reader = csv.reader(fr, delimiter=',') # 구분자가 ,일 경우

for line in reader:
    print(line)

fr.close()