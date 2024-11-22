# 날짜, 시, 분 을 정리해서 새로운 열에 저장
import csv

input_file = 'E:\\업무지시\\six_백석1동_기온_20230111_20241031.csv'
output_file = 'E:\\업무지시\\output_백석1동_기온_20230111_20241031.csv'

cyclic_values = [00, 10, 20, 30, 40, 50]

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8',
                                                                  newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 헤더 처리
    headers = next(reader)  # 첫 번째 행(헤더)을 읽음
    headers.append('Result')  # 새로운 열 이름 추가
    writer.writerow(headers)  # 헤더를 새 파일에 씀

    # 데이터 처리
    index = 0  # 순환 값의 인덱스
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

            # 순환 값 추가
            cyclic_value = cyclic_values[index % len(cyclic_values)]
            result = combined_number + cyclic_value  # 결과 계산

            # 6자리로 맞춤 (0으로 패딩)
            formatted_result = f"{result:06d}"  # 숫자를 6자리로 패딩

        except (ValueError, IndexError) as e:
            # 에러 발생 시 기본값 처리
            formatted_result = '000000'

        # 결과를 다섯 번째 열로 추가
        row.append(formatted_result)
        writer.writerow(row)
        index += 1  # 다음 순환 값으로 이동

print(f"데이터가 {output_file}에 저장되었습니다.")