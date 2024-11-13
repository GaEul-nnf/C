# 2024.11.12

## 1_GpioInputOutput

Button을 누르게 되면 점등되어있던 LED가 꺼짐


## 2_UartTx_polling

UART 드라이버 활성화

USART2를 이용해 UART통신

HAL_UART_Transmit을 이용해 데이터 전송


## 내용정리

#### UART Protocol 이해

 8비트가 있다고 가정

- 직렬 통신 (시리얼 통신): 8비트의 데이터 한 번에 한 비트씩 전송

- 병렬 통신 (버스): 8비트의 데이터 동시 전송


시리얼 데이터 통신

- 동기 : clock을 데이터와 함께 전송

- 비동기 : clock이 전송되지 않음


- UART : 범용 비동기화 송수신

- USART : 범용 동기/비동기화 송수신


전송 모드

- Duplex : 데이터 송수신 가능

- Simplex (단방향): 데이터를 전송만 가능하거나 수신만 가능함 (한방향으로만 전송)

- HALF Duplex (쌍방향): 데이터를 한번에 한가지 방식으로만 전송

- Full Duplex (양방향): 데이터를 한번에 두가지 방식으로 전송


Protocol

- 각 바이트 또는 문자는 시작 비트와 정지비트 사이에 들어있음

(시작비트 : 항상 1bit, value 항상 0bit, 정지비트 :1 or 2bit, value 항상 1bit )


configuration parameters

- Baudrate : 데이터 전송 속도 (초당 전송 비트수)

- Stop Bit : 전송된 Stop Bit수 1 or 2

- Parity : 홀수와 짝수를 이용하여 오류 검출

- Mode : RX 또는 TX모드를 활성화할지 비활성화 할지 지정

- Word Length : 전송하거나 수신하는 데이터 비트 수 지정 (8bit or 9bit)

- Hardware Flow Control : 하드웨어 흐름 제어를 활성화할지 비활성화할지 지정



