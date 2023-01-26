# USCG Boat Recall Data - Web Scraper
Michael Nolan, 2023.01.25

## Introduction
The U.S. Coast Guard makes boat recall data going back to the early 1980's publicly available here: https://uscgboating.org/content/recalls.php.
This was brought to my attention by the great newsletter [data-is-plural](https://www.data-is-plural.com/) which shares a weekly list of fun publicly available datasets for you to poke at and plot out.
Unfortunately, this boat recall dataset isn't readily downloadable as a table file. I quickly wrote this web scraper to collect that data into a single CSV file.

## Dependencies
- `numpy`
- `pandas`
- `tqdm`

## Contents
- `scrape_uscg_boat_recall_data.py` is a python script that scrapes the recalls website. Use this to generate the data table and extended data table.
- `uscg_boat_recalls.csv` is a CSV table file containing information about individual boat recalls in the U.S.
    - Fields:
        - Number: alphanumeric ID for each recall
        - MIC: Manufacturer's ID Code
        - Company Name: the company name associated with the recall. There's some slop here - 'YAMAHA MOTOR CORP USA', 'YAMAHA CORP USA' and 'YAMAHA MOTOR CORP' all exist as separate IDs in the table.
        - Model Name: the model of the boat or watercraft being recalled.
        - Problem 1: reason for the recall
        - Last Date: recall date. NOTE: ~100 or so recall entries have a value of `1970-01-01` that appears to be the default when a date is not given. There's a large discontinuity between that date and the next which is in early 1980.
- `uscg_boat_recalls_ext.csv` is a csv table file containing extended information about individual boat recalls in the U.S. Contains more data than `uscg_boat_recalls.csv`
    - Fields:
        - Number: alphanumeric ID for each recall
        - MIC: Manufacturer's ID Code
        - Company Name: the company name associated with the recall. There's some slop here - 'YAMAHA MOTOR CORP USA', 'YAMAHA CORP USA' and 'YAMAHA MOTOR CORP' all exist as separate IDs in the table.
        - Model Name: the model of the boat or watercraft being recalled.
        - Problem 1: reason for the recall
        - Problem 2: optional 2nd reason for recall
        - Last Date: recall date. NOTE: ~100 or so recall entries have a value of `1970-01-01` that appears to be the default when a date is not given. There's a large discontinuity between that date and the next which is in early 1980.
        - Boat Type: numeric values, I assume this is a length measurement
        - Campaign Open Date: start date of recall campaign
        - Campaign Close Date: end date of recall campaign
        - Case Open Date: start date of recall case
        - Case Close Date: end data of recall case
        - Company: company name
        - Company Official: alphanumeric code associated with company
        - Disposition: 'Open' or 'Closed', indicates recall status. Note: messy inputs, 'Closed' and 'closed', etc. Needs further cleaning.
        - HIN: Hull Identification Number
        - Model Year: watercraft model year or years affected
        - Severity: values are 'L', 'M', 'H', 'S' and '1'. Note: I assume this is low, med, high. Not sure about S or 1. Inputs messy, e.g. both 'h' and 'H' in table. Needs further cleaning.
        - Units: number of watercraft affected