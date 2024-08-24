**Simple ETL Pipeline Using Apache Airflow**

**Overview**

This project demonstrates a basic ETL (Extract, Transform, Load) pipeline using Apache Airflow. The pipeline reads data from a CSV file, performs basic transformations, and writes the transformed data to a new CSV file. This project is ideal for beginners who want to learn the basics of Apache Airflow and understand how to orchestrate ETL workflows.

**Features**

-Data Extraction: Reads data from an input CSV file.

-Data Transformation: Performs basic data filtering and aggregation.

-Data Loading: Writes the transformed data to a new CSV file.

-Automated Workflow: Utilizes Apache Airflow to automate the ETL process.

**Project Structure**

simple_airflow_etl/

├── dags/

│   └── simple_etl_dag.py       # Airflow DAG definition file

├── data/

│   ├── input_data.csv           # Input data file

│   ├── extracted_data.csv       # Extracted data (intermediate)

│   ├── transformed_data.csv     # Transformed data (intermediate)

│   └── output_data.csv          # Output data file

├── scripts/

│   ├── extract.py               # Script to extract data

│   ├── transform.py             # Script to transform data

│   └── load.py                  # Script to load data

└── README.md                    # Project README file


**Prerequisites**

-Python 3.7+ installed on your system.

-Required Python packages: pandas, apache-airflow.

**Installation**

Clone the Repository:

-git clone url

Set Up a Virtual Environment:

-python -m venv airflow_env

-.\airflow_env\Scripts\activate

Install Apache Airflow:

-pip install apache-airflow

Initialize the Airflow Database:

-airflow db init

**Usage**

Prepare the Input Data:

Add your input data to the data/input_data.csv file.

Run the Airflow Scheduler:

-airflow scheduler

Run the Airflow Web Server:

Open another terminal and run:

-airflow webserver

Access the Airflow UI:

Open your web browser and go to http://localhost:8080. You should see the simple_etl_dag listed in the DAGs.

Trigger the DAG:

Enable the DAG by toggling it on.

Manually trigger the DAG to run the ETL process.

Check the Output:

After running the DAG, check the data/output_data.csv file to see the transformed data.

**Customization**

Input Data: Modify the input_data.csv file with your own data.

Transformation Logic: Customize the transform.py script to perform different transformations as needed.

Schedule Interval: Adjust the schedule_interval in the DAG to control how often the ETL pipeline runs.

**Learning Objectives**

Understand the basics of Apache Airflow, including DAGs, tasks, and operators.

Learn how to orchestrate an ETL pipeline using Python and Airflow.

Gain hands-on experience with task scheduling and workflow automation.
