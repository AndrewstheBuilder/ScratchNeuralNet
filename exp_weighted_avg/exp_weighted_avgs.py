from generate_data import generate_data
import matplotlib.pyplot as plt
import pandas as pd

florida_fall_df = generate_data()
# print('florida_fall_df', florida_fall_df)

# Plotting
# ax = florida_fall_df.plot(kind='scatter', x='Day', y='Temperature', title='Synthetic Florida Fall Temperature Data', figsize=(10, 6), alpha=0.7, color='orange')
# ax.set_xlabel("Day")
# ax.set_ylabel("Temperature (°F)")

# Implement exponentially weighted averaging
# vt = beta*(v(t-1)) + (1-beta)*theta(t)
# v(0) = 0.0
# Three values of beta: 0.9(red), 0.98(green), 0.5(blue)
running_avg = [0.0, 0.0, 0.0] # v(0) for three betas
running_avg_final_01 = []
running_avg_final_02 = []
running_avg_final_03 = []
beta_01 = 0.9
beta_02 = 0.98
beta_03 = 0.5

# Iterate through each row in the DataFrame
for index, row in florida_fall_df.iterrows():
    day = row['Day']
    temperature = row['Temperature']
    running_avg[0] = beta_01 * running_avg[0] + (1-beta_01) * temperature
    running_avg[1] = beta_02 * running_avg[1] + (1-beta_02) * temperature
    running_avg[2] = beta_03 * running_avg[2] + (1-beta_03) * temperature
    running_avg_final_01.append(running_avg[0])
    running_avg_final_02.append(running_avg[1])
    running_avg_final_03.append(running_avg[2])
    print(f'Day: {day}, Temperature: {temperature}')

plt.figure(figsize=(10, 6))
plt.scatter(florida_fall_df['Day'], florida_fall_df['Temperature'], alpha=0.7, color='black')
# Line plot for beta value: 0.9
plt.plot(florida_fall_df['Day'], running_avg_final_01, color='red', linestyle='-', linewidth=1.5, alpha=0.7, label='beta: 0.9')

# Line plot for beta value: 0.98
plt.plot(florida_fall_df['Day'], running_avg_final_02, color='green', linestyle='--', linewidth=1.5, alpha=0.7, label='beta: 0.98')

# Line plot for beta value: 0.5
plt.plot(florida_fall_df['Day'], running_avg_final_03, color='blue', linestyle='-.', linewidth=1.5, alpha=0.7, label='beta: 0.5')

plt.title('Exponentially Weighted Average for Temperature Across 100 Days')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.legend(loc='lower right')

plt.show()