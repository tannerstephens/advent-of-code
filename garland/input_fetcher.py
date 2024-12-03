import zoneinfo
from collections import UserString
from datetime import datetime, timezone
from pathlib import Path
from time import sleep, time

import requests


class InputFetcher:
    DEFAULT_CACHE_LOCATION = Path.home().resolve() / ".aoc"

    RATE_LIMIT_FILE_NAME = "ratelimit"
    SESSION_TOKEN_FILE_NAME = "sessiontoken"

    AOC_INPUT_FORMAT_URL = "https://adventofcode.com/{year}/day/{day}/input"
    TIME_BETWEEN_REQUESTS = 900
    RATE_LIMIT_SLEEP_TIME = 5

    USER_AGENT = "github.com/tannerstephens/advent-of-code by tanner@tannerstephens.com"

    def __init__(self, cache_location: Path | None = None) -> None:
        self._init_cache(cache_location)
        self._init_rate_limit()
        self._init_session_token()

    def _init_cache(self, cache_location: Path | None) -> None:
        self.cache_location = cache_location or self.DEFAULT_CACHE_LOCATION
        self.cache_location.mkdir(parents=True, exist_ok=True)

    def _init_rate_limit(self) -> None:
        self.rate_limit_file = self.cache_location / self.RATE_LIMIT_FILE_NAME
        if not self.rate_limit_file.exists():
            with open(self.rate_limit_file, "w") as f:
                f.write("0")

    def _init_session_token(self) -> None:
        self.session_token_file = self.cache_location / self.SESSION_TOKEN_FILE_NAME
        if not self.session_token_file.exists():
            self.session_token_file.touch()

        with open(self.session_token_file) as f:
            self.session_token = f.read().strip()

        if len(self.session_token) == 0:
            raise Exception(f"No session token found in {self.session_token_file}")

    def _get_input_file(self, year: int, day: int) -> Path:
        return self.cache_location / str(year) / str(day)

    def _get_cache(self, year: int, day: int) -> str | None:
        input_file = self._get_input_file(year, day)

        if not input_file.exists():
            return None

        with open(input_file) as f:
            return f.read()

    def _wait_for_rate_limit(self) -> None:
        with open(self.rate_limit_file) as f:
            last_request_time = float(f.read())

        new_remaining_time = remaining_time = int(
            self.TIME_BETWEEN_REQUESTS - (time() - last_request_time)
        )

        for _ in range(0, remaining_time, self.RATE_LIMIT_SLEEP_TIME):
            print(f"Waiting {new_remaining_time} seconds before grabbing input")
            sleep(self.RATE_LIMIT_SLEEP_TIME)
            new_remaining_time = int(self.TIME_BETWEEN_REQUESTS - (time() - last_request_time))

        if new_remaining_time > 0:
            print(f"Waiting {new_remaining_time} seconds before grabbing input")
            sleep(new_remaining_time)

    def _update_cache(self, year: int, day: int, data) -> None:
        input_file = self._get_input_file(year, day)
        input_file.parent.mkdir(exist_ok=True)

        with open(input_file, "w") as f:
            f.write(data)

    def _update_rate_limit(self) -> None:
        with open(self.rate_limit_file, "w") as f:
            f.write(str(time()))

    @property
    def cookies(self) -> dict[str, str]:
        return {"session": self.session_token}

    @property
    def headers(self) -> dict[str, str]:
        return {"User-Agent": self.USER_AGENT}

    def input_available(self, year: int, day: int) -> bool:
        now_utc = datetime.now(timezone.utc)
        available_time = datetime(
            year=year, month=12, day=day, tzinfo=zoneinfo.ZoneInfo("America/New_York")
        )

        return now_utc >= available_time

    def get_input(self, year: int, day: int) -> str:
        if cache := self._get_cache(year, day):
            return cache

        if not self.input_available(year, day):
            print("No puzzle input yet!")
            return None

        self._wait_for_rate_limit()

        input_url = self.AOC_INPUT_FORMAT_URL.format(year=year, day=day)
        aoc_input = requests.get(
            input_url, headers=self.headers, cookies=self.cookies
        ).content.decode()

        self._update_cache(year, day, aoc_input)
        self._update_rate_limit()

        return aoc_input
