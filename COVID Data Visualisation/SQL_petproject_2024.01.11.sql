--Table 1
Select SUM(new_cases) as TotalCases, SUM(cast(new_deaths as int)) as TotalDeaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100 as DeathPercentage
From PortfolioProject1..CovidDeaths
Where continent is not NULL
order by 1,2;

--Table 2
Select location, MAX(cast(total_deaths as int)) as  TotalDeathCount
From PortfolioProject1..CovidDeaths
Where continent is NULL
and location not in ('World', 'European Union', 'International')
Group by location
order by TotalDeathCount desc

--Table3
Select location, population, MAX(total_cases) as  HighestInfectionCount, MAX(total_cases/population)*100 as PercentagePopulationInfected
From PortfolioProject1..CovidDeaths
Group by location, population
order by PercentagePopulationInfected desc

--Table4
Select location, population, date, MAX(total_cases) as  HighestInfectionCount, MAX(total_cases/population)*100 as PercentagePopulationInfected
From PortfolioProject1..CovidDeaths
Group by location, population, date
order by PercentagePopulationInfected desc
