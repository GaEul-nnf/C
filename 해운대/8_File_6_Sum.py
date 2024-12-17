import pandas as pd
import os

# 병합할 파일 목록
file_paths = [
    'E:\\해운대\\합본_enenF_2024_01_sensor_log.xlsx',
    'E:\\해운대\\합본_enenF_2024_02_sensor_log.xlsx',
    'E:\\해운대\\합본_enenF_2024_03_sensor_log.xlsx',
    'E:\\해운대\\합본_enenF_2024_04_sensor_log.xlsx',
    'E:\\해운대\\합본_enenF_2024_05_sensor_log.xlsx',
    'E:\\해운대\\합본_enenF_2024_06_sensor_log.xlsx'
]

# 출력 파일 경로
output_file = "E:\\해운대\\합본_enenF_2024_6_tsl_sensor_log_202412041134.xlsx"

# 각 시트별 데이터를 저장할 딕셔너리
merged_sheets = {}

# 각 파일의 시트를 읽어 병합
for file_path in file_paths:
    # 파일의 모든 시트 읽기
    data = pd.read_excel(file_path, sheet_name=None, engine='openpyxl')

    for sheet_name, sheet_data in data.items():
        if sheet_name not in merged_sheets:
            # 해당 시트가 처음 추가되는 경우
            merged_sheets[sheet_name] = sheet_data
        else:
            # 이미 해당 시트가 있다면 병합
            merged_sheets[sheet_name] = pd.concat([merged_sheets[sheet_name], sheet_data], ignore_index=True)

# 병합된 데이터를 새 엑셀 파일로 저장
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for sheet_name, sheet_data in merged_sheets.items():
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"병합 완료. 결과는 '{output_file}'에 저장되었습니다.")
