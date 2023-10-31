# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: ZACHARY HARBERT
# Section: 562
# Assignment: 9.16 LAB: Small functions
# Date: 25 OCTOBER 2023
#
#
# YOUR CODE HERE
#

import math

def parta(r_sphere, r_hole): 
    #FUNCTION A
    volume = ((4*math.pi)/3) * (r_sphere**2 - r_hole**2)**(3/2)
    return volume


def partb(n):
    #FUNCTION B
    if n <= 0:
        return False

    result = []
    start = 1
    end = 1
    current_sum = 1

    while start <= n // 2:
        if current_sum < n:
            end += 2
            current_sum += end
        elif current_sum > n:
            current_sum -= start
            start += 2
        else:
            result.append(list(range(start, end + 1, 2)))
            current_sum -= start
            start += 2

    if not result:
        return False
    else:
        return result[0]

def partc(border_char, name, company, email):
    #FUNCTION C
    max_length = max(len(name), len(company), len(email))
    padding = 2
    padding1 = 3

    border_line = border_char * (max_length + 2 * padding1)
    name_line = f"{border_char}{name.center(max_length + 2 * padding)}{border_char}"
    company_line = (
        f"{border_char}{company.center(max_length + 2 * padding)}{border_char}"
    )
    email_line = f"{border_char}{email.center(max_length + 2 * padding)}{border_char}"

    digital_card = (
        f"{border_line}\n{name_line}\n{company_line}\n{email_line}\n{border_line}"
    )
    return digital_card

def partd(numbers):
    #FUNCTION D
    if not numbers:
        return None

    minimum = min(numbers)
    maximum = max(numbers)

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]

    return (minimum, median, maximum)


def parte(times, distances):
    #FUNCTION E
    if len(times) < 2 or len(distances) < 2 or len(times) != len(distances):
        return []

    velocities = []
    for i in range(1, len(times)):
        time_difference = times[i] - times[i - 1]
        distance_difference = distances[i] - distances[i - 1]
        velocity = distance_difference / time_difference
        velocities.append(velocity)

    return velocities


def partf(numbers):
    #FUNCTION F
    if len(numbers) < 2:
        return False

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 2027:
                return numbers[i] * numbers[j]

    return False
