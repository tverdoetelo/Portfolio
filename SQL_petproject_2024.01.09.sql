Select *
From PortfolioProject1..CovidDeaths
Where continent is not NULL
order by 3,4

--Select *
--From PortfolioProject1..CovidVaccinations
--Where continent is not NULL
--order by 3,4

--Select Data that we are going to be using

Select location, date, total_cases, new_cases, total_deaths, population
From PortfolioProject1..CovidDeaths
Where continent is not NULL
order by 1,2

-- Looking at Total Cases vs Total Deaths
-- Shows likelihood of deying if you contract covid in your country
Select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
From PortfolioProject1..CovidDeaths
Where location like '%germany%'
order by 1,2

-- Looking at Total Cases vs Population
-- Shows what percentage of population got covid in your country
Select location, date, population, total_cases, (total_cases/population)*100 as PercentagePopelationInfected
From PortfolioProject1..CovidDeaths
Where location like '%germany%'
order by 1,2

-- Looking at Countries with Highest Infection Rate compared to Population
-- Shows what percentage of population got covid in your country
Select location, population, MAX(total_cases) as  HighestInfectionCount, MAX(total_cases/population)*100 as PercentagePopelationInfected
From PortfolioProject1..CovidDeaths
Where continent is not NULL
Group by location, population
order by PercentagePopelationInfected desc

--Showing Countries with Highest Death Count per Population
Select location, MAX(cast(total_deaths as int)) as  TotalDeathCount
From PortfolioProject1..CovidDeaths
Where continent is not NULL
Group by location
order by TotalDeathCount desc

--Showing Continents with Highest Death Count per Population
Select location, MAX(cast(total_deaths as int)) as  TotalDeathCount
From PortfolioProject1..CovidDeaths
Where continent is NULL
Group by location
order by TotalDeathCount desc

--Global numbers
Select date, SUM(new_cases) as TotalCases, SUM(cast(new_deaths as int)) as TotalDeaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100 as DeathPercentage
From PortfolioProject1..CovidDeaths
Where continent is not NULL
Group by date
order by 1,2

--Global numbers
Select SUM(new_cases) as TotalCases, SUM(cast(new_deaths as int)) as TotalDeaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100 as DeathPercentage
From PortfolioProject1..CovidDeaths
Where continent is not NULL
order by 1,2;


--Looking at Total Population vs Vaccinations

With PopvsVac (continent, location, date, population, new_vaccinations, RollingPeopleVaccinated)
as 
(
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(CONVERT(int, vac.new_vaccinations)) OVER (Partition by dea.location order by dea.location, dea.date) as RollingPeopleVaccinated
From PortfolioProject1..CovidDeaths dea
Join PortfolioProject1..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
Where dea.continent is not NULL
)
Select *, (RollingPeopleVaccinated/population)*100 as PercentageVaccinatedPeople
From PopvsVac