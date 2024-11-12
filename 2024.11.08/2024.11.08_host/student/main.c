/*
 * main.c
 *
 *  Created on: Nov 8, 2024
 *      Author: OWNER
 */

#include <stdio.h>
#include <stdint.h>
#include <string.h>

typedef struct
{
    int rollNumber;
    char name[100];
    char branch[50];
    char dob[15];
    int semister;

}STUDENT_INFO_t;

int max_record=10;

STUDENT_INFO_t students[10];

void display_menu(void); // 메뉴 출력
int read_menu_code(void); // 메뉴코드 입력
void decode_menu_code(int8_t menu_code); // 하나의 메뉴 종료후 멘트 출력
void display_all_records(STUDENT_INFO_t *record, int8_t max_record); //전체 레코드 출력
int check_roll_number(int roll_number, STUDENT_INFO_t *record, int8_t max_record); //롤 넘버를 입력 받아 체크
int add_new_record(STUDENT_INFO_t *record, int8_t max_record); // 새로운 레코드를 입력 받아 추가
int delete_record(STUDENT_INFO_t *record, int8_t max_record); // 만들어져 있는 레코드 삭제

int main()
{
    int8_t menu_code;
    int8_t app_continue = 1;

    printf("Student record management program\n");

     while(app_continue)
     {
		display_menu();
		menu_code = read_menu_code();

		if(menu_code){
			decode_menu_code(menu_code);
		}else{
			app_continue = 0;
			printf("Exiting application\n");
		}
     }
    return 0;
}

// 프로그램 시작 후 보이는 선택 메뉴
void display_menu(void)
{
    printf("\nDisplay all records  -->1\n");
    printf("Add new record       -->2\n");
    printf("Delete a record      -->3\n");
    printf("Exit application     -->0\n");
    printf("Enter your option here:");
}

// 메뉴 중 입력 받은 값
int read_menu_code(void)
{
	int input;
	scanf("%d",&input);

	return(input);
}

// 입력받은 하나의 메뉴를 실행
void decode_menu_code(int8_t menu_code)
{
    int8_t ret;

    switch(menu_code)
    {
        case 1:
        	printf("\nDisplaying all students record\n");
        	display_all_records(students,max_record);
        	break;
        case 2:
			printf("\nAdd a new record\n");
			ret = add_new_record(students,max_record);
			ret ? printf("\nRecord add successful\n") : printf("\nRecord added unsuccessfully\n");
			break;
        case 3:
			printf("\nDelete a record\n");
			ret = delete_record(students,max_record);
			ret ? printf("\nRecord deleted successfully\n") : printf("\nRecord not found\n");
			break;
        default:
			printf("\nInvalid input\n");
    }
}

//모든 record 화면에 출력
void display_all_records(STUDENT_INFO_t *record, int8_t max_record)
{
	int record_found = 0;

	for(uint32_t i=0 ; i<max_record ; i++)
	{
	    if( record[i].rollNumber)
	    {
	    	record_found = 1;
	        printf("\n***********\n");
	        printf("rollNumber	: %u\n",record[i].rollNumber);
	        printf("studentSemister	: %u\n",record[i].semister);
	        printf("studentDOB	: %s\n",record[i].dob);
	        printf("studentBranch	: %s\n",record[i].branch);
	        printf("studentName	: %s\n",record[i].name);
	        printf("***********\n");
	    }
	}
	if(! record_found)
	   printf("\nNo records found\n");
}

// 새로운 record 만들때 기존에 있는 roll_number와 겹치지 않도록 비교
int check_roll_number(int roll_number, STUDENT_INFO_t *record, int8_t max_record)
{
	int is_exist = 0;

	for(int i = 0 ; i < max_record ; i++)
	{
	    if ( record[i].rollNumber == roll_number)
	    {
	    	is_exist = 1;
	    	break;
		}
	}
	return is_exist;
}

// 새로운 record 추가
int add_new_record(STUDENT_INFO_t *record, int8_t max_record)
{
    int add_status=0;
    int is_exist=0;
    int roll_number;
    int i;

    for( i = 0 ; i < max_record ; i++)
    {
        if( ! record[i].rollNumber)
        {
                printf("Enter the rollNumber : ");
                scanf("%d",&roll_number);
                is_exist = check_roll_number(roll_number,students,max_record);
                if(! is_exist)
                {
                	add_status = 1; //adding new record
                    record[i].rollNumber = roll_number;
                    printf("Enter the studentSemister   : ");
                    scanf("%d",&record[i].semister);
                    getchar();
                    printf("Enter the studentDOB        : ");
                    scanf("%s",&record[i].dob);
                    getchar();
                    printf("Enter the studentBranch     : ");
                    scanf("%50[^\n]s",record[i].branch);
                    getchar();
                    printf("Enter the studentName       : ");
                    scanf("%50[^\n]s",record[i].name);

                }else
                {
                    printf("\n roll number already exist\n");
                }
                break;
        }
    }
    if(i == max_record)
        printf("\nNo space available\n");
    return add_status;
}

// record 삭제
int delete_record(STUDENT_INFO_t *record, int8_t max_record)
{
	int8_t delete_flag = 0;

	int roll_number;

	printf("\nEnter the roll number of the student:");
	scanf("%d",&roll_number);

	for(int i = 0 ; i < max_record ; i++)
	{
		if( roll_number == record[i].rollNumber)
		{
			delete_flag = 1;
			memset(&record[i],0,sizeof(STUDENT_INFO_t));
			break;
		}
	}
	return delete_flag;
}
