import aiohttp
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("app_id")
APP_KEY = os.getenv("app_key")
print(f"My ID is: {APP_ID}")
print(f"My Key is: {APP_KEY}")




async def fetch_jobs(session, app_id, app_key, role:str, country:str, page:int):
    url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}?app_id={app_id}&app_key={app_key}&what={role}"

    async with session.get(url) as response:
        data = await response.json()
        return data

async def main(role: str, country: str, pages: int):
    async with aiohttp.ClientSession() as session:
        tasks= []
        for page_num in range(1, pages+1):
            task = asyncio.create_task(fetch_jobs(session, APP_ID, APP_KEY, role, country, page_num))
            tasks.append(task)
            await asyncio.sleep(0.5)
        results = await asyncio.gather(*tasks)
        print(f"downloaded {len(results)} pages!")
        print(results[0])
        return results

#python -m pipeline.cli --role "data engineer" --country "at" --pages 3
    
        
    

    


