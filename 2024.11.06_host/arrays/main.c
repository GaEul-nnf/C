#include<stdint.h>
#include<stdio.h>

int main(void)
{
	uint8_t someData[10] = {0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff};

	printf("contents of this array\n");

	for(uint32_t i=0 ; i<10 ; i++ )
	{
		printf("%x\t",someData[i]);

		printf("%dth element value = %x\t",i,someData[i]);

		printf("%dth element value = %x\n",i,*(someData+i));
	}

	someData[2] = 0x33;

	printf("\n");

	for(uint32_t i=0 ; i<10 ; i++ )
		{
			printf("%x\t",someData[i]);

			printf("%dth element value = %x\t",i,someData[i]);

			printf("%dth element value = %x\n",i,*(someData+i));
		}

	return 0;
}
