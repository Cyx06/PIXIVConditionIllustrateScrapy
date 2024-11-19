# Pixiv Condition-Based Illustration Scraper

This script scrapes illustrations from [Pixiv](https://www.pixiv.net/) based on specific search keywords and filters them by a minimum rating count. It downloads the filtered illustrations to a specified output directory.

---

## Features

- **Keyword Search**: Fetches illustrations related to a specified keyword.
- **Rating Filter**: Filters illustrations by a minimum "likes" or `rating_count` threshold.
- **Sorting**: Sorts illustrations by their rating count in descending order.
- **Download**: Downloads the filtered illustrations to the local system.

---

## Code Description

1. **Imports**:
   - `requests`: Handles HTTP requests for Pixiv API and image downloads.
   - `json`: Parses JSON responses from Pixiv.
   - `time` and `random`: Introduce delays and randomness to avoid detection during scraping.

2. **Proxy Support**:
   - Uses a list of proxies (`ip` array) to alternate IPs during requests.
   - Proxies are selected randomly for each request.

3. **Functions**:
   - `bubbleSort(arr, arr2)`: Sorts the `like` and `il_url` lists in descending order of ratings using Bubble Sort.
   - `pixiv_get(keyword, page, rating_count)`: Handles the main scraping logic:
   1. Sends GET requests to Pixiv's illustration search endpoint.
   2. Fetches illustration metadata, including `id` and `url`.
   3. Filters illustrations based on the `rating_count`.
   4. Downloads the filtered illustrations to the specified output directory.

4. **Key Parameters**:
   - `keyword`: The term to search on Pixiv (e.g., "中野四葉").
   - `page`: Number of pages to scrape.
   - `rating_count`: Minimum "likes" required to download an illustration.

5. **Output**:
   - Downloads filtered illustrations as `.jpg` files in the specified directory.
   - Names files sequentially (`text_1.jpg`, `text_2.jpg`, etc.).

## How to Use This Code

### 1. Replace Input Parameters

Open the script and update the following:

#### Search Parameters

- `keyword`: Search keyword, e.g., `"中野四葉"`.
- `page`: Number of pages to scrape, e.g., `1`.
- `rating_count`: Minimum "likes" required to download an illustration, e.g.,`100`.

#### Output Path

- Replace `/output/path/` with the directory where images should be saved.


### 2. Run the Script
Run the script using the following command:
```
python PIXIVConditionIllustrateScrapy.py
```