#include <stdio.h>
#include <stdint.h>

void wait_for_user_input(void);

int main(void)
{
	int32_t num1, output;
	printf("Enter a number:");
	scanf("%d",&num1);

	output = num1 &  0x8F;
	printf("[input] [output] :0x%x 0x%x\n",num1, output);

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
