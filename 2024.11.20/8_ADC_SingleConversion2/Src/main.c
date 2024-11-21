#include <stdio.h>
#include "stm32f4xx_hal.h"
#include "uart.h"
#include "adc.h"

ADC_HandleTypeDef hadc1;

uint32_t  sensor_value;

int main()
{

  HAL_Init();
  uart_init();
  adc_pa0_single_conv_init();

  while(1)
  {
	   HAL_ADC_Start(&hadc1);

	   HAL_ADC_PollForConversion(&hadc1,1);

	  sensor_value =  pa0_adc_read();

	  printf("The sensor value : %d   \n\r",(int)sensor_value);

	  //HAL_Delay(10);
  }
}

void  SysTick_Handler(void)
{
	HAL_IncTick();
}



