# Fielding data crawler

## Installation

This project was set up using `uv`, and assumes its usage for installation and execution. Installation may also happen via `pip` in a standard virtual environment using the provided `requirements.txt` file, but will be less exhilarating. (The `Makefile` will also need to be modified.)

Clone this repository, then:

```shell
uv sync
```

or

```
pip install -r requirements.txt
```

```shell

## Usage

### Fetch player ids

Head to Fangraphs, and export a CSV capturing fielders from 2016-2024: https://www.fangraphs.com/leaders/major-league?pos=all&stats=fld&lg=all&type=1&ind=0&startdate=&enddate=&season1=2016&season=2024&qual=1&month=0

Then, use `xsv` to slim that down:

```shell
xsv select Pos,MLBAMID /path/to/export > player_ids.csv
```

### Crawling

To crawl, and assuming all requirements are satisfied, run:

```shell
PLAYER_IDS_FILE=/path/to/player_ids.csv make crawl
```

This will collect data for each player in the CSV, and store it a JSON-lines-formatted file, `mlbam-savant-range-data.jsonl`, in the same directory.

### Processing

The resultant file will have one line per event.
