# 센서별로 셀 나눠서 저장
import pandas as pd

df = pd.read_csv('E://해운대//enenF_2024_12_tsl_sensor_log_202412041138.csv')

output_file = 'E://해운대//enenF_2024_12_tsl_sensor_log_202412041138_sensor.xlsx'

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for s_id, group in df.groupby('s_id'):

        sheet_name = str(s_id)
        sheet_name = sheet_name.replace('/', ' ')

        group.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"각 f_id 별로 시트가 생성된 엑셀 파일을 '{output_file}'로 저장했습니다.")
