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
]

# Complete data with simulate values
data = []

for _ in range(num_students):
    school = random.choice(schools)
    student = {
        'First_Name': fake.first_name(),
        'Last_Name': fake.last_name(),
        'Age': random.randint(6, 18),
        'School': school['name'],
        'School_Address': school['address'],
        'School_zip_code': school['zip_code'],
        'Parents_salary': random.randint(1150, 100000),
        'Parents_occupation': random.choice(['Engineer', 'Teacher', 'Doctor', 'Lawyer', 'Nurse', 'Unemployed']),
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