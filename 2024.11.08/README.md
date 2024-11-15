#2024.11.08


## host


#### student

학생의 정보를 담고 있는 전역배열 선언

메뉴에서 활동을 입력 받음

(활동 : 1. 전체출력, 2. 학생정보추가, 3. 학생정보삭제, 4. 프로그램종료)

각 활동별 내용

(메뉴실행 - 하나의 메뉴를 입력 받으면 해당하는 활동을 실행)

전체출력 - 학생의 정보 (rollNumber, name, branch, dob, semister)출력 
(만약 정보가 없을시 찾을수 없음을 표시)

학생정보추가 - roll_number를 비교하고 새로운 학생의 정보를 입력 받아 추가함

(roll_number 비교 - 입력받은 roll_number가 이미 존재하는 roll_number라면 1을 출력)

학생정보삭제 - roll_number를 입력받아 해당 학생의 정보를 삭제

프로그램종료 - 메뉴에서 0을 입력 받으면 프로그램 종료


#### macro

전처리 연습

매크로를 이용하여 원과 삼각형의 넓이 계산

조건부 컴파일을 이용하여 코드블럭 배제


## target


#### 013_led_toggle_with_macros

main.h를 이용하여 주소 매크로 정의

주변장치의 클럭 활성화, IO핀 출력모드 설정, IO핀 5를 HIGH or LOW로 만드는 기능을 매크로 정의