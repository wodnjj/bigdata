import csv

# CSV 파일에 저장할 데이터
data = [
    ["이름", "나이", "성별"],
    ["홍길동", 20, "남성"],
    ["김영희", 25, "여성"],
    ["이철수", 30, "남성"]
]

# CSV 파일 열기
with open("data.csv", mode="w", newline="") as file:
    # CSV writer 생성
    writer = csv.writer(file)

    # 데이터 쓰기
    for row in data:
        writer.writerow(row)

print("CSV 파일 쓰기 완료")