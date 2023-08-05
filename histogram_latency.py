import pandas as pd
import matplotlib.pyplot as plt

settledToNextStarted = 4
snapshotGenerationTime = 6.069

columns = ['date', 'code', 'type', 'latency']
events = pd.read_csv('events.txt', sep=';', header=None, names=columns)

events_filtered = events.where(events['latency'] < 15)

# Basic statistics:
print(events.describe())
print("med", events['latency'].median())

events_filtered.hist(column='latency', bins = 50)
percentage_above = events_filtered.loc[events_filtered['latency'] > settledToNextStarted, 'latency'].count() / events_filtered['latency'].count()
plt.axvline(settledToNextStarted, color='red')
plt.axvline(snapshotGenerationTime, color='blue')
plt.xlabel("Latency(seconds)")
plt.ylabel("Count")
plt.text(settledToNextStarted + 0.3, plt.ylim()[1]*0.9, f"Median time between rounds: {settledToNextStarted}s", color='red')
plt.text(settledToNextStarted + 0.3, plt.ylim()[1]*0.8, f"Events above: {percentage_above:.2f}", color='red')
plt.text(snapshotGenerationTime + 0.3, plt.ylim()[1]*0.5, f"Snapshot availability median: {snapshotGenerationTime:.2f}s", color='blue')


plt.title('Latency: Time between round end and event availability in Kafka.')

plt.show()
