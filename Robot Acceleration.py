# https: // programmingelectronics.com/3-ways-to-use-acceleration-in-an-arduino-sketch
import math
import time


# def AccelerationTo(current_power, MaxSpeed):
#     time = 1
#     growth_rate = 1.03  # Growth Rate
#     if current_power < 1:
#         current_power = 1
#     while current_power < MaxSpeed:
#         # Calculation of acceleration using doubling time
#         Increase = current_power * (growth_rate ** time)
#         current_power = current_power+Increase
#         if current_power > MaxSpeed:
#             current_power = MaxSpeed
#         time += 1
#         print("Speed: ", current_power)
#         print("time:", time)


# def DeaccelerationTo(current_power, min_power):
#     time = 1
#     growth_rate = 1.03  # Growth Rate
#     if current_power < 0:
#         while current_power < min_power:
#             # Calculation of acceleration using doubling time
#             current_power = current_power + \
#                 (current_power * math.ceil(growth_rate ** time))
#             print(current_power)
#             time += 1
#     else:  # Current Power >= 0
#         while current_power > min_power:
#             current_power = current_power - \
#                 (current_power * math.ceil(growth_rate ** time))
#             time += 1
#         print("Speed: ", current_power)
#         print("time:", time)


# def AccelerationToV2(current_power, MaxSpeed):
#     time = 1
#     growth_rate = 1.03  # Growth Rate

#     if current_power < 1:
#         current_power = 1
#     while current_power < MaxSpeed:
#         current_power = current_power*(growth_rate**time)
#         # Calculation of acceleration using doubling time
#         if current_power > MaxSpeed:
#             current_power = MaxSpeed
#         time += 1
#         print("Speed: ", current_power)
#         print("time:", time)

# FINAL
def deaccelerate_to(current_power, min_power):
    time = 1
    growth_rate = .9  # Growth Rate

    while current_power != min_power:
        # Calculation of acceleration using doubling time
        current_power = int(current_power * (growth_rate ** time))
        # Checks to ensure that the value is not missed
        if current_power == -1 or current_power == 1:
            current_power = min_power
        # Iterate time for next calculation
        time += 1
        print("Speed: ", current_power)
        print("time:", time)

# FINAL


def forward_accelerate_to(current_power, max_power):
    time = 1
    growth_rate = 1.03  # Growth Rate
    # Check to ensure that there is a speed greater than one.
    if current_power == 0 or current_power == 1:
        current_power = 2

    while current_power != max_power:
        # Calculation of acceleration using doubling time
        current_power = int(current_power * (2 ** growth_rate))
        # Checks to ensure that the value is not missed
        if current_power > max_power:
            current_power = max_power
        # Iterate time for next calculation
        time += 1
        print("Speed: ", current_power)
        print("time:", time)

# FINAL


def reverse_accelerate_to(current_power, max_power):
    time = 1
    growth_rate = 1.03  # Growth Rate
    # Check to ensure that there is a speed greater than one.
    if current_power == 0 or current_power == -1:
        current_power = -2

    while current_power != max_power:
        # Calculation of acceleration using doubling time
        current_power = current_power * (growth_rate ** time)
        # Checks to ensure that the value is not missed
        if current_power < max_power:
            current_power = max_power
        # Iterate time for next calculation
        time += 1
        print("Speed: ", current_power)
        print("time:", time)


forward_accelerate_to(0, 100)
