.PHONY: crawl run

crawl:
	PYTHONPATH=fieldingrange SCRAPY_SETTINGS_MODULE=fieldingrange.settings \
		uv run scrapy crawl savant \
		-a player_ids_path=$(PLAYER_IDS_PATH) \
		-o mlbam-savant-range-data.jsonl

