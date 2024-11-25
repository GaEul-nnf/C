# 2024.11.25

## 15_SPI_Polling

SPI 통신에서 데이터를 송수신하는 가장 간단한 방식

CPU가 명령을 실행하며 데이터 전송이 완료될 때까지 대기

HAL 함수 HAL_SPI_Transmit(), HAL_SPI_Receive(), 또는 HAL_SPI_TransmitReceive()를 사용하여 데이터 전송 및 수신을 처리

완료될 때까지 CPU가 대기, 프로그램 실행이 중단되는 블로킹 방식


## 16_SPI_Interrupt

SPI 통신이 완료되면 인터럽트가 발생해 CPU 알림

인터럽트 서비스 루틴(ISR)을 통해 데이터를 처리, 비블로킹 방식으로 동작

HAL_SPI_Transmit_IT(), HAL_SPI_Receive_IT(), 또는 HAL_SPI_TransmitReceive_IT() 사용

데이터 전송 중 CPU가 다른 작업을 수행가능


## 17_SPI_DMA

DMA를 사용해 CPU를 거치지 않고 메모리와 SPI 주변 장치 간에 데이터를 직접 전송

CPU는 데이터를 전송하거나 대기하지 않고 다른 작업 수행 가능

DMA 전송이 완료되면 HAL_SPI_TxCpltCallback() 또는 HAL_SPI_RxCpltCallback()에서 처리

CPU 부하를 최소화하며, 대량 데이터 전송에 적합


## 내용정리 

#### SPI Protocol

SPI : 마이크로컨트롤러와 주변 장치 간에 데이터를 교환하는 고속 동기 직렬 통신 프로토콜

#### SPI 구성 요소

Master : 데이터 전송을 제어하는 장치

Slave : 명령을 받는 장치

연결 핀:

MOSI (Master Out Slave In): 마스터에서 슬레이브로 데이터 전송

MISO (Master In Slave Out): 슬레이브에서 마스터로 데이터 전송

SCLK (Serial Clock): 마스터가 생성하는 동기화 신호

SS (Slave Select): 특정 슬레이브를 선택하는 신호

#### 동작 원리

SPI는 클록 신호를 사용하여 데이터를 동기화, 데이터 동시에 송수신

마스터가 클록을 생성하고 데이터를 전송, 슬레이브는 이를 받아 처리

#### 전송 모드

SPI는 데이터 샘플링 시점과 클록 극성을 조절하는 CPOL및 CPHA로 구성된 4가지 모드를 지원

각 모드는 데이터 전송 방식에 영향을 미침

#### 장점

고속 데이터 전송

다수의 슬레이브 장치 연결 가능

풀 듀플렉스 지원

#### 단점

많은 핀 사용 (슬레이브 장치가 많을수록 SS 핀이 필요)

장거리 통신에 적합하지 않음
