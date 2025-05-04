from typing import List, Tuple
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from datetime import datetime, date


async def fetch_page(session: ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()


async def get_report_links(page_html: str) -> List[Tuple[str, date]]:
    soup = BeautifulSoup(page_html, "html.parser")
    report_links = []
    dates = []
    for item in soup.select(".accordeon-inner__wrap-item"):
        link = item.select_one(".accordeon-inner__item-title.link.xls")
        if link:
            report_links.append("https://spimex.com" + link.get("href"))
        date_elem = item.select_one(".accordeon-inner__item-inner__title span")
        if date_elem:
            date_str = date_elem.text.strip()
            dates.append(datetime.strptime(date_str, "%d.%m.%Y").date())
    return list(zip(report_links, dates))
