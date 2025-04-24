🚀 End-to-End Cloud Data Pipeline Project (Snowflake + dbt + Apache Airflow)

**📌 Project Overview**
 . Hey there! This project walks you through how to build a cloud-based data pipeline using:

 . Snowflake – a super scalable, cloud-native data warehouse

 . dbt (Data Build Tool) – lets you transform data using SQL like a pro, all while treating it like code

 . Apache Airflow (via Astro CLI) – to orchestrate and schedule everything, container-style

**Goal**: Seamlessly ingest, transform, and orchestrate structured data using modern, cloud-friendly tools in a containerized setup you can spin up anywhere.

**💡 Why This Project Matters**

 . Old-school ETL pipelines can be clunky — think hard-to-maintain scripts, mystery logic, and “who broke this?” moments.

** .dbt flips the script by:**

 . Making your SQL modular, version-controlled, and testable

 . Boosting transparency with data lineage and documentation

 . Letting data teams collaborate like software engineers

 . Pair that with Snowflake’s muscle and Airflow’s scheduling chops, and you’ve got a modern setup that actually scales.

**Why It’s Valuable for Data Analysts**

 . As a data analyst, being able to trust and understand your data is everything. This project:

 . Helps you trace how raw data becomes analysis-ready

 . Gives you visibility into transformations

 . Empowers self-service access through clean, documented models

****Why It’s Important for Me as a Data Engineer**
As the Data Engineer on this project, I:

 . Designed the ELT architecture from scratch using best practices

 . Wrote SQL-based models with dbt, using macros for flexibility

 . Built a reusable, containerized environment with Astro CLI + Docker

 . Automated all steps with Airflow and managed configs with profiles.yml

 . Integrated version control with Git and structured the project for teamwork

**🧱 Project Folder Breakdown**

dbt-dag/

├── dags/

│   ├── data_pipeline/       # Your dbt project: models, macros, seeds, snapshots

│   └── .dbt/profiles.yml    # Snowflake profile – safely mounted inside container

├── plugins/                 # Airflow plugins if needed

├── Dockerfile               # Astro Runtime image (comes with dbt)

├── requirements.txt         # Extra Python packages

├── airflow_settings.yaml    # Airflow config: DAGs, connections, variables

└── README.md

**✅ What We Built**

Modular staging, intermediate, and fact models using dbt

Smart macros to reuse logic and clean up transformations

An Airflow DAG using BashOperator to kick off dbt runs

A Dockerized local environment using Astro CLI

Safely stored Snowflake credentials via .dbt/profiles.yml

**📈 What You'll See Working**

Airflow UI running locally at localhost:8080

dbt models successfully building tables and views in Snowflake

A clean, Git-tracked project you can share or extend

**💬 Where You Can Take This**

Add dbt tests to validate assumptions

Auto-generate docs using dbt docs generate

Expand your DAGs to support upstream/downstream workflows

Deploy to managed Airflow like Astronomer Cloud

Built with 💻 by Alisha Ruqshan Kadiri



**🛠️ Getting Started Locally**

If you want to run this project on your machine:

🔁 Prerequisites:

Install Docker

Install Astro CLI

Clone this repo:

git clone https://github.com/AlishaRuqshan/snowflake-dbt-airflow-pipeline.git
cd snowflake-dbt-airflow-pipeline

🚀 Start the local environment:

astro dev start --wait 3m

🌐 Access Airflow:

Visit http://localhost:8080 and run the DAG named run_dbt_pipeline

🧪 Add your own Snowflake credentials inside dags/.dbt/profiles.yml

Or use env_var() style secrets with astro dev secrets set
