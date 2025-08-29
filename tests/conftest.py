import pytest
from src.config import SCRAPE_URL


@pytest.fixture
def target_url():
    return SCRAPE_URL


@pytest.fixture
def sample_announcement():
    return "[Initial Futures Listing] CeluvPlay (CELB) USDT-M Futures to List on Aug 29, 2025, 10:10 (UTC)"


@pytest.fixture
def sample_datetime():
    return "Aug 29, 2025, 10:10 (UTC)"
