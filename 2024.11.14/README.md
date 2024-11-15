# 2024.11.14

## 3_UartTx_Printf

UART설정하고, printf를 통해 문자열 전송

uart_init() 함수에서 UART2를 115200 bps로 설정하고, 전송 모드(TX)로 설정

__io_putchar를 통해 printf와 UART를 연결


## 내용정리 


#### SYSTEM TICK TIMER(SYSTICK)

sysTick : Cortex-M 코어에만 지원하는 24bit 타이머


#### sysTick - counting 

초깃값부터 0까지 계산

초깃값은 0x000000~0xFFFFFF사이의 값으로 설정 가능


#### sysTick - Registers

systick current value register - 현재 카운터 값을 읽거나 쓸 때 사용

systick control & status register - 타이머 활성화, 인터럽트 활성화, 클럭 소스 선택, 카운트 플래그 등을 제어

systick reload value register - 타이머가 0에 도달했을 때 자동으로 로드되는 값


#### TIMER - TIMER vs. COUNTER

TIMER - MCU 내부 clock을 세는 장치

COUNTER - MCU 외부 clock을 세는 장치


#### TIMER - STM32 Timers

Timer count register - 현재 카운트 값 출력

Timer auto-reload register - 카운터에서 언제 overflow가 발생할지 결정하는 역할

Timer prescaler register - 타이머의 입력 clock를 분할하여 타이머의 계산 속도 늧춤

