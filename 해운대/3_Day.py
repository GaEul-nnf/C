import csv

input_file = 'E:\\좌제3동_기온_202301_202411.csv'
output_file = 'E:\\day_좌제3동_기온_202301_202411.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8',
                                                                  newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 헤더 처리
    headers = next(reader)
    headers.append('Day')
    writer.writerow(headers)

    # 데이터 처리
    for row in reader:
        try:
            # 두 번째 열 값 처리
            if len(row) > 1:  # 두 번째 열이 존재할 경우
                second_column = row[1]
                if len(second_column) != 4:  # 4자리가 아닌 경우 패딩 처리
                    second_column = second_column.zfill(4)
                row[1] = second_column  # 패딩된 값 다시 저장
            else:  # 두 번째 열이 없을 경우
                row.append('0000')  # 기본값으로 추가
                second_column = '0000'

            # 첫 번째와 두 번째 열 데이터를 문자열로 결합
            combined_string = row[0] + second_column

            # 문자열 결합 결과를 숫자로 변환
            combined_number = int(combined_string)

            # 6자리로 맞춤 (0으로 패딩)
            formatted_result = f"{combined_number:06d}"  # 숫자를 6자리로 패딩

        except (ValueError, IndexError) as e:
            # 에러 발생 시 기본값 처리
            formatted_result = '000000'

        # 결과를 다섯 번째 열로 추가
        row.append(formatted_result)
        writer.writerow(row)

print(f"데이터가 {output_file}에 저장되었습니다.")
