# 년도 데이터를 2023년 12월 이후 를 2024년 01월 데이터로 변경
import csv

input_file = 'E:\\daySum_백석1동_습도_20230111_20241130.csv'
output_file = 'E:\\DayData_백석1동_습도_20230111_20241130.csv'

# 변경할 값들 매핑
value_mapping = {
    '202313': '202401',
    '202314': '202402',
    '202315': '202403',
    '202316': '202404',
    '202317': '202405',
    '202318': '202406',
    '202319': '202407',
    '202320': '202408',
    '202321': '202409',
    '202322': '202410',
    '202323': '202411'
}

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8',
                                                                  newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 첫 번째 행(헤더) 처리
    headers = next(reader)
    writer.writerow(headers)  # 헤더 그대로 작성

    # 데이터 처리
    for row in reader:
        # 5번째 열 (index 4) 값을 확인하여 매핑된 값으로 바꿈
        if row[4] in value_mapping:
            row[4] = value_mapping[row[4]]

        writer.writerow(row)  # 수정된 행 작성

print(f"데이터가 {output_file}에 저장되었습니다.")