import pandas as pd

# 파일 경로 지정
temperature_file = 'E:\\final_좌제3동_기온_202301_202411_xlsx.xlsx'  # 기온 데이터 파일 경로
humidity_file = 'E:\\final_좌제3동_습도_202301_202411_xlsx.xlsx'  # 습도 데이터 파일 경로
base_file = 'E:\\해운대\\enenF_2024_12_sensor_log.xlsx'  # 기본 엑셀 파일 경로
output_file = 'E:\\해운대\\합본_enenF_2024_12_sensor_log.xlsx'  # 출력 파일 경로

# 데이터 로드 (엑셀 파일 읽기)
temperature = pd.read_excel(temperature_file, usecols=['daydata', 'value'], engine='openpyxl')
humidity = pd.read_excel(humidity_file, usecols=['daydata', 'value'], engine='openpyxl')

# 날짜 형식 변환
temperature['daydata'] = pd.to_datetime(temperature['daydata'], format='%Y%m%d%H%M', errors='coerce')
humidity['daydata'] = pd.to_datetime(humidity['daydata'], format='%Y%m%d%H%M', errors='coerce')

# NaT 값 처리 (예: 기본 날짜 설정)
temperature['daydata'] = temperature['daydata'].fillna(pd.to_datetime('2023-01-01 00:00'))
humidity['daydata'] = humidity['daydata'].fillna(pd.to_datetime('2023-01-01 00:00'))

# Base 파일의 모든 시트 읽기
base_data = pd.read_excel(base_file, sheet_name=None, engine='openpyxl')

output_sheets = {}

# 각 시트에 대해 데이터 처리
for sheet_name, sheet_data in base_data.items():
    sheet_data_copy = sheet_data.copy()

    # 원본 sl_date_collect 저장
    sheet_data_copy['sl_date_collect_original'] = pd.to_datetime(sheet_data_copy['sl_date_collect'], errors='coerce')

    # 비교용 sl_date_collect를 시 단위로 변환
    sheet_data_copy['sl_date_collect'] = sheet_data_copy['sl_date_collect_original'].dt.floor('h')

    # 기온, 습도 데이터와 시트의 시간 범위 비교
    valid_range_start = sheet_data_copy['sl_date_collect'].min()
    valid_range_end = sheet_data_copy['sl_date_collect'].max()

    temperature_filtered = temperature[
        (temperature['daydata'] >= valid_range_start) &
        (temperature['daydata'] <= valid_range_end)
    ]
    humidity_filtered = humidity[
        (humidity['daydata'] >= valid_range_start) &
        (humidity['daydata'] <= valid_range_end)
    ]

    # 기온 데이터 병합
    sheet_data_copy = sheet_data_copy.merge(
        temperature_filtered[['daydata', 'value']],
        left_on='sl_date_collect',  # 비교는 시 단위로
        right_on='daydata',
        how='left'
    ).rename(columns={'value': '기상청_기온'}).drop(columns=['daydata'])

    # 습도 데이터 병합
    sheet_data_copy = sheet_data_copy.merge(
        humidity_filtered[['daydata', 'value']],
        left_on='sl_date_collect',  # 비교는 시 단위로
        right_on='daydata',
        how='left'
    ).rename(columns={'value': '기상청_습도'}).drop(columns=['daydata'])

    # 원본 sl_date_collect를 다시 저장
    sheet_data_copy['sl_date_collect'] = sheet_data_copy['sl_date_collect_original']
    sheet_data_copy = sheet_data_copy.drop(columns=['sl_date_collect_original'])

    # 병합된 데이터를 output_sheets에 저장
    output_sheets[sheet_name] = sheet_data_copy

# 병합된 데이터를 새 엑셀 파일로 저장
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for sheet_name, sheet_data in output_sheets.items():
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"병합 완료. 결과는 '{output_file}'에 저장되었습니다.")
