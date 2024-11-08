# 2024.11.05_target

## 004led_on

STM32F401RE 보드의 LED켜기

Green LED의 부품번호 LD2 PA5에 연결되어 있음

(PA5는 A포트의 5번핀을 의미)

GPIOA를 이용해 제어

RCC 주변 클럭 제어

IO 포트 A클럭이 활성화


GPIOA 레지스터

- 모드설정을 위한 port moide register

- 데이터 작성을 위한 port output data register


port output data register

- port A의 5번핀을 제어하기 위해 5번째 위치를 1로 변경


port moide register

- 핀모드를 OUTPUT으로 구성 


## 005led_toggel

RCC 주변 클럭 제어

IO 포트 A클럭이 활성화


GPIOA 레지스터

- 모드설정을 위한 port moide register

- 데이터 작성을 위한 port output data register


port mode register

- port A의 5번핀을 제어하기 위해 5번째 위치를 1로 변경


while문을 사용하여 LED를 깜빡이도록 설정

- port output data register 의 값을 조절


## 006pin_read


PA0의 상태를 읽어 LED제어


GPIOA를 이용해 제어


RCC 주변 클럭 제어

IO 포트 A클럭이 활성화


GPIOA 레지스터

- 모드설정을 위한 port moide register

- 데이터 작성을 위한 port output data register


port mode register

- port A의 5번핀을 제어하기 위해 10번째 위치를 1로 변경


port output data register

- 핀모드를 OUTPUT으로 구성 


PA0의 상태가 HIGH일때 LED점등


port mode register

- 0번핀 입력모드로 구성 하기 위해 0,1위치의 비트를 00으로 만들어줌
 

port input data register
- 0위치의 비트를 제외한 다른 모든 비트를 0으로 만듬


