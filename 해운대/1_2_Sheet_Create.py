import pandas as pd

# CSV 파일 경로
input_file = 'E://해운대//enenF_2023_6_tsl_sensor_log_202412041134.csv'
# 데이터 로드
df = pd.read_csv(input_file)

# sl_date_collect 열을 datetime 형식으로 변환
df['sl_date_collect'] = pd.to_datetime(df['sl_date_collect'])

# 각 달별로 데이터를 분리하여 저장
for (year, month), group in df.groupby([df['sl_date_collect'].dt.year, df['sl_date_collect'].dt.month]):
    # 저장 파일 경로
    output_file = f'E://해운대//enenF_{year}_{month:02d}_sensor_log.xlsx'

    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # s_id 기준으로 분리하여 각 시트에 저장
        for s_id, sensor_group in group.groupby('s_id'):
            sheet_name = str(s_id).replace('/', ' ')
            sensor_group.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"{year}년 {month}월 데이터가 저장된 파일을 '{output_file}'로 생성했습니다.")
