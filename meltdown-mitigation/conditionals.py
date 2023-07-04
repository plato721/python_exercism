"""Functions to prevent a nuclear meltdown."""
CRITICAL_TEMPERATURE_MAX = 800
CRITICAL_NEUTRONS_MIN = 500
TEMPERATURE_NEUTRONS_MAX_PRODUCT = 500000

GREEN_EFFICIENCY_MIN = 80
ORANGE_EFFICIENCY_MIN = 60
RED_EFFICIENCY_MIN = 30

LOW_NORMAL_STATUS_PERCENT = 0.9
HIGH_NORMAL_STATUS_PERCENT = 1.1
LOW_STATUS_PERCENT = 0.9


def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < CRITICAL_TEMPERATURE_MAX and \
        neutrons_emitted > CRITICAL_NEUTRONS_MIN and \
        temperature * neutrons_emitted < TEMPERATURE_NEUTRONS_MAX_PRODUCT


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = get_generated_power(voltage, current)
    efficiency = get_efficiency_percentage(generated_power, theoretical_max_power)

    if efficiency >= GREEN_EFFICIENCY_MIN:
        return 'green'
    elif efficiency >= ORANGE_EFFICIENCY_MIN:
        return 'orange'
    elif efficiency >= RED_EFFICIENCY_MIN:
        return 'red'
    else:
        return 'black'


def get_efficiency_percentage(generated_power, theoretical_max_power):
    return generated_power / theoretical_max_power * 100


def get_generated_power(voltage, current):
    return voltage * current


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    status_percentage = get_status(temperature, neutrons_produced_per_second)

    if is_low_status(status_percentage, threshold):
        return 'LOW'
    elif is_normal_status(status_percentage, threshold):
        return 'NORMAL'
    else:
        return 'DANGER'


def get_status(temperature, neutrons_produced_per_second):
    return temperature * neutrons_produced_per_second


def is_low_status(status, threshold):
    return status < threshold * LOW_STATUS_PERCENT


def is_normal_status(status, threshold):
    return threshold * HIGH_NORMAL_STATUS_PERCENT > status > threshold * LOW_NORMAL_STATUS_PERCENT
