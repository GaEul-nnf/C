#include <stdio.h>
#include <stdint.h>

int main(void)
{
	int32_t age = 0;

	printf("나이를 입력해주세요(Please enter your age) : ");
	scanf("%d",&age);

	if(age>=18)
		printf("투표 가능한 나이입니다(You're old enough to vote)");
	else
		printf("투표 불가능한 나이입니다(You're an age where you can't vote)");

	printf("Press enter key to exit application\n");
	while(getchar() != '\n')
		{

		}
	getchar();
}
