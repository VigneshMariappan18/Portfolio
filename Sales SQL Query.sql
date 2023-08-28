SELECT *
	FROM [SQL Data Cleaning].dbo.['supermarket_sales']

-- Standardising Time Format

Select time, convert(time,time)
FROM [SQL Data Cleaning].dbo.['supermarket_sales']

update ['supermarket_sales']
set time = convert(time,time)

alter table ['supermarket_sales']
add Time_converted time;

update ['supermarket_sales']
set time_converted = convert(time,time)

Select time_converted, convert(time,time)
FROM [SQL Data Cleaning].dbo.['supermarket_sales']
 
-- Standardising Date Format

Select *
FROM [SQL Data Cleaning].dbo.['supermarket_sales']


-- Finding total sales

Select sum(total) as total_sales
from [SQL Data Cleaning].dbo.['supermarket_sales']

--Finding City wise total sales

Select city, sum(total) as total_sales
from [SQL Data Cleaning].dbo.['supermarket_sales']
group by city

--Finding Gender wise total sales

Select gender, sum(total) as total_sales
from [SQL Data Cleaning].dbo.['supermarket_sales']
group by gender

--Payment type total

Select payment, sum(total) as total_sales
from [SQL Data Cleaning].dbo.['supermarket_sales']
group by payment
