# 날자 데이터를 분단위로 비교하여 일치하면 기온과 습도 데이터를 추가하도록 하고자 함
import pandas as pd

# 파일 경로 지정
temperature_file = 'E:\\final_좌제3동_기온_202301_202411.csv'  # 기온 데이터 파일 경로
humidity_file = 'E:\\final_좌제3동_습도_202301_202411.csv'  # 습도 데이터 파일 경로
base_file = 'E:\\해운대\\enenF_2023_6_tsl_sensor_log_202412041134_sensor.xlsx'  # 기본 엑셀 파일 경로
output_file = 'E:\\해운대\\합본_enenF_2023_6_tsl_sensor_log_202412041134_sensor.xlsx'  # 출력 파일 경로

# 기온 데이터 로드 (CSV 파일 읽기)
temperature = pd.read_csv(temperature_file, usecols=['daydata', 'value'], encoding='utf-8')

# 습도 데이터 로드 (CSV 파일 읽기)
humidity = pd.read_csv(humidity_file, usecols=['daydata', 'value'], encoding='utf-8')

# 'daydata' 컬럼을 datetime 형식으로 변환하고 분을 내림 (시 단위로)
temperature['daydata'] = pd.to_datetime(temperature['daydata'], format='%Y%m%d%H%M', errors='coerce').dt.floor('h')
humidity['daydata'] = pd.to_datetime(humidity['daydata'], format='%Y%m%d%H%M', errors='coerce').dt.floor('h')

# NaT (Not a Time) 값 처리
temperature['daydata'] = temperature['daydata'].fillna(pd.to_datetime('2023-01-01 00:00'))
humidity['daydata'] = humidity['daydata'].fillna(pd.to_datetime('2023-01-01 00:00'))

# Base 파일의 모든 시트 읽기
base_data = pd.read_excel(base_file, sheet_name=None, engine='openpyxl')

# 출력 데이터를 저장할 딕셔너리 (각 시트별로 처리된 데이터를 저장)
output_sheets = {}

# 각 시트에 대해 데이터 처리
for sheet_name, sheet_data in base_data.items():
    # 'sl_date_collect' 컬럼을 datetime 형식으로 변환하고 분을 내림
    sheet_data['sl_date_collect'] = pd.to_datetime(sheet_data['sl_date_collect'], errors='coerce').dt.floor('h')

    # 'sl_date_collect'과 기온 데이터 병합
    sheet_data = sheet_data.merge(
        temperature[['daydata', 'value']],  # 기온 데이터에서 'daydata'와 'value' 컬럼 선택
        left_on='sl_date_collect',  # 현재 시트의 'sl_date_collect' 컬럼을 기준으로
        right_on='daydata',  # 기온 데이터의 'daydata' 컬럼과 병합
        how='left'  # left join을 사용하여 현재 시트에 기온 데이터를 추가
    ).rename(columns={'value': '기상청_기온'}).drop(columns=['daydata'])

    # 습도 데이터를 'sl_date_collect'을 기준으로 병합
    sheet_data = sheet_data.merge(
        humidity[['daydata', 'value']],  # 습도 데이터에서 'daydata'와 'value' 컬럼 선택
        left_on='sl_date_collect',  # 현재 시트의 'sl_date_collect' 컬럼을 기준으로
        right_on='daydata',  # 습도 데이터의 'daydata' 컬럼과 병합
        how='left'  # left join을 사용하여 현재 시트에 습도 데이터를 추가
    ).rename(columns={'value': '기상청_습도'}).drop(columns=['daydata'])

    # 'sl_date_collect'은 datetime 형식으로 그대로 유지

    # 처리된 시트를 output_sheets 딕셔너리에 저장
    output_sheets[sheet_name] = sheet_data

# 병합된 데이터를 새 엑셀 파일로 저장
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for sheet_name, sheet_data in output_sheets.items():
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)
        # 처리된 시트 데이터를 새 엑셀 파일에 저장
        # index=False로 인덱스 컬럼은 제외하고 저장

print(f"병합 완료. 결과는 '{output_file}'에 저장되었습니다.")
# 작업이 완료되면 출력 파일 경로를 출력하여 확인
