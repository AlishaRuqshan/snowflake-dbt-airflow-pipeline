FROM astrocrpublic.azurecr.io/runtime:3.0-1

# Install dbt-core and dbt-snowflake globally into the Astro container
RUN pip install dbt-core dbt-snowflake