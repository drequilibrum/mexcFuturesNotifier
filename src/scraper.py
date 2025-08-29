from bs4 import BeautifulSoup
from urllib.request import urlopen
from typing import Union as U
from .config import SCRAPE_URL
from datetime import datetime


def scrape_announcements(url: str) -> list[str]:
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    announcements = []

    for announcement in soup.find_all(
        "li", class_="article-list_articleListItem-community__AgU6l"
    ):
        if "[Initial Futures Listing]" in announcement.text:
            announcements.append(announcement.text.strip())

    return announcements


def extract_coin_ticker(announcement: str) -> U[str, None]:
    start = announcement.find("(") + 1
    end = announcement.find(")", start)
    if start > 0 and end > start:
        return announcement[start:end]
    return None


def reformat_datetime(datetime_str: str) -> U[str, None]:
    try:
        datetime_obj = datetime.strptime(datetime_str, "%b %d, %Y, %H:%M (UTC)")
        return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None


def extract_listing_datetime(announcement: str) -> U[str, None]:
    try:
        parts = announcement.split(" to List on ")
        if len(parts) > 1:
            datetime_part = parts[1]
            return reformat_datetime(datetime_part.strip())
    except IndexError:
        return None
    return None


def get_latest_listing():
    announcements = scrape_announcements(SCRAPE_URL)
    latest_announcement = announcements[0] if len(announcements) > 0 else None
    if not latest_announcement:
        return None
    ticker = extract_coin_ticker(latest_announcement)
    listing_datetime = extract_listing_datetime(latest_announcement)
    return {"WHAT": ticker, "WHEN": listing_datetime + " (UTC)"}
