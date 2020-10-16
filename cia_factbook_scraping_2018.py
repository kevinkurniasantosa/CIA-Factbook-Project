import json
import os
import re
from bs4 import BeautifulSoup
import unicodedata
import csv
import time

print('import success')

# Define variables - YOU CAN CUSTOMIZE IT DEPENDS ON YOUR NEEDS
input_directory = os.getcwd() + '\\json' # THE JSONS FOLDER/DIRECTORY
output_filename = 'CIA Factbook output.csv' # THE OUTPUT FILENAME

def clean_string(string):
    string = string.replace('\"', '\'\'').replace('\r', ' ').replace('\n', ' ')
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore')
    string = string.decode('ascii')

    return string

def main(data):
    # Name
    try:
        name = data['name']
    except:
        name = '-'
    print('Name: ' + name)

    # Area
    try:
        area = soup.find('div', {'id': 'field-area'}).find('span', class_='subfield-number').text
    except:
        area = '-'
    print('Area: ' + area)

    # Population
    try:
        population = soup.find('div', {'id': 'field-population'}).find('span', class_='subfield-number').text
    except:
        population = '-'
    print('Population: ' + population)

    # Population growth rate
    try:
        population_growth_rate = soup.find('div', {'id': 'field-population-growth-rate'}).find('span', class_='subfield-number').text
    except:
        population_growth_rate = '-'
    print('Population growth rate: ' + population_growth_rate)

    # Birth rate
    try:
        birth_rate = soup.find('div', {'id': 'field-birth-rate'}).find('span', class_='subfield-number').text
    except:
        birth_rate = '-'
    print('Birth rate: ' + birth_rate)

    # Death rate
    try:
        death_rate = soup.find('div', {'id': 'field-death-rate'}).find('span', class_='subfield-number').text
    except:
        death_rate = '-'
    print('Death rate: ' + death_rate)

    # Net migration rate
    try:
        net_migration_rate = soup.find('div', {'id': 'field-net-migration-rate'}).find('span', class_='subfield-number').text
    except:
        net_migration_rate = '-'
    print('Net migration rate: ' + net_migration_rate)

    # Maternal mortality rate
    try:
        maternal_mortality_rate = soup.find('div', {'id': 'field-maternal-mortality-rate'}).find('span', class_='subfield-number').text
    except:
        maternal_mortality_rate = '-'
    print('Maternal mortality rate: ' + maternal_mortality_rate)

    # Infant mortality rate
    try:
        infant_mortality_rate = soup.find('div', {'id': 'field-infant-mortality-rate'}).find('span', class_='subfield-number').text
    except:
        infant_mortality_rate = '-'
    print('Infant mortality rate: ' + infant_mortality_rate)

    # Life expectancy at birth
    try:
        life_expectancy = soup.find('div', {'id': 'field-life-expectancy-at-birth'}).find('span', class_='subfield-number').text
    except:
        life_expectancy = '-'
    print('Life expectancy at birth: ' + life_expectancy)

    # Total fertility rate
    try:
        total_fertility_rate = soup.find('div', {'id': 'field-total-fertility-rate'}).find('span', class_='subfield-number').text
    except:
        total_fertility_rate = '-'
    print('Total fertility rate: ' + total_fertility_rate)

    # Health expenditures
    try:
        health_expenditures = soup.find('div', {'id': 'field-health-expenditures'}).find('span', class_='subfield-number').text
    except:
        health_expenditures = '-'
    print('Health expenditures: ' + health_expenditures)

    # HIV/AIDS - adult prevalence rate
    try:
        hiv_adult_prevalence = soup.find('div', {'id': 'field-hiv-aids-adult-prevalence-rate'}).find('span', class_='subfield-number').text
    except:
        hiv_adult_prevalence = '-'
    print('HIV/AIDS - adult prevalence rate: ' + hiv_adult_prevalence)

    # HIV/AIDS - people living with HIV/AIDS
    try:
        hiv_people_living = soup.find('div', {'id': 'field-hiv-aids-people-living-with-hiv-aids'}).find('span', class_='subfield-number').text
    except:
        hiv_people_living = '-'
    print('HIV/AIDS - people living with HIV/AIDS: ' + hiv_people_living)

    # HIV/AIDS - deaths
    try:
        hiv_deaths = soup.find('div', {'id': 'field-hiv-aids-deaths'}).find('span', class_='subfield-number').text
    except:
        hiv_deaths = '-'
    print('HIV/AIDS - deaths: ' + hiv_deaths)

    # Obesity - adult prevalence rate
    try:
        obesity_rate = soup.find('div', {'id': 'field-obesity-adult-prevalence-rate'}).find('span', class_='subfield-number').text
    except:
        obesity_rate = '-'
    print('Obesity - adult prevalence rate: ' + obesity_rate)

    # Children under the age of 5 years underweight
    try:
        children_underweight = soup.find('div', {'id': 'field-children-under-the-age-of-5-years-underweight'}).find('span', class_='subfield-number').text
    except:
        children_underweight = '-'
    print('Children under the age of 5 years underweight: ' + children_underweight)

    # Education expenditures
    try:
        education_expenditures = soup.find('div', {'id': 'field-education-expenditures'}).find('span', class_='subfield-number').text
    except:
        education_expenditures = '-'
    print('Education expenditures: ' + education_expenditures)

    # Unemployment, youth ages 15-24
    try:
        unemployment_youth = soup.find('div', {'id': 'field-unemployment-youth-ages-15-24'}).find('span', class_='subfield-number').text
    except:
        unemployment_youth = '-'
    print('Unemployment, youth ages 15-24: ' + unemployment_youth)

    # Exchange Rate
    try:
        exchange_rate = soup.find('div', {'id': 'field-exchange-rates'}).find('span', class_='subfield-number').text
    except:
        exchange_rate = '-'
    print('Exchange Rate: ' + str(exchange_rate))

    # Currency
    try:
        currency = soup.find('div', {'id': 'field-exchange-rates'}).find('div', class_='category_data subfield text').text
    except:
        currency = '-'
    print('Currency: ' + str(currency))

    # GDP (purchasing power parity)
    try:
        gdp_ppp = soup.find('div', {'id': 'field-gdp-purchasing-power-parity'}).find('span', class_='subfield-number').text
    except:
        gdp_ppp = '-'
    print('GDP (purchasing power parity): ' + gdp_ppp)

    # GDP - real growth rate
    try:
        gdp_growth_rate = soup.find('div', {'id': 'field-gdp-real-growth-rate'}).find('span', class_='subfield-number').text
    except:
        gdp_growth_rate = '-'
    print('GDP - real growth rate: ' + gdp_growth_rate)

    # GDP - per capita (PPP)
    try:
        gdp_per_capita = soup.find('div', {'id': 'field-gdp-per-capita-ppp'}).find('span', class_='subfield-number').text
    except:
        gdp_per_capita = '-'
    print('GDP - per capita (PPP): ' + gdp_per_capita)

    # Gross national saving
    try:
        gross_saving = soup.find('div', {'id': 'field-gross-national-saving'}).find('span', class_='subfield-number').text
    except:
        gross_saving = '-'
    print('Gross national saving: ' + gross_saving)

    # Industrial production growth rate
    try:
        industrial_growth_rate = soup.find('div', {'id': 'field-industrial-production-growth-rate'}).find('span', class_='subfield-number').text
    except:
        industrial_growth_rate = '-'
    print('Industrial production growth rate: ' + industrial_growth_rate)
    
    # Labor Force
    try:
        labor_force = soup.find('div', {'id': 'field-labor-force'}).find('span', class_='subfield-number').text
    except:
        labor_force = '-'
    print('Labor force: ' + labor_force)

    # Unemployment rate
    try:
        unemployment_rate = soup.find('div', {'id': 'field-unemployment-rate'}).find('span', class_='subfield-number').text
    except:
        unemployment_rate = '-'
    print('Unemployment rate: ' + unemployment_rate)

    # Distribution of family income
    try:
        distribution_family_income = soup.find('div', {'id': 'field-distribution-of-family-income-gini-index'}).find('span', class_='subfield-number').text
    except:
        distribution_family_income = '-'
    print('Distribution of family income: ' + distribution_family_income)

    # Taxes and other revenues
    try:
        taxes_and_revenues = soup.find('div', {'id': 'field-taxes-and-other-revenues'}).find('span', class_='subfield-number').text
    except:
        taxes_and_revenues = '-'
    print('Taxes and other revenues: ' + taxes_and_revenues)

    # Budget surplus (+) or deficit (-)
    try:
        budget_surplus_deficit = soup.find('div', {'id': 'field-budget-surplus-or-deficit'}).find('span', class_='subfield-number').text
    except:
        budget_surplus_deficit = '-'
    print('Budget surplus (+) or deficit (-): ' + budget_surplus_deficit)

    # Public debt
    try:
        public_debt = soup.find('div', {'id': 'field-public-debt'}).find('span', class_='subfield-number').text
    except:
        public_debt = '-'
    print('Public debt: ' + public_debt)

    # Inflation rate
    try:
        inflation_rate = soup.find('div', {'id': 'field-inflation-rate-consumer-prices'}).find('span', class_='subfield-number').text
    except:
        inflation_rate = '-'
    print('Inflation rate: ' + inflation_rate)

    # Central bank discount rate 
    try:
        central_bank_rate = soup.find('div', {'id': 'field-central-bank-discount-rate'}).find('span', class_='subfield-number').text
    except:
        central_bank_rate = '-'
    print('Central bank discount rate : ' + central_bank_rate)

    # Commercial bank prime lending rate 
    try:
        commercial_bank_lending_rate = soup.find('div', {'id': 'field-commercial-bank-prime-lending-rate'}).find('span', class_='subfield-number').text
    except:
        commercial_bank_lending_rate = '-'
    print('Commercial bank prime lending rate : ' + commercial_bank_lending_rate)

    # Stock of narrow money 
    try:
        stock_narrow_money = soup.find('div', {'id': 'field-stock-of-narrow-money'}).find('span', class_='subfield-number').text
    except:
        stock_narrow_money = '-'
    print('Stock of narrow money : ' + stock_narrow_money)

    # Stock of broad money 
    try:
        stock_broad_money = soup.find('div', {'id': 'field-stock-of-broad-money'}).find('span', class_='subfield-number').text
    except:
        stock_broad_money = '-'
    print('Stock of broad money : ' + stock_broad_money)

    # Stock of domestic credit 
    try:
        stock_domestic_credit = soup.find('div', {'id': 'field-stock-of-domestic-credit'}).find('span', class_='subfield-number').text
    except:
        stock_domestic_credit = '-'
    print('Stock of domestic credit : ' + stock_domestic_credit)

    # Market value of publicly traded shares 
    try:
        market_value_shares = soup.find('div', {'id': 'field-market-value-of-publicly-traded-shares'}).find('span', class_='subfield-number').text
    except:
        market_value_shares = '-'
    print('Market value of publicly traded shares : ' + market_value_shares)

    # Current account balance 
    try:
        current_account_balance = soup.find('div', {'id': 'field-current-account-balance'}).find('span', class_='subfield-number').text
    except:
        current_account_balance = '-'
    print('Current account balance : ' + current_account_balance)

    # Exports
    try:
        exports = soup.find('div', {'id': 'field-exports'}).find('span', class_='subfield-number').text
    except:
        exports = '-'
    print('Exports: ' + exports)

    # Exports - partners
    try:
        exports_partners = soup.find('div', {'id': 'field-exports-partners'}).text
    except:
        exports_partners = '-'
    print('Exports - partners: ' + exports_partners)

    # Exports - commodities
    try:
        exports_commodities = soup.find('div', {'id': 'field-exports-commodities'}).text
    except:
        exports_commodities = '-'
    print('Exports - commodities: ' + exports_commodities)
    
    # Imports
    try:
        imports = soup.find('div', {'id': 'field-imports'}).find('span', class_='subfield-number').text
    except:
        imports = '-'
    print('Imports: ' + imports)

    # Imports - partners
    try:
        imports_partners = soup.find('div', {'id': 'field-imports-partners'}).text
    except:
        imports_partners = '-'
    print('Imports - partners: ' + imports_partners)

    # Imports - commodities
    try:
        imports_commodities = soup.find('div', {'id': 'field-imports-commodities'}).text
    except:
        imports_commodities = '-'
    print('Imports - commodities: ' + imports_commodities)

    # Reserves of foreign exchange and gold
    try:
        reserves_exchange_gold = soup.find('div', {'id': 'field-reserves-of-foreign-exchange-and-gold'}).find('span', class_='subfield-number').text
    except:
        reserves_exchange_gold = '-'
    print('Reserves of foreign exchange and gold: ' + reserves_exchange_gold)

    # External debt
    try:
        external_debt = soup.find('div', {'id': 'field-debt-external'}).find('span', class_='subfield-number').text
    except:
        external_debt = '-'
    print('External debt: ' + external_debt)

    # Stock of direct foreign investment - at home
    try:
        stock_investment_home = soup.find('div', {'id': 'field-stock-of-direct-foreign-investment-at-home'}).find('span', class_='subfield-number').text
    except:
        stock_investment_home = '-'
    print('Stock of direct foreign investment - at home: ' + stock_investment_home)

    # Stock of direct foreign investment - abroad
    try:
        stock_investment_abroad = soup.find('div', {'id': 'field-stock-of-direct-foreign-investment-abroad'}).find('span', class_='subfield-number').text
    except:
        stock_investment_abroad = '-'
    print('Stock of direct foreign investment - abroad: ' + stock_investment_abroad)

    # Military expenditures
    try:
        military_expenditures = soup.find('div', {'id': 'field-military-expenditures'}).find('span', class_='subfield-number').text
    except:
        military_expenditures = '-'
    print('Military expenditures: ' + military_expenditures)

    # Airports
    try:
        airports = soup.find('div', {'id': 'field-airports'}).find('span', class_='subfield-number').text
    except:
        airports = '-'
    print('Airports: ' + airports)

    # Railways
    try:
        railways = soup.find('div', {'id': 'field-railways'}).find('span', class_='subfield-number').text
    except:
        railways = '-'
    print('Railways: ' + railways)

    # Roadways
    try:
        roadways = soup.find('div', {'id': 'field-roadways'}).find('span', class_='subfield-number').text
    except:
        roadways = '-'
    print('Roadways: ' + roadways)

    # Waterways
    try:
        waterways = soup.find('div', {'id': 'field-waterways'}).find('span', class_='subfield-number').text
    except:
        waterways = '-'
    print('Waterways: ' + waterways)

    # Merchant marine
    try:
        merchant_marine = soup.find('div', {'id': 'field-merchant-marine'}).find('span', class_='subfield-number').text
    except:
        merchant_marine = '-'
    print('Merchant marine: ' + merchant_marine)

    # Electricity - production
    try:
        electricity_production = soup.find('div', {'id': 'field-electricity-production'}).find('span', class_='subfield-number').text
    except:
        electricity_production = '-'
    print('Electricity - production: ' + electricity_production)

    # Electricity - consumption
    try:
        electricity_consumption = soup.find('div', {'id': 'field-electricity-consumption'}).find('span', class_='subfield-number').text
    except:
        electricity_consumption = '-'
    print('Electricity - consumption: ' + electricity_consumption)

    # Electricity - exports
    try:
        electricity_exports = soup.find('div', {'id': 'field-electricity-exports'}).find('span', class_='subfield-number').text
    except:
        electricity_exports = '-'
    print('Electricity - exports: ' + electricity_exports)

    # Electricity - imports
    try:
        electricity_imports = soup.find('div', {'id': 'field-electricity-imports'}).find('span', class_='subfield-number').text
    except:
        electricity_imports = '-'
    print('Electricity - imports: ' + electricity_imports)

    # Electricity - installed generating capacity
    try:
        electricity_installed_capacity = soup.find('div', {'id': 'field-electricity-installed-generating-capacity'}).find('span', class_='subfield-number').text
    except:
        electricity_installed_capacity = '-'
    print('Electricity - installed generating capacity: ' + electricity_installed_capacity)

    # Electricity - from fossil fuels
    try:
        electricity_fossil_fuels = soup.find('div', {'id': 'field-electricity-from-fossil-fuels'}).find('span', class_='subfield-number').text
    except:
        electricity_fossil_fuels = '-'
    print('Electricity - from fossil fuels: ' + electricity_fossil_fuels)

    # Electricity - from nuclear fuels
    try:
        electricity_nuclear_fuels = soup.find('div', {'id': 'field-electricity-from-nuclear-fuels'}).find('span', class_='subfield-number').text
    except:
        electricity_nuclear_fuels = '-'
    print('Electricity - from nuclear fuels: ' + electricity_nuclear_fuels)

    # Electricity - from hydroelectric plants
    try:
        electricity_hydroelectric_plants = soup.find('div', {'id': 'field-electricity-from-hydroelectric-plants'}).find('span', class_='subfield-number').text
    except:
        electricity_hydroelectric_plants = '-'
    print('Electricity - from hydroelectric plants: ' + electricity_hydroelectric_plants)

    # Electricity - from other renewable sources
    try:
        electricity_other_sources = soup.find('div', {'id': 'field-electricity-from-other-renewable-sources'}).find('span', class_='subfield-number').text
    except:
        electricity_other_sources = '-'
    print('Electricity - from other renewable sources: ' + electricity_other_sources)

    # Crude oil - production
    try:
        crude_oil_production = soup.find('div', {'id': 'field-crude-oil-production'}).find('span', class_='subfield-number').text
    except:
        crude_oil_production = '-'
    print('Crude oil - production: ' + crude_oil_production)

    # Crude oil - exports
    try:
        crude_oil_exports = soup.find('div', {'id': 'field-crude-oil-exports'}).find('span', class_='subfield-number').text
    except:
        crude_oil_exports = '-'
    print('Crude oil - exports: ' + crude_oil_exports)

    # Crude oil - imports
    try:
        crude_oil_imports = soup.find('div', {'id': 'field-crude-oil-imports'}).find('span', class_='subfield-number').text
    except:
        crude_oil_imports = '-'
    print('Crude oil - imports: ' + crude_oil_imports)
    
    # Crude oil - proved reserves
    try:
        crude_oil_reserves = soup.find('div', {'id': 'field-crude-oil-proved-reserves'}).find('span', class_='subfield-number').text
    except:
        crude_oil_reserves = '-'
    print('Crude oil - proved reserves: ' + crude_oil_reserves)

    # Refined petroleum products - production
    try:
        petroleum_production = soup.find('div', {'id': 'field-refined-petroleum-products-production'}).find('span', class_='subfield-number').text
    except:
        petroleum_production = '-'
    print('Refined petroleum products - production: ' + petroleum_production)

    # Refined petroleum products - consumption
    try:
        petroleum_consumption = soup.find('div', {'id': 'field-refined-petroleum-products-consumption'}).find('span', class_='subfield-number').text
    except:
        petroleum_consumption = '-'
    print('Refined petroleum products - consumption: ' + petroleum_consumption)

    # Refined petroleum products - exports
    try:
        petroleum_exports = soup.find('div', {'id': 'field-refined-petroleum-products-exports'}).find('span', class_='subfield-number').text
    except:
        petroleum_exports = '-'
    print('Refined petroleum products - exports: ' + petroleum_exports)

    # Refined petroleum products - imports
    try:
        petroleum_imports = soup.find('div', {'id': 'field-refined-petroleum-products-imports'}).find('span', class_='subfield-number').text
    except:
        petroleum_imports = '-'
    print('Refined petroleum products - imports: ' + petroleum_imports)

    # Natural gas - production
    try:
        natural_gas_production = soup.find('div', {'id': 'field-natural-gas-production'}).find('span', class_='subfield-number').text
    except:
        natural_gas_production = '-'
    print('Natural gas - production: ' + natural_gas_production)

    # Natural gas - consumption
    try:
        natural_gas_consumption = soup.find('div', {'id': 'field-natural-gas-consumption'}).find('span', class_='subfield-number').text
    except:
        natural_gas_consumption = '-'
    print('Natural gas - consumption: ' + natural_gas_consumption)

    # Natural gas - exports
    try:
        natural_gas_exports = soup.find('div', {'id': 'field-natural-gas-exports'}).find('span', class_='subfield-number').text
    except:
        natural_gas_exports = '-'
    print('Natural gas - exports: ' + natural_gas_exports)

    # Natural gas - imports
    try:
        natural_gas_imports = soup.find('div', {'id': 'field-natural-gas-imports'}).find('span', class_='subfield-number').text
    except:
        natural_gas_imports = '-'
    print('Natural gas - imports: ' + natural_gas_imports)

    # Natural gas - proved reserves
    try:
        natural_gas_reserves = soup.find('div', {'id': 'field-natural-gas-proved-reserves'}).find('span', class_='subfield-number').text
    except:
        natural_gas_reserves = '-'
    print('Natural gas - proved reserves: ' + natural_gas_reserves)

    # Telephones - fixed lines
    try:
        telephones_fixed_lines = soup.find('div', {'id': 'field-telephones-fixed-lines'}).find('span', class_='subfield-number').text
    except:
        telephones_fixed_lines = '-'
    print('Telephones - fixed lines: ' + telephones_fixed_lines)

    # Telephones - mobile cellular
    try:
        telephones_mobile_cellular = soup.find('div', {'id': 'field-telephones-mobile-cellular'}).find('span', class_='subfield-number').text
    except:
        telephones_mobile_cellular = '-'
    print('Telephones - mobile cellular: ' + telephones_mobile_cellular)

    # Internet users
    try:
        internet_users = soup.find('div', {'id': 'field-internet-users'}).find('span', class_='subfield-number').text
    except:
        internet_users = '-'
    print('Internet users: ' + internet_users)
    
    data = {
        'Name': name,
        'Area': area,
        'Population': population,
        'Population growth rate': population_growth_rate,
        'Birth rate': birth_rate,
        'Death rate': death_rate,
        'Net migration rate': net_migration_rate,
        'Maternal mortality rate': maternal_mortality_rate,
        'Infant mortality rate': infant_mortality_rate,
        'Life expectancy at birth': life_expectancy,
        'Total fertility rate': total_fertility_rate,
        'Health expenditures': health_expenditures,
        'HIV/AIDS - adult prevalence rate': hiv_adult_prevalence,
        'HIV/AIDS - people living with HIV/AIDS': hiv_people_living,
        'HIV/AIDS - deaths': hiv_deaths,
        'Obesity - adult prevalence rate': obesity_rate,
        'Children under the age of 5 years underweight': children_underweight,
        'Education expenditures': education_expenditures,
        'Unemployment, youth ages 15-24': unemployment_youth,
        'Exchange Rate': exchange_rate,
        'Currency': currency,
        'GDP (purchasing power parity)': gdp_ppp,
        'GDP - real growth rate': gdp_growth_rate,
        'GDP - per capita (PPP)': gdp_per_capita,
        'Gross national saving': gross_saving,
        'Industrial production growth rate': industrial_growth_rate,
        'Labor Force': labor_force,
        'Unemployment rate': unemployment_rate,
        'Distribution of family income': distribution_family_income,
        'Taxes and other revenues': taxes_and_revenues,
        'Budget surplus (+) or deficit (-)': budget_surplus_deficit,
        'Public debt': public_debt,
        'Inflation rate (consumer prices)': inflation_rate,
        'Central bank discount rate': central_bank_rate,
        'Commercial bank prime lending rate': commercial_bank_lending_rate,
        'Stock of narrow money': stock_narrow_money,
        'Stock of broad money': stock_broad_money,
        'Stock of domestic credit': stock_domestic_credit,
        'Market value of publicly traded shares': market_value_shares,
        'Current account balance': current_account_balance,
        'Exports': exports,
        'Exports - partners': exports_partners,
        'Exports - commodities': exports_commodities,
        'Imports': imports,
        'Imports - partners': imports_partners,
        'Imports - commodities': imports_commodities,
        'Reserves of foreign exchange and gold': reserves_exchange_gold,
        'External debt': external_debt,
        'Stock of direct foreign investment - at home': stock_investment_home,
        'Stock of direct foreign investment - abroad': stock_investment_abroad,
        'Military expenditures': military_expenditures,
        'Airports': airports,
        'Railways': railways,
        'Roadways': roadways,
        'Waterways': waterways,
        'Merchant marine': merchant_marine,
        'Electricity - production': electricity_production,
        'Electricity - consumption': electricity_consumption,
        'Electricity - exports': electricity_exports,
        'Electricity - imports': electricity_imports,
        'Electricity - installed generating capacity': electricity_installed_capacity,
        'Electricity - from fossil fuels': electricity_fossil_fuels,
        'Electricity - from nuclear fuels': electricity_nuclear_fuels,
        'Electricity - from hydroelectric plants': electricity_hydroelectric_plants,
        'Electricity - from other renewable sources': electricity_other_sources,
        'Crude oil - production': crude_oil_production,
        'Crude oil - exports': crude_oil_exports,
        'Crude oil - imports': crude_oil_imports,
        'Crude oil - proved reserves': crude_oil_reserves,
        'Refined petroleum products - production': petroleum_production,
        'Refined petroleum products - consumption': petroleum_consumption,
        'Refined petroleum products - exports': petroleum_exports,
        'Refined petroleum products - imports': petroleum_imports,
        'Natural gas - production': natural_gas_production,
        'Natural gas - consumption': natural_gas_consumption,
        'Natural gas - exports': natural_gas_exports,
        'Natural gas - imports': natural_gas_imports,
        'Natural gas - proved reserves': natural_gas_reserves,
        'Telephones - fixed lines': telephones_fixed_lines,
        'Telephones - mobile cellular': telephones_mobile_cellular,
        'Internet users': internet_users
    }

    writer.writerow(data)

######################################################
######################################################

if __name__ == '__main__':
    # Define field names
    fieldnames = [
        'Name',
        'Area',
        'Population',
        'Population growth rate',
        'Birth rate',
        'Death rate',
        'Net migration rate',
        'Maternal mortality rate',
        'Infant mortality rate',
        'Life expectancy at birth',
        'Total fertility rate',
        'Health expenditures',
        'HIV/AIDS - adult prevalence rate',
        'HIV/AIDS - people living with HIV/AIDS',
        'HIV/AIDS - deaths',
        'Obesity - adult prevalence rate',
        'Children under the age of 5 years underweight',
        'Education expenditures',
        'Unemployment, youth ages 15-24',
        'Exchange Rate',
        'Currency',
        'GDP (purchasing power parity)',
        'GDP - real growth rate',
        'GDP - per capita (PPP)',
        'Gross national saving',
        'Industrial production growth rate',
        'Labor Force',
        'Unemployment rate',
        'Distribution of family income',
        'Taxes and other revenues',
        'Budget surplus (+) or deficit (-)',
        'Public debt',
        'Inflation rate (consumer prices)',
        'Central bank discount rate',
        'Commercial bank prime lending rate',
        'Stock of narrow money',
        'Stock of broad money',
        'Stock of domestic credit',
        'Market value of publicly traded shares',
        'Current account balance',
        'Exports',
        'Exports - partners',
        'Exports - commodities',
        'Imports',
        'Imports - partners',
        'Imports - commodities',
        'Reserves of foreign exchange and gold',
        'External debt',
        'Stock of direct foreign investment - at home',
        'Stock of direct foreign investment - abroad',
        'Military expenditures',
        'Airports',
        'Railways',
        'Roadways',
        'Waterways',
        'Merchant marine',
        'Electricity - production',
        'Electricity - consumption',
        'Electricity - exports',
        'Electricity - imports',
        'Electricity - installed generating capacity',
        'Electricity - from fossil fuels',
        'Electricity - from nuclear fuels',
        'Electricity - from hydroelectric plants',
        'Electricity - from other renewable sources',
        'Crude oil - production',
        'Crude oil - exports',
        'Crude oil - imports',
        'Crude oil - proved reserves',
        'Refined petroleum products - production',
        'Refined petroleum products - consumption',
        'Refined petroleum products - exports',
        'Refined petroleum products - imports',
        'Natural gas - production',
        'Natural gas - consumption',
        'Natural gas - exports',
        'Natural gas - imports',
        'Natural gas - proved reserves',
        'Telephones - fixed lines',
        'Telephones - mobile cellular',
        'Internet users'
    ]

    with open(output_filename , 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i, filename in enumerate(os.listdir(input_directory)):
            if filename.endswith('.json'):
                print('======================= ' + str(i+1))
                print('Read JSON file: ' + filename)
                print('-----------------------')

                with open(input_directory + '\\' + filename, 'r', encoding='utf8') as json_file:
                    data = json.load(json_file, strict=False)
                    html_data = data['html'].replace('\\', '')
                    soup = BeautifulSoup(html_data, 'html.parser')
                    try:
                        main(data)  # Call main function
                        print('Data saved successfully')
                    except Exception as err:
                        print('Failed to save')
                        print('Error: ' + str(err))
                        
        print('=======================')
        print('All data saved successfully')

    #############################################################################

    # # FOR TESTING

    # with open(output_filename , 'w', newline='') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()

    #     with open(os.getcwd() + '\\json\\id.json', 'r', encoding='utf8') as json_file:
    #         data = json.load(json_file, strict=False)
    #         html_data = data['html'].replace('\\', '')
    #         soup = BeautifulSoup(html_data, 'html.parser')
    #         try:
    #             main(data)  # Call main function
    #             print('Data saved successfully')
    #         except Exception as err:
    #             print('Failed to save')
    #             print('Error: ' + str(err))
    
        



