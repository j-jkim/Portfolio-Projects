-- COVID19 DATA EXPLORATION ANALYSIS 
-- Skills used: Joins, CTE's, Temp Tables, Windows Functions, Aggregate Functions, Creating Views, Converting Data Types


-- EXPLORING COVID DEATHS TABLE
-- Query to see available data in table
SELECT location, date, total_cases, new_cases, total_deaths, population
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
ORDER BY 1,2;


-- Investigating total cases & total deaths
-- How likely is it to die from COVID in South Korea?
SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 AS death_percentage
FROM PortfolioProject..CovidDeaths
WHERE location = 'South Korea' AND continent IS NOT NULL
ORDER BY 1,2;

-- Investigating total cases & population
-- What is the total percentage of people who contracted COVID from total population in South Korea?
SELECT location, date, total_cases, population, (total_cases/population)*100 AS total_cases_percentage
FROM PortfolioProject..CovidDeaths
WHERE location = 'South Korea' AND continent IS NOT NULL
ORDER BY 1,2;

-- Which countries have the highest infection % compared to population?
SELECT location,population, MAX(total_cases) AS highest_infection_count, MAX((total_cases/population))*100 AS percent_pop_infected
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
GROUP BY location, population
ORDER BY percent_pop_infected DESC;


-- Countries with highest death toll per population
SELECT location, MAX(cast(total_deaths AS INT)) AS max_death_count
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
GROUP BY location
ORDER BY max_death_count DESC;


-- Continents with death toll per population
SELECT continent, SUM(cast(new_deaths AS INT)) AS total_deaths
FROM PortfolioProject..CovidDeaths
WHERE continent IS NOT NULL
GROUP BY continent
ORDER BY total_deaths DESC;



-- EXPLORING VACCINATIONS TABLE
-- Query joining COVID DEATHS and COVID VACCINATIONS tables
SELECT *
FROM PortfolioProject..CovidDeaths dea
JOIN PortfolioProject..CovidVaccinations vac
	ON  dea.location = vac.location
	AND dea.date = vac.date;


-- Investigating total population & vaccinations
-- Query to set up rolling count of vaccinations per updated case
-- Shows percentage of population that has received at least one vaccine
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, 
SUM(CONVERT(BIGINT,vac.new_vaccinations)) 
OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS rolling_vax_count
FROM PortfolioProject..CovidDeaths dea
JOIN PortfolioProject..CovidVaccinations vac
	ON  dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
ORDER BY 2,3;

-- Same query as previous one but using CTE to perform calculation on PARTITION BY
WITH PopvsVac (continent, location, date, population, new_vaccinations, rolling_vax_count)
AS 
(
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, 
SUM(CONVERT(BIGINT,vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS rolling_vax_count
FROM PortfolioProject..CovidDeaths dea
JOIN PortfolioProject..CovidVaccinations vac
	ON  dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
)
-- Query to look at rolling vaccination totals & percentage from newer vaccination #s daily
SELECT *, (rolling_vax_count/population)*100
FROM PopvsVac;



-- Same query as previous one but creating a temp table to perform calculation on PARTITION BY
DROP TABLE IF EXISTS #PercentPopulationVaccinated
CREATE TABLE #PercentPopulationVaccinated
(
continent nvarchar(255),
location nvarchar(255),
date datetime,
population numeric,
new_vaccinations numeric,
rolling_vax_count numeric
)

INSERT INTO #PercentPopulationVaccinated
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, 
SUM(CONVERT(BIGINT,vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS rolling_vax_count
FROM PortfolioProject..CovidDeaths dea
JOIN PortfolioProject..CovidVaccinations vac
	ON  dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
-- Query to look at rolling vaccination totals & percentage from newer vaccination #s daily
SELECT *, (rolling_vax_count/population)*100
FROM #PercentPopulationVaccinated;


-- Creating a VIEW for potential visualization
CREATE VIEW PercentPopulationVaccinated AS
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
SUM(CONVERT(BIGINT,vac.new_vaccinations)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS
rolling_vax_count
FROM PortfolioProject.dbo.CovidDeaths dea
JOIN PortfolioProject.dbo.CovidVaccinations vac
	ON dea.location = vac.location AND dea.date = vac.date
WHERE dea.continent IS NOT NULL;


SELECT *
FROM PercentPopulationVaccinated;