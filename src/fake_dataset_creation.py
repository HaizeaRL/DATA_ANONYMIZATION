import pandas as pd
from faker import Faker
import random
import os

# Initialize Faker
fake = Faker()
num_students = 35125  # Simulate number of students in dataset

# Simulate school date
schools = [
    {'name': 'School A', 'address': 'Street A 123', 'zip_code': '12345'},
    {'name': 'School B', 'address': 'Street B 456', 'zip_code': '23456'},
    {'name': 'School C', 'address': 'Street C 789', 'zip_code': '34567'},
    {'name': 'School D', 'address': 'Street D 101', 'zip_code': '45678'},
    {'name': 'School E', 'address': 'Street E 202', 'zip_code': '56789'},
    {'name': 'School F', 'address': 'Street F 123', 'zip_code': '12456'},
    {'name': 'School G', 'address': 'Street G 456', 'zip_code': '12654'},
    {'name': 'School H', 'address': 'Street H 789', 'zip_code': '67890'},
    {'name': 'School I', 'address': 'Street I 101', 'zip_code': '23654'},
    {'name': 'School J', 'address': 'Street J 202', 'zip_code': '56789'},
    {'name': 'School K', 'address': 'Street K 789', 'zip_code': '34667'},
    {'name': 'School L', 'address': 'Street L 101', 'zip_code': '45789'},
    {'name': 'School M', 'address': 'Street M 202', 'zip_code': '56779'}
]

# simulate salary ranges per occupancy
salary_ranges = {
    'Engineer': (5000, 20000),
    'Teacher': (3000, 12000),
    'Doctor': (15000, 50000),
    'Lawyer': (10000, 35000),
    'Nurse': (4000, 14000),
    'Unemployed': (300, 1568)
}

# Complete data with simulate values
data = []

for _ in range(num_students):
    school = random.choice(schools)
    occupation = random.choice(['Engineer', 'Teacher', 'Doctor', 'Lawyer', 'Nurse', 'Unemployed'])
    student = {
        'First_Name': fake.first_name(),
        'Last_Name': fake.last_name(),
        'Age': random.randint(0, 26),
        'School_Name': school['name'],
        'School_Address': school['address'],
        'School_ZipCode': school['zip_code'],         
        'Parents_Salary': round(random.uniform(*salary_ranges[occupation]), 3),
        'Parents_Occupation': occupation,
        'Weight': round(random.uniform(20, 80), 1),
        'Size': round(random.uniform(100, 200), 1),
        'Feet_size': random.choice([34, 35, 36, 37, 38, 39, 40, 41, 42]),
        'Eye_color': random.choice(['Blue', 'Green', 'Brown']),
        'Hair_color': random.choice(['Blonde', 'Brown', 'Black', 'Red']),
        'Previous_year_grades': round(random.uniform(2, 10), 1),
        'Current_year_grades': round(random.uniform(2, 10), 1),
    }
    data.append(student)

# Create dataframe and save file
df = pd.DataFrame(data)
df.to_csv('./students_data.csv', index=False, encoding='utf-8')

print("Dataset 'students_data.csv' created and saved.")