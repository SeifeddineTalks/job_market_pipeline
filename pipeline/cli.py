from pipeline.extract import main
import asyncio
import argparse


job_parser=argparse.ArgumentParser(description="Fetch live job postings from Adzuna")

job_parser.add_argument("--country", required=True, help="where are you looking for the job", type=str)
job_parser.add_argument("--pages", required=True, help="how many pages to fetch", type=int)
job_parser.add_argument("--role", required=True, help="what job role to fetch", type=str)

args = job_parser.parse_args()

print(f"Searching for {args.role} jobs in {args.country} for {args.pages} pages...")

asyncio.run(main(args.role, args.country, args.pages))

