import pandas as pd

# 파일 경로
temperature_file = 'E:\\final_백석1동_기온_20230111_20241130.csv'
humidity_file = 'E:\\final_백석1동_습도_20230111_20241130.csv'
base_file = 'E:\\업무지시\\일산_2023_2024_.xlsx'
output_file = 'E:\\업무지시\\일산_2023_2024_합본_최종.xlsx'

# 데이터 로드 (CSV 파일 읽기)
temperature = pd.read_csv(temperature_file, usecols=['daydata', 'value'], encoding='utf-8')
humidity = pd.read_csv(humidity_file, usecols=['daydata', 'value'], encoding='utf-8')

# 날짜 형식 변환
temperature['daydata'] = pd.to_datetime(temperature['daydata'], format='%Y%m%d%H%M', errors='coerce')
humidity['daydata'] = pd.to_datetime(humidity['daydata'], format='%Y%m%d%H%M', errors='coerce')

# NaT 값 처리 (예: 기본 날짜 설정)
temperature['daydata'] = temperature['daydata'].fillna(pd.to_datetime('2023-01-01 00:00'))
humidity['daydata'] = humidity['daydata'].fillna(pd.to_datetime('2023-01-01 00:00'))

# Base 파일의 모든 시트 읽기
base_data = pd.read_excel(base_file, sheet_name=None, engine='openpyxl')

# 출력 데이터를 저장할 딕셔너리
output_sheets = {}

# 병합 제외 시트 이름
exclude_sheet_name = "일산_2023_2024"

# 각 시트 처리
for sheet_name, sheet_data in base_data.items():
    if sheet_name == exclude_sheet_name:
        # 제외 시트는 그대로 추가
        output_sheets[sheet_name] = sheet_data
    else:
        # ss_day_time을 datetime 형식으로 변환
        sheet_data['ss_day_time'] = pd.to_datetime(sheet_data['ss_day_time'], format='%Y%m%d%H%M', errors='coerce')

        # 기온 데이터를 병합
        sheet_data = sheet_data.merge(
            temperature[['daydata', 'value']],
            left_on='ss_day_time',
            right_on='daydata',
            how='left'
        ).rename(columns={'value': '기상청_기온'}).drop(columns=['daydata'])

        # 습도 데이터를 병합
        sheet_data = sheet_data.merge(
            humidity[['daydata', 'value']],
            left_on='ss_day_time',
            right_on='daydata',
            how='left'
        ).rename(columns={'value': '기상청_습도'}).drop(columns=['daydata'])

        # ss_day_time을 숫자 형식으로 변환
        sheet_data['ss_day_time'] = sheet_data['ss_day_time'].dt.strftime('%Y%m%d%H%M').astype(int)

        # 처리된 시트를 저장
        output_sheets[sheet_name] = sheet_data

# 병합된 데이터 저장
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for sheet_name, sheet_data in output_sheets.items():
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"병합 완료. 결과는 '{output_file}'에 저장되었습니다.")
