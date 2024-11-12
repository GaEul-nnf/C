#include <stdio.h>
#include <stdint.h>

void wait_for_user_input(void);

int main(void)
{
	int64_t income = 0;
	int64_t tax = 0;

	double temp_income;

	printf("Enter your total income : ");
	scanf("%lf",&temp_income);

	if(temp_income<0){
		printf("Income cannot be -ve\n");
		wait_for_user_input();
		return 0;
	}

	income = (int64_t)temp_income;

	if(income <= 9525){
		tax = 0;
	}
	else if((9526<income)&&(38700>=income)){
		tax = income * 0.12;
	}
	else if((38701<income)&&(82500>=income)){
		tax = income * 0.22;
	}
	else if((income>82500)){
		tax = income * 0.32;
		tax = tax + 1000;
	}
	else{
		;
	}

	printf("Tax payable : $%I64u\n",tax);

	wait_for_user_input();
}

void wait_for_user_input(void)
{
	printf("Press enter key to exit application\n");
	while(getchar() != '\n')
		{

		}
	getchar();
}
