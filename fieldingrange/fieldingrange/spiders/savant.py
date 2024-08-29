import csv
import json
from typing import Iterable

import scrapy
from scrapy import Request


class SavantSpider(scrapy.Spider):
    name = "savant"
    allowed_domains = ["baseballsavant.mlb.com"]
    start_urls = ["https://baseballsavant.mlb.com"]

    def __init__(self, player_ids_path: str, *args, **kwargs):
        self.player_ids_path = player_ids_path

        super(SavantSpider, self).__init__(*args, **kwargs)

    def start_requests(self) -> Iterable[Request]:
        def get_player_type(value: str):
            return 'pitcher' if value == 'P' else 'fielder'

        reader: Iterable[dict[str, str]] = csv.DictReader(open(self.player_ids_path))

        for player in reader:
            for season in range(2016, 2025):
                player_id = player['MLBAMID']
                player_type = get_player_type(player['Pos'])
                url = f'https://baseballsavant.mlb.com/player-services/range?playerId={player_id}&season={season}&playerType={player_type}'
                yield Request(url, callback=self.parse, meta={
                    'season': season,
                })

    def parse(self, response, **kwargs):
        body = json.loads(response.text)

        for row in body:
            row['season'] = response.meta['season']
            yield row
