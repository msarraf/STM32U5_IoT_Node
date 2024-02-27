################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Drivers/BSP/b_u585i_iot02a_bus.c \
../Drivers/BSP/b_u585i_iot02a_ranging_sensor.c \
../Drivers/BSP/platform.c \
../Drivers/BSP/vl53l5cx.c \
../Drivers/BSP/vl53l5cx_api.c \
../Drivers/BSP/vl53l5cx_plugin_detection_thresholds.c 

OBJS += \
./Drivers/BSP/b_u585i_iot02a_bus.o \
./Drivers/BSP/b_u585i_iot02a_ranging_sensor.o \
./Drivers/BSP/platform.o \
./Drivers/BSP/vl53l5cx.o \
./Drivers/BSP/vl53l5cx_api.o \
./Drivers/BSP/vl53l5cx_plugin_detection_thresholds.o 

C_DEPS += \
./Drivers/BSP/b_u585i_iot02a_bus.d \
./Drivers/BSP/b_u585i_iot02a_ranging_sensor.d \
./Drivers/BSP/platform.d \
./Drivers/BSP/vl53l5cx.d \
./Drivers/BSP/vl53l5cx_api.d \
./Drivers/BSP/vl53l5cx_plugin_detection_thresholds.d 


# Each subdirectory must supply rules for building sources it contributes
Drivers/BSP/%.o Drivers/BSP/%.su Drivers/BSP/%.cyclo: ../Drivers/BSP/%.c Drivers/BSP/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m33 -std=gnu11 -g3 -DDEBUG -DUSE_FULL_LL_DRIVER -DUSE_HAL_DRIVER -DSTM32U585xx -c -I../Drivers/BSP -I../Core/Inc -I../Drivers/STM32U5xx_HAL_Driver/Inc -I../Drivers/STM32U5xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32U5xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Drivers-2f-BSP

clean-Drivers-2f-BSP:
	-$(RM) ./Drivers/BSP/b_u585i_iot02a_bus.cyclo ./Drivers/BSP/b_u585i_iot02a_bus.d ./Drivers/BSP/b_u585i_iot02a_bus.o ./Drivers/BSP/b_u585i_iot02a_bus.su ./Drivers/BSP/b_u585i_iot02a_ranging_sensor.cyclo ./Drivers/BSP/b_u585i_iot02a_ranging_sensor.d ./Drivers/BSP/b_u585i_iot02a_ranging_sensor.o ./Drivers/BSP/b_u585i_iot02a_ranging_sensor.su ./Drivers/BSP/platform.cyclo ./Drivers/BSP/platform.d ./Drivers/BSP/platform.o ./Drivers/BSP/platform.su ./Drivers/BSP/vl53l5cx.cyclo ./Drivers/BSP/vl53l5cx.d ./Drivers/BSP/vl53l5cx.o ./Drivers/BSP/vl53l5cx.su ./Drivers/BSP/vl53l5cx_api.cyclo ./Drivers/BSP/vl53l5cx_api.d ./Drivers/BSP/vl53l5cx_api.o ./Drivers/BSP/vl53l5cx_api.su ./Drivers/BSP/vl53l5cx_plugin_detection_thresholds.cyclo ./Drivers/BSP/vl53l5cx_plugin_detection_thresholds.d ./Drivers/BSP/vl53l5cx_plugin_detection_thresholds.o ./Drivers/BSP/vl53l5cx_plugin_detection_thresholds.su

.PHONY: clean-Drivers-2f-BSP

