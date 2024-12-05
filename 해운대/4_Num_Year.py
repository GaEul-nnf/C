import csv

input_file = 'E:\\day_좌제3동_습도_202301_202411.csv'
output_file = 'E:\\daySum_좌제3동_습도_202301_202411.csv'

# 시작 값
base_value = 202301
current_value = base_value  # 현재 처리 중인 값
skip_count = 0  # "1" 감지 이후 건너뛰는 행 카운트
is_first_detected = False  # 첫 번째 "1" 감지가 완료되었는지 여부

# CSV 파일 읽고 수정하기
with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8',
                                                                  newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 첫 번째 행(헤더) 처리
    headers = next(reader)
    headers.append('YearMonth')  # 'Year' 대신 'YearMonth'로 더 명확히 이름 지정
    writer.writerow(headers)

    # 데이터 처리
    for row in reader:
        if not is_first_detected:
            # 첫 번째 열에서 "1"을 감지하면 현재 값을 추가
            if row[0] == '1':
                row.append(str(current_value))  # 현재 년월 값 추가
                is_first_detected = True  # 첫 번째 "1" 감지 완료
                skip_count = 1  # 건너뛰기 시작
            else:
                row.append(str(current_value))  # 초기값 유지
        else:
            if skip_count < 150:
                # "1" 이후 150개 행 동안 동일한 값 유지
                row.append(str(current_value))
                skip_count += 1
            else:
                # 150개 행 이후 "1" 감지 시 값을 증가
                if row[0] == '1':
                    current_value += 1  # 다음 년월로 이동
                    row.append(str(current_value))  # 새로운 값 추가
                    skip_count = 1  # 다시 건너뛰기 시작
                else:
                    row.append(str(current_value))  # 현재 값 유지

        writer.writerow(row)  # 수정된 행 작성

print(f"데이터가 {output_file}에 저장되었습니다.")
