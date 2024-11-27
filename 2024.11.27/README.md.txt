README.md

# 2024.11.27

## 20_RealtimeClock

RTC와 UART를 사용하여 현재 시간과 날짜를 출력하는 프로그램

RTC를 설정하고, 필요 시 백업 레지스터를 사용하여 다시 설정하지 않도록 설정 정보를 저장

RTC에서 현재 시간과 날짜를 읽어오고, 이를 UART를 통해 PC 터미널에 출력

USART2를 사용하여 PC와 시리얼 통신을 설정

시간과 날짜를 printf를 통해 출력할 수 있도록 UART가 __io_putchar에 연결

MCU가 부팅되면 HAL 및 UART, RTC 초기화

RTC 백업 레지스터에 저장된 값(BK_FLAG)을 확인하여, RTC가 초기화되지 않았으면 기본값으로 설정

무한 루프에서 RTC 시간을 읽어와 UART로 PC에 출력