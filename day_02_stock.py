import os

print("Current working directory:" , os.getcwd())

# 거래량 기준 설정 : 'standard_volume' 최소 거래량입니다.
standard_volume = 30000
# 낮은 거래량 기준 
volume_too_low = 10000

# 결과를 저장할 리스트 초기화 
target_dates = [] # 목표 거래량 이상인 날짜 저장 
end_price_target_dates = [] # 목표 거래량 이상일 때의 종가 저장
ends = [] # 모든 종가 저장 
ma3_end = [] # ma3를 저장할 리스트


# 파일을 순차적으로 읽어 들입니다. 예를 들어, stock1.txt 부터 stock4.txt 까지

for i in range(1,5):
    #파일 이름을 설정합니다. 여기서는 디렉토리 경로를포함합니다.
    file_name = f"./stock_practice/stock{i}.txt"

    with open(file_name, "r", encoding="utf-8") as f:
        entire_txt = f.read() # 전체 텍스트를 읽어 들입니다.

    lines = entire_txt.split("\n") # 각 행을 분리하여 리스트로 만듭니다.

    lines_values = lines[1:] # 첫번째 행은 헤더이므로 제외합니다.

    for line in lines_values:
        values = line.split(",") # 각 행을 분리하여 리스트로 만듭니다.
        date, start, high, low, end, volume, amount, fluc_rate = values

        # 거래량이 기준보다 높으면 해당 날짜와 종가를 저장합니다.
        if int(volume) > standard_volume:
            print(f"At {date}, trading volume is larger than target")
            target_dates.append(date)
            end_price_target_dates.append(int(end))
        elif int(volume) < volume_too_low:
            print(f"At {date}, trading volume is too low")
        
        # 모든 종가를 저장합니다.
        ends.append(int(end))

#종가의 3일 이동 평균을 계산합니다.
for j in range(len(ends)):
    if j > 2:
        moving_avg = (ends[j-2]+ends[j-1]+ends[j])/3
        ma3_end.append(moving_avg)


# 목표 거래량을 초과하는 날짜의 종가 평균을 계산합니다.
        
mean_target_end = sum(end_price_target_dates)/len(end_price_target_dates)

# 결과를 파일로 저장합니다.
# 목표 날짜를 저장하는 파일 
with open('target_dates.txt',"w", encoding='utf-8') as f:
    for date in target_dates:
        f.write(f"{date}\n")

# 이동 평균을 저장하는 파일 
with open("target_ma.txt","w",encoding="utf-8")as f:
    for ma in ma3_end:
        f.write(f"{ma}\n")





    