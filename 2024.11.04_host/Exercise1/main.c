#include <stdio.h>

int main(void)
{
	char data = 100;
	printf("Value of data is : %d\n", data);
	printf("Address of the variable data is : %p\n", &data);

	char* pAddress = &data; // 변수의 주소 포인터에 저장

	char value = *pAddress; // 포인터 변수 역참조
	printf("read value is : %d\n", value);

	*pAddress = 65; // 데이터 작성을 위해 포인터 변주 역참조
	printf("Value of data is : %d\n", data);


}
