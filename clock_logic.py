def calculate_acute_angle(hours, minutes):
    """Return the acute angle between the hour and minute hands."""
    hour = hours % 12
    hour_angle = 30 * hour + 0.5 * minutes
    minute_angle = 6 * minutes
    difference = abs(hour_angle - minute_angle)
    return min(difference, 360 - difference)
