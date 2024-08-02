# WorldQuant-University-Projects

A repository containing all the projects that were carried out during my Applied Data Science course learning at WorldQuant University.

# The Project

Predicting House Prices in Mexico

# Predicting House Prices in Brazil

In this assignment, you'll work with a dataset of homes for sale in Brazil. Your goal is to determine if there are regional differences in the real estate market.
Also, you will look at southern Brazil to see if there is a relationship between home size and price, similar to what you saw with housing in some states in Mexico.

# Predicting Apartment Prices in Mexico City

This was similar to the first project but we had to create a wrangle function that could do the following:

1- Subset the data in the CSV file and return only apartments in Mexico City ("Distrito Federal") that cost less than $100,000.
2- Remove outliers by trimming the bottom and top 10% of properties in terms of "surface_covered_in_m2".
3- Create separate "lat" and "lon" columns.
4- Mexico City is divided into 16 boroughs. Create a "borough" feature from the "place_with_parent_names" column.
5- Drop columns that are more than 50% null values.
6- Drop columns containing low- or high-cardinality categorical values.
7- Drop any columns that would constitute leakage for the target "price_aprox_usd".
8- Drop any columns that would create issues of multicollinearity.

# Algorithms

1- Linear Regression
2- Logistic Regression
