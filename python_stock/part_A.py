# os 모듈을 임포트하여 운영체제와 상호 작용할 수 있습니다.
import os

# 현재 작업 디렉토리를 출력합니다. 이는 스크립트가 실행되는 위치를 확인하기 위함입니다.
print("Current working directory:", os.getcwd())

# 거래량 기준 설정: 'standard_volume'은 관심을 가질 최소 거래량입니다.
standard_volume = 30000
# 'volume_too_low'는 너무 낮은 거래량을 나타내는 기준입니다.
volume_too_low = 10000

# 결과를 저장할 리스트 초기화
target_dates = []  # 목표 거래량 이상인 날짜 저장
end_price_target_dates = []  # 목표 거래량 이상일 때의 종가 저장
ends = []  # 모든 종가 저장
ma3_end = []  # 종가의 3일 이동평균 저장


# 파일을 순차적으로 읽어 들입니다. 예를 들어, stock1.txt 부터 stock4.txt까지
for i in range(1, 4+1):
    # 파일 이름을 설정합니다. 여기서는 디렉토리 경로를 포함합니다.
    file_name = f"./stock_practice/stock{i}.txt"

    # 파일을 열고, 전체 내용을 읽은 다음 파일을 닫습니다.
    with open(file_name, "r", encoding="utf-8") as f:
        entire_txt = f.read()

    # 텍스트를 줄바꿈 기호에 따라 분리합니다.
    lines = entire_txt.split("\n")
    # 첫 줄(헤더)을 제외한 나머지 줄만 처리합니다.
    lines_values = lines[1:]
    
    # 각 줄을 처리합니다.
    for line in lines_values:
        values = line.split(",")
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

# 종가의 3일 이동 평균을 계산합니다.
for j in range(len(ends)):
    if j > 2:
        moving_avg = (ends[j-2] + ends[j-1] + ends[j]) / 3
        ma3_end.append(moving_avg)

# 목표 거래량을 초과하는 날짜의 종가 평균을 계산합니다.
mean_target_end = sum(end_price_target_dates) / len(end_price_target_dates)

# 결과를 파일로 저장합니다.
# 목표 날짜를 저장하는 파일
with open("target_dates.txt", "w", encoding="utf-8") as f:
    for date in target_dates:
        f.write(f"{date}\n")

# 이동 평균을 저장하는 파일
with open("target_ma.txt", "w", encoding="utf-8") as f:
    for ma in ma3_end:
        f.write(f"{ma}\n")
