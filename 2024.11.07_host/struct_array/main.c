/*
 * main.c
 *
 *  Created on: Nov 7, 2024
 *      Author: OWNER
 */

#include <stdint.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
	int rollNumber;
	char name[100];
	char branch[50];
	char dob[15];
	int semister;
}STUDENT_INFO_t;

int const max_record = 2;

STUDENT_INFO_t students[2] =
{
		{9876, "ashok kumar","mechanical","12/11/1999",7},
		{8888, "ram kumar","computer","12/11/1999",7}
};

void display_all_records(STUDENT_INFO_t *pBaseAddrofRecords, int max_record)
{
	for(uint32_t i=0 ; i<max_record ; i++)
	{
		printf("Roll number of %dth element of the array = %d\n",i,pBaseAddrofRecords[i].rollNumber);

		// pBaseAddrofRecords[i] ==> *(pBaseAddrofRecords+i)
	}
}

int main(void)
{
	display_all_records(students,max_record);
	return 0;
}
