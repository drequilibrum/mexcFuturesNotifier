import pytest
from src.scraper import (
    scrape_announcements,
    extract_coin_ticker,
    extract_listing_datetime,
    reformat_datetime,
    get_latest_listing,
)


def test_scrape_announcements(target_url):
    announcements = scrape_announcements(target_url)
    assert isinstance(announcements, list), "Expected a list of announcements"
    assert all(
        isinstance(item, str) for item in announcements
    ), "Expected all announcements to be strings"
    assert all(
        "[Initial Futures Listing]" in item for item in announcements
    ), "Expected all announcements to contain '[Initial Futures Listing]'"


def test_extract_coin_ticker(sample_announcement):
    ticker = extract_coin_ticker(sample_announcement)
    assert ticker == "CELB", f"Expected 'CELB', but got {ticker}"


def test_extract_listing_datetime(sample_announcement):
    datetime = extract_listing_datetime(sample_announcement)
    assert (
        datetime == "2025-08-29 10:10:00"
    ), f"Expected '2025-08-29 10:10:00', but got {datetime}"


def test_reformat_datetime(sample_datetime):
    reformatted = reformat_datetime(sample_datetime)
    assert (
        reformatted == "2025-08-29 10:10:00"
    ), f"Expected '2025-08-29 10:10:00', but got {reformatted}"


def test_get_latest_listing():
    latest_listing = get_latest_listing()
    print(latest_listing)
    assert latest_listing == {
        "WHAT": "CELB",
        "WHEN": "2025-08-29 10:10:00 (UTC)",
    }, f"Expected {{'WHAT': 'CELB', 'WHEN': '2025-08-29 10:10:00 (UTC)'}}, but got {latest_listing}"
