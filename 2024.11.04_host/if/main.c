#include <stdio.h>
#include <stdint.h>

int main(void)
{
	uint8_t myData = 60;

	if (myData > 40)
	{
		;
	}
	{
		printf("Value = %d\n",myData);
		myData=0;
	}

	myData++;

	return 0;
}
