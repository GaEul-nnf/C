# 2024.11.15

## 7_Timer_Timebase

UART를 사용하여 데이터를 송신하고 printf를 통해 UART를 출력 스트림으로 사용

SysTick 타이머 : 일정 주기로 인터럽트를 발생시켜 시스템 시간을 관리, 이를 통해 HAL_Delay()와 같은 딜레이 함수를 사용할 수 있게 해줌

PA2: USART2_TX (UART 송신)

클럭 설정

GPIOA 클럭 활성화: __HAL_RCC_GPIOA_CLK_ENABLE()

USART2 클럭 활성화: __HAL_RCC_USART2_CLK_ENABLE()


UART 설정

Baud Rate: 115200 bps (초당 비트 전송 속도)

Word Length: 8비트

Stop Bits: 1비트

Parity: 없음

Mode: 송신(TX)만 활성화


## 4_ADC_ContinuousConversion

ADC와 UART를 사용해 PA0에서 읽은 데이터를 변환하여 UART로 전송

ADC를 초기화 하고 ADC 데이터를 수집함

UART를 초기화 하고 printf 함수가 UART를 통해 데이터를 전송하도록 설정

무한 루프에서 pa0_adc_read 함수를 사용해 PA0 핀의 ADC 데이터 읽기


## 내용정리 

#### ADC 

아날로그 신호를 디지털 값으로 변환하는 장치

#### ADC 모드

단일 변환 모드 : 한 번의 변환으로 단일 또는 여러 채널의 데이터를 수집, 한 번의 측정만 필요한 간헐적인 데이터 수집에 적합

연속 변환 모드 : ADC가 설정된 채널을 반복적으로 변환하여 실시간 데이터 모니터링에 적합, 변환은 자동으로 반복되며 사용자가 중지할 때까지 지속

다중 채널 연속 변환 : 여러 채널을 특정 순서로 설정하여, 각 채널을 개별적으로 샘플링 가능, 다양한 센서 데이터를 동시에 수집에 유용

데이터 처리 방식 : 변환된 데이터를 읽는 방법으로는 폴링(종료 플래그 확인), 인터럽트, DMA(직접 메모리 접근)를 사용, DMA는 CPU의 개입 없이 자동으로 데이터를 메모리로 전송해 시스템 효율성을 상승

