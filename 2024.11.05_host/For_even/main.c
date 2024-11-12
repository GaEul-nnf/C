#include <stdio.h>
#include <stdint.h>

void wait_for_user_input(void);

int main(void)
{
	int32_t num1, num2;
	int32_t even = 0;

	printf("Enter start and end numbers(give space between 2 nos):");
	scanf("%d %d", &num1, &num2);

	if(num2 < num1){
		printf("ending number should be > starting number\n");
		wait_for_user_input();
		return 0;
	}

	for(printf("Even number are :\n");num1 <= num2;num1++){
		if(!(num1%2)){
			printf("%4d\t", num1);
			even++;
		}
	}

	printf("\nTotal number of even nos = %u\n", even);

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
