import asyncio
import requests
import aiohttp 

response = requests.get('https://jsonplaceholder.typicode.com/photos')
with open('git.json','w') as file:
    file.write(response.text)


async def download_json(url, session):
    async with session.get(url) as response:
        with open("data_json",'w') as file:
            file.write(await response.text())


async def main():
    urls = ["https://jsonplaceholder.typicode.com/photos"]
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(download_json(url, session)) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())  



