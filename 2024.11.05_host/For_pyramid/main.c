#include <stdio.h>
#include <stdint.h>

void wait_for_user_input(void);

int main(void)
{
	int32_t height;

	printf("Enter height of pyramid:");
	scanf("%d",&height);

	for(int32_t i=1 ; i<=height ; i++)
	{
		for(int32_t j=i ; j>0 ; j--)
		{
			printf("%3d", j);
		}
		printf("\n");
	}

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
