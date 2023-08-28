Select *
From covid_data

-- New Cases and New Deaths ordered by date

Select location, date, population, new_cases, new_deaths
From covid_data
Order by date

-- Looking at Total Cases vs Total Deaths (Percentage)

Select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as Death_percentage
From covid_data
Order by 1,2


-- Looking at Total Cases vs Total Deaths (Percentage) for India
Select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as Death_percentage
From covid_data
Where location like 'India'
Order by 1,2

-- Looking at Total Cases vs Population (Percentage) for India
Select location, date, Population, total_cases, (total_cases/Population)*100 as Infection_percentage
From covid_data
Where location like 'India'
Order by 1,2


-- Looking at Countries with Highest Infection Rate compared to population

Select location, Population, Max(total_cases) as Highestinfectioncount
From covid_data
Where location like 'India'
Group by Location, Population
Order by 1,2

-- Countries with Highest Infection Rate compared to Population
Select location, population, Max(total_cases) as Highestinfectioncount, Max((total_cases/population))*100 as Percentagepopulationinfected
from covid_data
Group by Location, population
order by Percentagepopulationinfected Desc

-- Countries with Highest death count per population
Select location, population, Max(cast(total_deaths as int)) as Highestdeathcount
from covid_data
Group by Location, population
order by Highestdeathcount Desc

-- Countries with Highest death count per population (percentage)
Select location, population, Max(total_deaths) as Highestdeathcount, Max((total_deaths/population))*100 as Percentagepopulationdeath
from covid_data
Group by Location, population
order by Percentagepopulationdeath Desc

-- Countries with Highest death count per population (India)
Select location, population, Max(total_deaths) as Highestdeathcount, Max((total_deaths/population))*100 as Percentagepopulationdeath
from covid_data
Where location like 'India'
Group by Location, population
order by Percentagepopulationdeath Desc

-- by Continent

Select continent, Max(cast(total_deaths as int)) as Total_Death_Count
From covid_data
Where continent is not null
Group by continent
order by Total_Death_Count desc

--World Wide Data
Select sum(new_cases) as total_cases_worldwide 
From Covid_data

Select sum(new_deaths) as total_deaths_worldwide 
From Covid_data
