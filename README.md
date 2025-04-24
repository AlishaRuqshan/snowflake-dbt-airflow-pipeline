🚀 End-to-End Cloud Data Pipeline Project (Snowflake + dbt + Apache Airflow)

📌 Project Overview
Hey there! This project walks you through how to build a cloud-based data pipeline using:

Snowflake – a super scalable, cloud-native data warehouse

dbt (Data Build Tool) – lets you transform data using SQL like a pro, all while treating it like code

Apache Airflow (via Astro CLI) – to orchestrate and schedule everything, container-style

Goal: Seamlessly ingest, transform, and orchestrate structured data using modern, cloud-friendly tools in a containerized setup you can spin up anywhere.

💡 Why This Project Matters

Old-school ETL pipelines can be clunky — think hard-to-maintain scripts, mystery logic, and “who broke this?” moments.

dbt flips the script by:

Making your SQL modular, version-controlled, and testable

Boosting transparency with data lineage and documentation

Letting data teams collaborate like software engineers

Pair that with Snowflake’s muscle and Airflow’s scheduling chops, and you’ve got a modern setup that actually scales.

🔧 What You'll Get Out of This

Build end-to-end ELT pipelines using dbt + Snowflake

Write clean, reusable SQL models and macros

Trigger and monitor dbt runs inside Apache Airflow

Manage your config with profiles.yml and support multiple environments

Organize your repo like a pro and track it all with Git

🧱 Project Folder Breakdown

dbt-dag/
├── dags/
│   ├── data_pipeline/       # Your dbt project: models, macros, seeds, snapshots
│   └── .dbt/profiles.yml    # Snowflake profile – safely mounted inside container
├── plugins/                 # Airflow plugins if needed
├── Dockerfile               # Astro Runtime image (comes with dbt)
├── requirements.txt         # Extra Python packages
├── airflow_settings.yaml    # Airflow config: DAGs, connections, variables
└── README.md

✅ What We Built

Modular staging, intermediate, and fact models using dbt

Smart macros to reuse logic and clean up transformations

An Airflow DAG using BashOperator to kick off dbt runs

A Dockerized local environment using Astro CLI

Safely stored Snowflake credentials via .dbt/profiles.yml

📈 What You'll See Working

Airflow UI running locally at localhost:8080

dbt models successfully building tables and views in Snowflake

A clean, Git-tracked project you can share or extend

💬 Where You Can Take This

Add dbt tests to validate assumptions

Auto-generate docs using dbt docs generate

Expand your DAGs to support upstream/downstream workflows

Deploy to managed Airflow like Astronomer Cloud

Built with 💻 by Alisha Ruqshan Kadiri
