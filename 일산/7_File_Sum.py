# 원본 파일과 기온, 습도 파일을 합침
import pandas as pd

temperature_file = 'E:\\최종_백석1동_기온_20230111_20241031_xlsx.xlsx'
humidity_file = 'E:\\최종_백석1동_습도_20230111_20241031_xlsx.xlsx'

# Excel 파일에서 필요한 열만 가져오기
temperature = pd.read_excel(temperature_file, usecols=['daydata', 'value'])
humidity = pd.read_excel(humidity_file, usecols=['daydata', 'value'])

# 날짜 형식 변환
temperature['daydata'] = pd.to_datetime(temperature['daydata'], format='%Y%m%d%H%M', errors='coerce')
humidity['daydata'] = pd.to_datetime(humidity['daydata'], format='%Y%m%d%H%M', errors='coerce')

# NaT 값 처리
temperature['daydata'] = temperature['daydata'].fillna(pd.to_datetime('2023-01-01 00:00'))
humidity['daydata'] = humidity['daydata'].fillna(pd.to_datetime('2023-01-01 00:00'))

base_file = 'E:\\업무지시\\일산_2023_2024_.xlsx'
base_data = pd.read_excel(base_file, sheet_name=None)

output_sheets = {}

# 특정 시트를 제외하고 모든 시트 처리
exclude_sheet_name = "일산_2023_2024"
for sheet_name, sheet_data in base_data.items():
    if sheet_name == exclude_sheet_name:
        output_sheets[sheet_name] = sheet_data
    else:
        # ss_day_time을 datetime 형식으로 변환
        sheet_data['ss_day_time'] = pd.to_datetime(sheet_data['ss_day_time'], format='%Y%m%d%H%M', errors='coerce')

        # 기온과 습도를 날짜 기준으로 병합
        sheet_data = sheet_data.merge(temperature[['daydata', 'value']], left_on='ss_day_time', right_on='daydata', how='left')
        sheet_data = sheet_data.rename(columns={'value': '기상청_기온'}).drop(columns=['daydata'])

        sheet_data = sheet_data.merge(humidity[['daydata', 'value']], left_on='ss_day_time', right_on='daydata', how='left')
        sheet_data = sheet_data.rename(columns={'value': '기상청_습도'}).drop(columns=['daydata'])

        # ss_day_time을 숫자 형식으로 변환 (예: 202301011200 형태로 변환)
        sheet_data['ss_day_time'] = sheet_data['ss_day_time'].dt.strftime('%Y%m%d%H%M').astype(int)

        output_sheets[sheet_name] = sheet_data

# 병합된 데이터 저장
with pd.ExcelWriter('E:\\업무지시\\일산_2023_2024_합본_최종.xlsx') as writer:
    for sheet_name, sheet_data in output_sheets.items():
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)