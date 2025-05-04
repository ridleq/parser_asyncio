import os
from aiohttp import ClientSession
from datetime import date


async def download_file(
    session: ClientSession, url: str,
    report_date: date, folder: str = "downloads"
) -> None:
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/{report_date}.xls"
    async with session.get(url) as response:
        if response.status == 200:
            content = await response.read()
            with open(filename, "wb") as f:
                f.write(content)
            print(f"Successfully downloaded {filename}")
        else:
            print(f"Failed to download {url}: HTTP {response.status}")
