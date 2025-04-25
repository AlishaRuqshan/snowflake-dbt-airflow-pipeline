🚀 End-to-End Cloud Data Pipeline Project (Snowflake + dbt + Apache Airflow)

**📌 Project Overview**
- 	🔐 **Created a secure environment in Snowflake:**
	 - •Set up a dedicated database (dbt_db) and schema (dbt_schema)
	 - •Created a custom role (dbt_role) and granted it permission to create tables, views, stages, and formats
	 - •Assigned the role to your Snowflake user.
- 🛠️** Built a DBT project locally:**
	 - •Initialized a new DBT project (data_pipeline)
  - •Configured profiles.yml with your Snowflake connection details (user, password, warehouse, schema)
	 - •Defined staging and mart models using SQL files and config() blocks
	 - •Wrote reusable macros for transformations.
- ⚙️ **Set up Airflow locally using Astro CLI:**
	 - •Ran astro dev init to scaffold the Airflow project
	 - •Wrote a DAG (dbt_dag.py) that uses BashOperator to trigger dbt run and dbt test
	 - •Mounted the DBT project folder into the dags/ directory of the Astro environment
	 - •Added the profiles.yml inside a hidden .dbt folder so Airflow could access it.
- **🔁 Ran and orchestrated everything locally:**
	 - •Triggered the Airflow DAG manually via the UI
	 - •Verified task status in the Graph view
	 - •Checked logs to confirm DBT transformations executed successfully
	 - •Models appeared in Snowflake as expected (with correct materializations: table, view)
 
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



**📈 What You'll See Working**

Airflow UI running locally at localhost:8080
dbt models successfully building tables and views in Snowflake
A clean, Git-tracked project you can share or extend


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
