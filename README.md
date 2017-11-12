# Scrapy crwaler for Shuku Ert page
http://www.shuku.net/novels/mulu/ert.html

# usage
```Bash
scrapy crawl ert -o contents.json
```

```
2017-11-12 22:12:28 [scrapy.extensions.feedexport] INFO: Stored json feed (4580 items) in: contents.json
2017-11-12 22:12:28 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 1606771,
 'downloader/request_count': 5080,
 'downloader/request_method_count/GET': 5080,
 'downloader/response_bytes': 35481595,
 'downloader/response_count': 5080,
 'downloader/response_status_count/200': 5054,
 'downloader/response_status_count/404': 26,
 'dupefilter/filtered': 90,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2017, 11, 12, 22, 12, 28, 816588),
 'httperror/response_ignored_count': 26,
 'httperror/response_ignored_status_count/404': 26,
 'item_scraped_count': 4606,
 'log_count/DEBUG': 9688,
 'log_count/ERROR': 28,
 'log_count/INFO': 36,
 'memusage/max': 76558336,
 'memusage/startup': 51601408,
 'offsite/filtered': 1,
 'request_depth_max': 2,
 'response_received_count': 5080,
 'scheduler/dequeued': 5079,
 'scheduler/dequeued/memory': 5079,
 'scheduler/enqueued': 5079,
 'scheduler/enqueued/memory': 5079,
 'spider_exceptions/AttributeError': 2,
 'start_time': datetime.datetime(2017, 11, 12, 22, 10, 18, 246576)}
```