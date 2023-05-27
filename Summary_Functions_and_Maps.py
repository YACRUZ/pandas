import pandas as pd

##Ejercicio 1
print("===== Question 1 =====")
# What is the median of the points column in the reviews DataFrame?
median_points = reviews.points.median()
print(median_points)



##Ejercicio 2
print("===== Question 2 =====")
#hat countries are represented in the dataset? (Your answer should not include any duplicates.)
countries = reviews.country.unique()
print(countries)



##Ejercicio 3
print("===== Question 3 =====")
#How often does each country appear in the dataset?
reviews_per_country = reviews.country.value_counts()
print(reviews_per_country)



##Ejercicio 4
print("===== Question 4 =====")
#



##Ejercicio 5
print("===== Question 5 =====")
#



##Ejercicio 6
print("===== Question 6 =====")
#



##Ejercicio 7
print("===== Question 7 =====")
#



