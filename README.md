# DATA-ANONYMIZATION

- **Author**: Haizea Rumayor Lazkano
- **Last update**: August 2024

------------------------------------------------------------------------

## Introduction

Data anonymization is essential in a data-driven world. As more personal information is collected and stored, the risk of exposing sensitive data increases. Anonymization reduces these risks by making it impossible to identify individuals from the data, protecting their privacy and meeting legal requirements.

Anonymizing data not only safeguards privacy but also ensures the secure handling of sensitive information. It helps prevent data breaches, misuse, and unauthorized access, allowing for safe analysis and sharing without compromising personal details.

## Overview

This GitHub project demonstrates a case study originally developed in 2016 but uploaded this year. The case involves collaboration between two organizations: one collects personal and academic data from students, while the other uses this data to analyze whether a new product improves academic performance.

To comply with data protection laws, the collected data—which includes both direct identifiers (such as names, eye colors, etc.) and indirect identifiers (like parents' employment status, salary information, and grades)—will be anonymized. By anonymizing data, organizations ensure that individual identities remain confidential and that sensitive information is handled securely, in line with legal standards for data protection.

## Project Structure

The project includes a Python script named `fake_dataset_creation.py` that generates a fake dataset with sensitive data, saved as `students_data.csv`, simulating the type of information the first organization would collect.

Additionally, a Jupyter Notebook named `anonymization.ipynb` is provided, which justifies and applies the necessary anonymization techniques to the dataset.

## Installation

To set up the project environment, you need to install the required Python packages. The necessary packages are listed in the `requirements.txt` file. You can install them using the following command:

```bash
pip install -r requirements.txt
