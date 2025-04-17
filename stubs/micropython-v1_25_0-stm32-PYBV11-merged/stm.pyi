"""
Functionality specific to STM32 MCUs.

MicroPython module: https://docs.micropython.org/en/v1.25.0/library/stm.html

This module provides functionality specific to STM32 microcontrollers, including
direct access to peripheral registers.

---
Module: 'stm' on micropython-v1.25.0-stm32-PYBV11
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': '1.25.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Tuple, Final
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

SPI_I2SPR: Final[int] = 32
RTC_DR: Final[int] = 4
RTC_CR: Final[int] = 8
RTC_CALR: Final[int] = 60
RTC_ISR: Final[int] = 12
RTC_SSR: Final[int] = 40
RTC_SHIFTR: Final[int] = 44
RTC_PRER: Final[int] = 16
RTC_CALIBR: Final[int] = 24
RTC_BKP5R: Final[int] = 100
RTC_BKP4R: Final[int] = 96
RTC_BKP3R: Final[int] = 92
RTC_BKP6R: Final[int] = 104
RTC_BKP9R: Final[int] = 116
RTC_BKP8R: Final[int] = 112
RTC_BKP7R: Final[int] = 108
RTC_TAFCR: Final[int] = 64
SPI_CR1: Final[int] = 0
SPI3: Final[int] = 1073757184
SPI2: Final[int] = 1073756160
SPI_CR2: Final[int] = 4
SPI_I2SCFGR: Final[int] = 28
SPI_DR: Final[int] = 12
SPI_CRCPR: Final[int] = 16
SPI1: Final[int] = 1073819648
RTC_TSSSR: Final[int] = 56
RTC_TSDR: Final[int] = 52
RTC_TR: Final[int] = 0
RTC_TSTR: Final[int] = 48
SDIO: Final[int] = 1073818624
RTC_WUTR: Final[int] = 20
RTC_WPR: Final[int] = 36
RTC_BKP2R: Final[int] = 88
RNG: Final[int] = 1342572544
RCC_SSCGR: Final[int] = 128
RCC_PLLI2SCFGR: Final[int] = 132
RNG_CR: Final[int] = 0
RTC: Final[int] = 1073752064
RNG_SR: Final[int] = 4
RNG_DR: Final[int] = 8
RCC_PLLCFGR: Final[int] = 4
RCC_BDCR: Final[int] = 112
RCC_APB2RSTR: Final[int] = 36
RCC_APB2LPENR: Final[int] = 100
RCC_CFGR: Final[int] = 8
RCC_CSR: Final[int] = 116
RCC_CR: Final[int] = 0
RCC_CIR: Final[int] = 12
RTC_ALRMAR: Final[int] = 28
RTC_BKP16R: Final[int] = 144
RTC_BKP15R: Final[int] = 140
RTC_BKP14R: Final[int] = 136
RTC_BKP17R: Final[int] = 148
RTC_BKP1R: Final[int] = 84
RTC_BKP19R: Final[int] = 156
RTC_BKP18R: Final[int] = 152
RTC_BKP13R: Final[int] = 132
RTC_ALRMBSSR: Final[int] = 72
RTC_ALRMBR: Final[int] = 32
RTC_ALRMASSR: Final[int] = 68
RTC_BKP0R: Final[int] = 80
RTC_BKP12R: Final[int] = 128
RTC_BKP11R: Final[int] = 124
RTC_BKP10R: Final[int] = 120
WWDG_SR: Final[int] = 8
SPI_RXCRCR: Final[int] = 20
TIM_RCR: Final[int] = 48
TIM_PSC: Final[int] = 40
TIM_OR: Final[int] = 80
TIM_SMCR: Final[int] = 8
UART5: Final[int] = 1073762304
UART4: Final[int] = 1073761280
TIM_SR: Final[int] = 16
TIM_EGR: Final[int] = 20
TIM_CR1: Final[int] = 0
TIM_CNT: Final[int] = 36
TIM_CCR4: Final[int] = 64
TIM_CR2: Final[int] = 4
TIM_DMAR: Final[int] = 76
TIM_DIER: Final[int] = 12
TIM_DCR: Final[int] = 72
USART1: Final[int] = 1073811456
USB_OTG_FS: Final[int] = 1342177280
USART_SR: Final[int] = 0
USART_GTPR: Final[int] = 24
USB_OTG_HS: Final[int] = 1074003968
WWDG_CR: Final[int] = 0
WWDG_CFR: Final[int] = 4
WWDG: Final[int] = 1073753088
USART_DR: Final[int] = 4
USART6: Final[int] = 1073812480
USART3: Final[int] = 1073760256
USART2: Final[int] = 1073759232
USART_BRR: Final[int] = 8
USART_CR3: Final[int] = 20
USART_CR2: Final[int] = 16
USART_CR1: Final[int] = 12
TIM_CCR3: Final[int] = 60
TIM1: Final[int] = 1073807360
SYSCFG_PMC: Final[int] = 4
SYSCFG_MEMRMP: Final[int] = 0
TIM10: Final[int] = 1073824768
TIM13: Final[int] = 1073748992
TIM12: Final[int] = 1073747968
TIM11: Final[int] = 1073825792
SYSCFG_EXTICR3: Final[int] = 20
SYSCFG: Final[int] = 1073821696
SPI_TXCRCR: Final[int] = 24
SPI_SR: Final[int] = 8
SYSCFG_CMPCR: Final[int] = 32
SYSCFG_EXTICR2: Final[int] = 16
SYSCFG_EXTICR1: Final[int] = 12
SYSCFG_EXTICR0: Final[int] = 8
TIM14: Final[int] = 1073750016
TIM_CCER: Final[int] = 32
TIM_BDTR: Final[int] = 68
TIM_ARR: Final[int] = 44
TIM_CCMR1: Final[int] = 24
TIM_CCR2: Final[int] = 56
TIM_CCR1: Final[int] = 52
TIM_CCMR2: Final[int] = 28
TIM9: Final[int] = 1073823744
TIM4: Final[int] = 1073743872
TIM3: Final[int] = 1073742848
TIM2: Final[int] = 1073741824
TIM5: Final[int] = 1073744896
TIM8: Final[int] = 1073808384
TIM7: Final[int] = 1073746944
TIM6: Final[int] = 1073745920
EXTI_SWIER: Final[int] = 16
DAC_DOR1: Final[int] = 44
DAC_DHR8RD: Final[int] = 40
DAC_DHR8R2: Final[int] = 28
DAC_DOR2: Final[int] = 48
DBGMCU: Final[int] = 3758366720
DAC_SWTRIGR: Final[int] = 4
DAC_SR: Final[int] = 52
DAC_DHR8R1: Final[int] = 16
DAC_DHR12L2: Final[int] = 24
DAC_DHR12L1: Final[int] = 12
DAC_CR: Final[int] = 0
DAC_DHR12LD: Final[int] = 36
DAC_DHR12RD: Final[int] = 32
DAC_DHR12R2: Final[int] = 20
DAC_DHR12R1: Final[int] = 8
DBGMCU_APB1FZ: Final[int] = 8
EXTI_EMR: Final[int] = 4
EXTI: Final[int] = 1073822720
DMA_LISR: Final[int] = 0
EXTI_FTSR: Final[int] = 12
EXTI_RTSR: Final[int] = 8
EXTI_PR: Final[int] = 20
EXTI_IMR: Final[int] = 0
DMA_LIFCR: Final[int] = 8
DBGMCU_IDCODE: Final[int] = 0
DBGMCU_CR: Final[int] = 4
DBGMCU_APB2FZ: Final[int] = 12
DMA1: Final[int] = 1073897472
DMA_HISR: Final[int] = 4
DMA_HIFCR: Final[int] = 12
DMA2: Final[int] = 1073898496
DAC1: Final[int] = 1073771520
ADC_JDR3: Final[int] = 68
ADC_JDR2: Final[int] = 64
ADC_JDR1: Final[int] = 60
ADC_JDR4: Final[int] = 72
ADC_JOFR3: Final[int] = 28
ADC_JOFR2: Final[int] = 24
ADC_JOFR1: Final[int] = 20
ADC_HTR: Final[int] = 36
ADC2: Final[int] = 1073815808
ADC123_COMMON: Final[int] = 1073816320
ADC1: Final[int] = 1073815552
ADC3: Final[int] = 1073816064
ADC_DR: Final[int] = 76
ADC_CR2: Final[int] = 8
ADC_CR1: Final[int] = 4
ADC_JOFR4: Final[int] = 32
CRC: Final[int] = 1073885184
CAN2: Final[int] = 1073768448
CAN1: Final[int] = 1073767424
CRC_CR: Final[int] = 8
DAC: Final[int] = 1073771520
CRC_IDR: Final[int] = 4
CRC_DR: Final[int] = 0
ADC_SR: Final[int] = 0
ADC_SMPR1: Final[int] = 12
ADC_LTR: Final[int] = 40
ADC_JSQR: Final[int] = 56
ADC_SMPR2: Final[int] = 16
ADC_SQR3: Final[int] = 52
ADC_SQR2: Final[int] = 48
ADC_SQR1: Final[int] = 44
RCC_APB2ENR: Final[int] = 68
FLASH: Final[int] = 1073888256
IWDG: Final[int] = 1073754112
I2S3EXT: Final[int] = 1073758208
I2S2EXT: Final[int] = 1073755136
IWDG_KR: Final[int] = 0
IWDG_SR: Final[int] = 12
IWDG_RLR: Final[int] = 8
IWDG_PR: Final[int] = 4
I2C_TRISE: Final[int] = 32
I2C_DR: Final[int] = 16
I2C_CR2: Final[int] = 4
I2C_CR1: Final[int] = 0
I2C_OAR1: Final[int] = 8
I2C_SR2: Final[int] = 24
I2C_SR1: Final[int] = 20
I2C_OAR2: Final[int] = 12
PWR: Final[int] = 1073770496
RCC_AHB3LPENR: Final[int] = 88
RCC_AHB3ENR: Final[int] = 56
RCC_AHB2RSTR: Final[int] = 20
RCC_AHB3RSTR: Final[int] = 24
RCC_APB1RSTR: Final[int] = 32
RCC_APB1LPENR: Final[int] = 96
RCC_APB1ENR: Final[int] = 64
RCC_AHB2LPENR: Final[int] = 84
RCC: Final[int] = 1073887232
PWR_CSR: Final[int] = 4
PWR_CR: Final[int] = 0
RCC_AHB1ENR: Final[int] = 48
RCC_AHB2ENR: Final[int] = 52
RCC_AHB1RSTR: Final[int] = 16
RCC_AHB1LPENR: Final[int] = 80
I2C_CCR: Final[int] = 28
GPIOD: Final[int] = 1073875968
GPIOC: Final[int] = 1073874944
GPIOB: Final[int] = 1073873920
GPIOE: Final[int] = 1073876992
GPIOH: Final[int] = 1073880064
GPIOG: Final[int] = 1073879040
GPIOF: Final[int] = 1073878016
GPIOA: Final[int] = 1073872896
FLASH_KEYR: Final[int] = 4
FLASH_CR: Final[int] = 16
FLASH_ACR: Final[int] = 0
FLASH_OPTCR: Final[int] = 20
FLASH_SR: Final[int] = 12
FLASH_OPTKEYR: Final[int] = 8
FLASH_OPTCR1: Final[int] = 24
GPIOI: Final[int] = 1073881088
GPIO_OTYPER: Final[int] = 4
GPIO_OSPEEDR: Final[int] = 8
GPIO_ODR: Final[int] = 20
GPIO_PUPDR: Final[int] = 12
I2C3: Final[int] = 1073765376
I2C2: Final[int] = 1073764352
I2C1: Final[int] = 1073763328
GPIO_MODER: Final[int] = 0
GPIO_BSRR: Final[int] = 24
GPIO_AFR1: Final[int] = 36
GPIO_AFR0: Final[int] = 32
GPIO_BSRRH: Final[int] = 26
GPIO_LCKR: Final[int] = 28
GPIO_IDR: Final[int] = 16
GPIO_BSRRL: Final[int] = 24
mem32: Incomplete  ## <class 'mem'> = <32-bit memory>
mem8: Incomplete  ## <class 'mem'> = <8-bit memory>
mem16: Incomplete  ## <class 'mem'> = <16-bit memory>
