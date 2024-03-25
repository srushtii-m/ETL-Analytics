# Supply Chain Data Engineering End-to-End Project

## Objective

In this project, I developed a complete data pipeline, guiding data from collection to insights through a series of structured stages.       
1. Extracted data, cleaned it and loaded into Google Cloud Storage for further processing.
2. Transformed and modeled the data using fact and dimensional data modeling concepts using Python.
3. Using ETL concept, orchestrated the data pipeline on Mage AI and loaded the transformed data into Google BigQuery.
4. Developed a dashboard on Looker Studio.

## Dataset Used

I'm using the dataset from [DataCo Global](https://data.mendeley.com/datasets/8gx2fvg2k6/5). The data description is [here](data\Data Dictionary.pdf). It consists of 52 features in areas of provisioning, production, sales, and commercial distribution.

## Technologies:

* Language: Python, SQL
* Extraction and transformation: Jupyter Notebook, Google BigQuery
* Storage: Google Cloud Storage
* Orchestration: [Mage AI](https://www.mage.ai/)
* Dashboard: Looker Studio

## Data Pipeline Architecture

![Architecture](https://github.com/srushtii-m/ETL-Analytics/blob/main/images/etl%20pipeline.png)

Step 1: Cleaning and transformation - sc_data.ipynb
Step 2: Storage
Step 3: ETL, Orchestration - Mage: Extract, Transform, Load
Step 4: Analytics - SQL script
Step 5: Dashboard

## Data Modeling
The datasets are designed using the principles of fact and dim data modeling concepts.         
![Modeling](https://github.com/srushtii-m/ETL-Analytics/blob/main/images/sc_datamodel.png)

### Step 1: Cleaning and Transformation
In this step, I loaded the CSV file into VSCode and carried out data cleaning and transformation activities prior to organizing them into fact and dim tables.[script](data_cleaning.ipynb)

### Step 2: Stored the data on Google Cloud Storage

### Step 3: ETL
1. Launched the SSH instance and installed required libraries and Mage AI library.
2. ETL is carried out by accessing the external IP address and mage-ai port number.
3. Created a new pipeline with the following stages:
    * [Extract](Mage\scm_dataloader.py)
    * [Transform](Mage\scm_transformation.py)
    * [Load](Mage\scm_bigquery.py)

### Step 4: Analytics
After running the pipeline in Mage, the fact and dimensional tables were generated in Google Big Query. Performed few queries and crearted sales analytics table. [SQL queries here.](queries.sql)

### Step 5: Dashboard
After completing the analysis, I loaded the relevant tables into Looker Studio and created a dashboard. [Dashboard here.](https://lookerstudio.google.com/s/qMZDCm_iIgA)
![dashboard](https://github.com/srushtii-m/ETL-Analytics/blob/main/images/sales_dashboard.png)
