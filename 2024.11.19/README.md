# 2024.11.19

## 5_GPIO_Interrupt_EXTI

인터럽트 발생 시 LED 점등, 소등

GPIO 핀에서 외부 신호를 감지하고 인터럽트를 처리

특정 GPIO 핀에 인터럽트 기능을 활성화하고, 외부 신호가 감지되었을 때 사용자 정의 콜백 함수가 호출

HAL 라이브러리를 사용해 EXTI 설정


## 6_Multiple GPIO_Interrupts_EXTI

각각의 EXTI 핀에 별도 동작 설정

외부 인터럽트를 사용하여 다중 GPIO 핀에서 발생하는 이벤트를 처리

GPIO 핀을 입력 모드로 설정하고, EXTI(External Interrupt Line)와 연결

NVIC에서 각 EXTI 라인의 우선순위를 설정 및 활성화

어떤 GPIO 핀이 트리거되었는지 확인 후 특정 작업 수행


## 내용정리 

인터럽트 

MCU가 현재 실행 중인 작업을 중단하고, 특정 이벤트(외부 신호, 타이머 만료, 데이터 수신 등)에 대해 즉시 반응하도록 하는 메커니즘

특징 

- 이벤트 발생 시, CPU가 인터럽트 서비스 루틴(ISR)을 실행

- 시스템 응답성을 높이고, 폴링(polling) 방식의 비효율성을 제거

인터럽트 설정 흐름

- 인터럽트 소스 활성화:

주변 장치 또는 GPIO에서 인터럽트를 활성화

EXTI, UART, I2C, Timer 등에서 설정 가능

- NVIC 설정:

HAL_NVIC_SetPriority()로 우선순위를 설정

HAL_NVIC_EnableIRQ()로 특정 인터럽트를 활성화

- 콜백 함수 구현:

HAL 라이브러리에서 제공하는 콜백 함수(HAL_xxx_IRQHandler)를 사용하여 인터럽트 이벤트를 처리
