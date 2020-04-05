# importing modules
import pandas as pd

# Read datasets/yearly_deaths_by_clinic.csv into yearly
yearly = pd.read_csv('datasets/yearly_deaths_by_clinic.csv')

# Print out yearly
print (yearly)

# Calculate proportion of deaths per no. births
yearly["proportion_deaths"] = yearly["deaths"]/ yearly["births"]
# Extract clinic 1 data into yearly1 and clinic 2 data into yearly2
yearly1 = yearly[yearly.clinic == 'clinic 1']
yearly2 = yearly[yearly.clinic == 'clinic 2']

# Print out yearly1
print(yearly1)


# Plot yearly proportion of deaths at the two clinics
ax = yearly1.plot('year','proportion_deaths', label='clinic 1')
yearly2.plot('year', 'proportion_deaths', label='clinic 2', ax= ax)

# Read datasets/monthly_deaths.csv into monthly
monthly = pd.read_csv('datasets/monthly_deaths.csv', parse_dates=["date"])
# pd.to_datetime(monthly.date)
# Calculate proportion of deaths per no. births
monthly["proportion_deaths"] = monthly["deaths"] / monthly["births"]

# Print out the first rows in monthly
print(monthly.head())

# Plot monthly proportion of deaths

ax = monthly.plot( 'date','proportion_deaths', label='monthly')

# Date when handwashing was made mandatory
handwashing_start = pd.to_datetime('1847-06-01')

# Split monthly into before and after handwashing_start
before_washing = monthly[monthly["date"] < handwashing_start]
after_washing = monthly[monthly["date"] >= handwashing_start]
ax = before_washing.plot('date','proportion_deaths', label='before_washing')
after_washing.plot('date', 'proportion_deaths', label='after_washing', ax=ax)


# Difference in mean monthly proportion of deaths due to handwashing
before_proportion = before_washing['proportion_deaths']
after_proportion = after_washing['proportion_deaths']
mean_diff = after_proportion.mean() - before_proportion.mean()
mean_diff

# A bootstrap analysis of the reduction of deaths due to handwashing
boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac=1, replace=True)
    boot_after = after_proportion.sample(frac=1, replace=True)
    boot_mean_diff.append(boot_after.mean() - boot_before.mean())

# Calculating a 95% confidence interval from boot_mean_diff 
confidence_interval = monthly.quantile([0.025, 0.975])
confidence_interval
