#include <stdio.h>
#include <stdint.h>

struct carModel
{
	uint32_t carNumber;
	uint32_t carPrice;
	uint16_t carMaxSpeed;
	float carWeight;
};

int main(void)
{
	struct carModel CarBMW = {2021, 15000, 220, 1330};
	printf("Sizeof struct carModel is %u\n",sizeof(struct carModel));

	getchar();

	return 0;
}
