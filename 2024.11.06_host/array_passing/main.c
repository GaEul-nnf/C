#include<stdint.h>
#include<stdio.h>

void array_display(uint8_t const *const pArray, uint32_t nItmes);

int main(void)
{
	uint8_t someData[10] = {0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};

	for(uint32_t i=0 ; i<10 ; i++ )
	{
		someData[i] = i;
	}

	uint32_t nItmes = sizeof(someData)/sizeof(uint8_t);

	array_display(&someData[2],nItmes-2);

	return 0;
}

void array_display(uint8_t const *const pArray, uint32_t nItmes)
{
	for(uint32_t i=0 ; i<nItmes ; i++ )
	{
		printf("%x\t", pArray[i]);
	}
}
