# 2024.11.20

## 8_ADC_SingleConversion

ADC를 사용하여 single conversion을 수행

초기화
ADC, GPIO(입력 핀), UART 초기화.
ADC는 12비트 해상도로 설정, 단일 변환 모드 사용.

ADC 변환
HAL 함수를 사용해 ADC 변환 시작 (HAL_ADC_Start).
변환 완료 대기 (HAL_ADC_PollForConversion).
변환 결과(디지털 값) 읽기 (HAL_ADC_GetValue).
변환 종료 (HAL_ADC_Stop).

데이터 출력
변환된 값을 UART로 전송하여 디버깅이나 출력.

주기적 반복
1초 간격으로 변환 수행 및 결과 출력.

