import pandas as pd

# Load the CSV file
df = pd.read_csv("owid-covid-data.csv")

print(df.columns)

print(df.head())

print(df.isnull().sum())

countries=['Kenya','United States','India']
df_filtered=df[df['location'].isin(countries)]

df_filtered=df_filtered.dropna(subset=['date','total_cases'])

df_filtered['date']=pd.to_datetime(df_filtered['date'])
df_filtered=df_filtered.fillna(method='ffill')

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='total_cases', hue='location')
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend(title='Country')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.lineplot(data=df_filtered, x='date', y='new_cases', hue='location')
plt.title(' Daily New COVID-19 Cases ')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend(title='Country')
plt.tight_layout()
plt.show()

df_filtered['death_rate']=df_filtered['total_deaths']/df_filtered['total_cases']
plt.figure(figsize=(12,6))
sns.lineplot(data=df_filtered, x='date', y='death_rate', hue='location')
plt.title('COVID-19 Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate (Deaths/Cases')
plt.legend(title='Country')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.lineplot(data=df_filtered, x='date', y='total_vaccinations', hue='location')
plt.title('Cummulative COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend(title='Country')
plt.tight_layout()
plt.show()

latest_vax=df_filtered.sort_values('date').groupby('location').tail(1)

plt.figure(fig_size=(8, 5))
sns.barplot(data=latest_vax, x='location', y='people_vaccinated_per_hundred')
plt.title('Percentage of population Vaccinated(Latest Available Data)')
plt.xlabel('Country')
plt.ylabel('% Vaccination')
plt.ylim(0, 100)
plt.tight_layout()
plt.show()




