import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"c:\Users\aishs\Downloads\Unemployment in India.csv")
print("First Five Rows")
print(df.head())
print("\nDataset Information")
print(df.info())
print("\nColumn Names")
print(df.columns)
df.columns = df.columns.str.strip()
df.rename(columns={
    'Region': 'State',
    'Date': 'Date',
    'Estimated Unemployment Rate (%)': 'Unemployment_Rate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Labour_Participation_Rate'
}, inplace=True)
print("\nMissing Values")
print(df.isnull().sum())
# Remove missing values
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()
print("\nCleaned Dataset")
print(df.head())
print("\nStatistical Summary")
print(df.describe())
print("\nAverage Unemployment Rate")
print(df['Unemployment_Rate'].mean())
print("\nHighest Unemployment Rate")
print(df['Unemployment_Rate'].max())
print("\nLowest Unemployment Rate")
print(df['Unemployment_Rate'].min())
sns.set_style("whitegrid")
plt.figure(figsize=(8,5))
sns.histplot(df['Unemployment_Rate'], bins=20, color='skyblue')
plt.title("Distribution of Unemployment Rate")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Frequency")
plt.show()
monthly = df.groupby("Date")["Unemployment_Rate"].mean()
plt.figure(figsize=(12,6))
plt.plot(monthly.index, monthly.values, marker='o')
plt.title("Average Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
state_avg = df.groupby("State")["Unemployment_Rate"].mean().sort_values()
plt.figure(figsize=(12,8))
state_avg.plot(kind='barh', color='orange')
plt.title("Average Unemployment Rate by State")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("State")
plt.show()
covid = df[df['Year'] == 2020]

plt.figure(figsize=(12,6))
sns.lineplot(data=covid,
             x='Date',
             y='Unemployment_Rate',
             marker='o')
plt.title("Covid-19 Impact on Unemployment (2020)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.show()
month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']

monthly_avg = df.groupby('Month')['Unemployment_Rate'].mean().reindex(month_order)
plt.figure(figsize=(10,5))
sns.barplot(x=monthly_avg.index,
            y=monthly_avg.values,
            palette='viridis')
plt.xticks(rotation=45)
plt.title("Average Monthly Unemployment Rate")
plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")
plt.show()
plt.figure(figsize=(6,5))
sns.heatmap(df[['Unemployment_Rate',
                'Employed',
                'Labour_Participation_Rate']].corr(),
            annot=True,
            cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
print("\n==============================")
print("KEY INSIGHTS")
print("==============================")
print(f"Average Unemployment Rate : {df['Unemployment_Rate'].mean():.2f}%")
highest = df.loc[df['Unemployment_Rate'].idxmax()]
print(f"Highest Unemployment:")
print(f"State : {highest['State']}")
print(f"Rate  : {highest['Unemployment_Rate']}%")
lowest = df.loc[df['Unemployment_Rate'].idxmin()]
print(f"\nLowest Unemployment:")
print(f"State : {lowest['State']}")
print(f"Rate  : {lowest['Unemployment_Rate']}%")
print("\nCovid-19 caused a noticeable increase in unemployment during 2020.")
print("\nSeasonal trends indicate unemployment fluctuates across different months.")
print("\nPolicy Suggestions:")
print("1. Increase employment opportunities during economic downturns.")
print("2. Support small businesses with financial assistance.")
print("3. Strengthen skill development programs.")
print("4. Improve rural employment schemes.")
print("5. Focus on job creation in high-unemployment states.")