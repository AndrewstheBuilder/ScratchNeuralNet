import pandas as pd
import numpy as np

def generate_data():
    # Define parameters
    days_total = 100
    readings_per_day = 1
    daily_fluctuation = 5

    # Prepare empty lists to store the generated data
    day_temperatures = {
        'Day': [],
        'Temperature': []
    }

    # Generate temperatures for days 1-70 (gradual increase)
    for day in range(1, 71):
        # Base temperature (linear increase from 80 to 95 over 70 days)
        base_temp = 80 + (95 - 80) * (day / 70)

        # Generate (readings_per_day) readings for the day, within 5 degrees of the base temperature
        daily_temps = np.random.uniform(base_temp - 2.5, base_temp + 2.5, readings_per_day)

        # Store the data
        day_temperatures['Day'].extend([day] * readings_per_day)
        day_temperatures['Temperature'].extend(daily_temps)

    # Generate temperatures for days 71-100 (gradual decrease)
    for day in range(71, 101):
        # Base temperature (linear decrease from 95 to 70 over 30 days)
        base_temp = 95 - (95 - 70) * ((day - 70) / 30)

        # Generate (readings_per_day) readings for the day, within 5 degrees of the base temperature
        daily_temps = np.random.uniform(base_temp - 2.5, base_temp + 2.5, readings_per_day)

        # Store the data
        day_temperatures['Day'].extend([day] * readings_per_day)
        day_temperatures['Temperature'].extend(daily_temps)

    # Convert to a DataFrame for easier handling and visualization
    florida_fall_df = pd.DataFrame(day_temperatures)

    return florida_fall_df