# Job Market Data Pipeline

**Project Goal:** I built this project to practice real data engineering skills. It shows how I can build a full data system from start to finish using tools like Python, Pandas, SQL, and Apache Airflow.

## How the Project Works

The project is broken down into four main parts:

### Phase 1: Getting the Data
The script pulls live job posts from the Adzuna API. It uses async Python to get many pages at once so it runs very fast.
- **Tools:** aiohttp, asyncio

### Phase 2: Cleaning the Data
We load the raw data into Pandas. The code removes double job posts and checks the text to find required skills (like Python, SQL, or AWS).
- **Tools:** pandas, numpy, re (Regex)

### Phase 3: Database Storage
We move the clean data into a PostgreSQL database. The data is sorted into clear tables (Star Schema) so we can ask questions like, "What are the top 5 skills for Data Engineers right now?"
- **Tools:** sqlalchemy, PostgreSQL

### Phase 4: Cloud and Automation
The goal is to make the project run on its own. We save the data files to the cloud (AWS S3) and use Apache Airflow to run the script every night at 2:00 AM.
- **Tools:** boto3, Apache Airflow, AWS S3

## How to Run It

1. Make a file named .env in the main folder.
2. Add your Adzuna API keys inside the .env file:
   app_id=YOUR_APP_ID
   app_key=YOUR_APP_KEY

3. Install the required tools:
   pip install -r requirements.txt

4. Run the main script:
   python run_pipeline.py --role "Data Engineer" --country "us" --pages 5

## Project Folders

* data/ - Holds the raw and clean data files (hidden from GitHub).
* pipeline/ - Holds the main Python code.
* .env - Keeps API keys safe.