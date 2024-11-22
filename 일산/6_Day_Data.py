# 원본 파일과 동일하게 날자 데이터를 합침
import csv

input_file = 'E:\\테스트_백석1동_습도_20230111_20241031.csv'
output_file = 'E:\\최종_백석1동_습도_20230111_20241031.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8',
                                                                  newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 첫 번째 행(헤더) 처리
    headers = next(reader)
    writer.writerow(headers)  # 헤더 그대로 작성

    # 데이터 처리
    for row in reader:
        # 5번 열 (index 4)과 6번 열 (index 5)의 값 가져오기
        column_5_value = row[4]
        column_6_value = row[5]

        # 5번 열의 값이 5자리 숫자라면, 앞에 0을 추가하여 6자리로 만들기
        if len(column_5_value) == 5:
            column_5_value = column_5_value.zfill(6)

        # 6번 열의 값이 앞에, 5번 열의 값이 뒤에 오도록 결합
        new_value = column_6_value + column_5_value

        # 새 값을 마지막 열에 추가
        row.append(new_value)

        writer.writerow(row)

print(f"데이터가 {output_file}에 저장되었습니다.")