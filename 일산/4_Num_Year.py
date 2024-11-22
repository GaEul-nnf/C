# 202301부터 년도와 월 데이터 추가
import csv

input_file = 'E:\\output_백석1동_습도_20230111_20241031.csv'
output_file = 'E:\\test_백석1동_습도_20230111_20241031.csv'

# 시작 값
base_value = 202301
last_value = base_value  # 처음 시작 값을 last_value로 설정
skip_count = 0  # 첫 번째 열에서 1을 감지한 후 건너뛰는 행의 개수
is_base_value_set = False  # base_value가 설정되었는지 여부를 추적

# CSV 파일 읽고 수정하기
with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8',
                                                                  newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 첫 번째 행(헤더) 처리
    headers = next(reader)
    writer.writerow(headers)  # 헤더 그대로 작성

    # 데이터 처리
    for row in reader:
        if not is_base_value_set:
            # 첫 번째 열에서 1을 감지하고, base_value는 202301에서 202302로 설정
            if row[0] == '1':
                row.append(str(base_value + 1))  # 첫 번째 1 감지 시, 202302 사용
                last_value = base_value + 1  # 현재 값으로 설정
                base_value += 1  # base_value 증가
                skip_count = 1  # 1이 감지되면 그 다음부터 150개까지는 건너뛰기 시작
                is_base_value_set = True  # base_value 설정 완료
            else:
                # 첫 번째 열이 1이 아닌 경우, 이전의 last_value 값을 사용
                row.append(str(last_value))  # 이전 값을 추가
        else:
            if skip_count < 150:
                # 첫 번째 열이 1이 아닐 때, 이전의 last_value 값을 사용
                row.append(str(last_value))  # 이전 값을 계속 사용
                skip_count += 1  # 150개 행 카운트
            else:
                # 150개의 행을 처리한 후에는 다시 첫 번째 열에서 1을 감지할 때까지 동일한 값 사용
                if row[0] == '1':
                    row.append(str(base_value + 1))  # 첫 번째 1 감지 시, 202302 사용
                    last_value = base_value + 1  # 현재 값으로 설정
                    base_value += 1  # base_value 증가
                    skip_count = 1  # 1이 감지되면 그 다음부터 150개까지는 건너뛰기 시작
                else:
                    row.append(str(last_value))  # 이전 값을 계속 사용

        writer.writerow(row)  # 수정된 행 작성

print(f"데이터가 {output_file}에 저장되었습니다.")