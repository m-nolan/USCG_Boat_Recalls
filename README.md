# USCG Boat Recall Data - Web Scraper
Michael Nolan, 2023.01.25

## Introduction
The U.S. Coast Guard makes boat recall data going back to the early 1980's publicly available here: https://uscgboating.org/content/recalls.php.
This was brought to my attention by the great newsletter [data-is-plural](https://www.data-is-plural.com/) which shares a weekly list of fun publicly available datasets for you to poke at and plot out.
Unfortunately, this boat recall dataset isn't readily downloadable as a table file. I quickly wrote this web scraper to collect that data into a single CSV file.

## Contents
- `scrape_uscg_boat_recall_data.ipnb` is a notebook of python code that scrapes the recalls website.
- `uscg_boat_recalls.csv` is a CSV table file containing information about individual boat recalls in the U.S.
    - Fields:
        - Number: alphanumeric ID for each recall
        - MIC:
        - Company Name: the company name associated with the recall. There's some slop here - 'YAMAHA MOTOR CORP USA', 'YAMAHA CORP USA' and 'YAMAHA MOTOR CORP' all exist as separate IDs in the table.
        - Model Name: the model of the boat or watercraft being recalled.
        - Problem 1: reason for the recall
        - Last Date: recall date. NOTE: ~100 or so recall entries have a value of `1970-01-01` that appears to be the default when a date is not given. There's a large discontinuity between that date and the next which is in early 1980.