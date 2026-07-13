# SQLite 数据摘要

文件: `dacomp-zh-078.sqlite`


## pendo__account

- Rows: 1000

- Columns: account_id (TEXT), last_updated_at (TEXT), account_id_hash (REAL), first_visit_at (TEXT), last_visit_at (TEXT), latest_account_index (INTEGER), count_associated_visitors (INTEGER), min_nps_rating (INTEGER), max_nps_rating (INTEGER), avg_nps_rating (REAL), count_active_visitors (REAL), count_page_viewing_visitors (REAL), count_feature_clicking_visitors (REAL), count_active_days (INTEGER), count_active_months (INTEGER), sum_minutes (REAL), sum_events (REAL), count_event_records (REAL), average_daily_minutes (REAL), average_daily_events (REAL), first_event_on (TIMESTAMP), last_event_on (TIMESTAMP)

```json
[
  {
    "account_id": "ACC00000001",
    "last_updated_at": "2024-04-17 00:00:00.000 +0800",
    "account_id_hash": 3134190643.0,
    "first_visit_at": "2024-01-08 00:00:00.000 +0800",
    "last_visit_at": "2024-04-17 00:00:00.000 +0800",
    "latest_account_index": 1,
    "count_associated_visitors": 78,
    "min_nps_rating": 6,
    "max_nps_rating": 9,
    "avg_nps_rating": 7.333333333333333,
    "count_active_visitors": 56.0,
    "count_page_viewing_visitors": 71.0,
    "count_feature_clicking_visitors": 39.0,
    "count_active_days": 33,
    "count_active_months": 2,
    "sum_minutes": 8243.0,
    "sum_events": 17783.0,
    "count_event_records": 17788.0,
    "average_daily_minutes": 249.78787878787878,
    "average_daily_events": 538.8787878787879,
    "first_event_on": "2024-01-08 00:00:00",
    "last_event_on": "2024-04-17 00:00:00"
  },
  {
    "account_id": "ACC00000002",
    "last_updated_at": "2024-02-23 00:00:00.000 +0800",
    "account_id_hash": 3657993941.0,
    "first_visit_at": "2024-01-18 00:00:00.000 +0800",
    "last_visit_at": "2024-02-23 00:00:00.000 +0800",
    "latest_account_index": 2,
    "count_associated_visitors": 109,
    "min_nps_rating": 6,
    "max_nps_rating": 6,
    "avg_nps_rating": 6.0,
    "count_active_visitors": 88.0,
    "count_page_viewing_visitors": 97.0,
    "count_feature_clicking_visitors": 82.0,
    "count_active_days": 11,
    "count_active_months": 1,
    "sum_minutes": 2248.0,
    "sum_events": 4596.0,
    "count_event_records": 4740.0,
    "average_daily_minutes": 204.36363636363637,
    "average_daily_events": 417.8181818181818,
    "first_event_on": "2024-01-18 00:00:00",
    "last_event_on": "2024-02-23 00:00:00"
  },
  {
    "account_id": "ACC00000003",
    "last_updated_at": "2024-05-05 00:00:00.000 +0800",
    "account_id_hash": 2410074845.0,
    "first_visit_at": "2024-01-09 00:00:00.000 +0800",
    "last_visit_at": "2024-05-05 00:00:00.000 +0800",
    "latest_account_index": 3,
    "count_associated_visitors": 90,
    "min_nps_rating": 8,
    "max_nps_rating": 8,
    "avg_nps_rating": 8.0,
    "count_active_visitors": 71.0,
    "count_page_viewing_visitors": 81.0,
    "count_feature_clicking_visitors": 54.0,
    "count_active_days": 34,
    "count_active_months": 2,
    "sum_minutes": 33452.0,
    "sum_events": 81769.0,
    "count_event_records": 81786.0,
    "average_daily_minutes": 983.8823529411765,
    "average_daily_events": 2404.970588235294,
    "first_event_on": "2024-01-09 00:00:00",
    "last_event_on": "2024-05-05 00:00:00"
  }
]
```


## pendo__feature

- Rows: 2000

- Columns: feature_id (TEXT), app_id (TEXT), created_at (TEXT), created_by_user_id (TEXT), is_dirty (INTEGER), group_id (INTEGER), is_core_event (INTEGER), last_updated_at (TEXT), last_updated_by_user_id (TEXT), feature_name (TEXT), page_id (TEXT), root_version_id (INTEGER), stable_version_id (INTEGER), valid_through (TEXT), product_area_name (TEXT), page_name (TEXT), page_created_at (TEXT), page_valid_through (TEXT), app_display_name (TEXT), app_platform (TEXT), created_by_user_full_name (TEXT), created_by_user_username (TEXT), last_updated_by_user_full_name (TEXT), last_updated_by_user_username (TEXT), count_visitors (INTEGER), count_accounts (INTEGER), sum_clicks (REAL), count_click_events (INTEGER), first_click_at (TEXT), last_click_at (TEXT), avg_visitor_minutes (REAL), avg_visitor_events (REAL)

```json
[
  {
    "feature_id": "FEA10000000001",
    "app_id": "APP10000000196",
    "created_at": "2023-05-24 21:36:06.612 +0800",
    "created_by_user_id": "USE10000000110",
    "is_dirty": 0,
    "group_id": 87019997192,
    "is_core_event": 0,
    "last_updated_at": "2024-10-14 22:36:07.343 +0800",
    "last_updated_by_user_id": "USE10000000092",
    "feature_name": "professor",
    "page_id": "PAG10000001104",
    "root_version_id": 5920747680,
    "stable_version_id": 3267087256,
    "valid_through": "2023-06-07 13:52:45.700 +0800",
    "product_area_name": null,
    "page_name": "same",
    "page_created_at": "2023-03-29 20:54:45.804 +0800",
    "page_valid_through": "2023-06-22 18:17:57.252 +0800",
    "app_display_name": "Blair LLC",
    "app_platform": "mobile",
    "created_by_user_full_name": "Blake Patel",
    "created_by_user_username": "casey50",
    "last_updated_by_user_full_name": "Edward Reyes",
    "last_updated_by_user_username": "jasminebrown",
    "count_visitors": 11,
    "count_accounts": 11,
    "sum_clicks": 5919.629999999999,
    "count_click_events": 11,
    "first_click_at": "2021-04-04 22:13:41.533 +0800",
    "last_click_at": "2024-10-31 06:59:19.962 +0800",
    "avg_visitor_minutes": 45.586,
    "avg_visitor_events": 538.148
  },
  {
    "feature_id": "FEA10000000054",
    "app_id": "APP10000000174",
    "created_at": "2022-07-14 17:59:13.300 +0800",
    "created_by_user_id": "USE10000000117",
    "is_dirty": 1,
    "group_id": 75368374291,
    "is_core_event": 0,
    "last_updated_at": "2023-05-30 07:17:53.540 +0800",
    "last_updated_by_user_id": "USE10000000062",
    "feature_name": "start",
    "page_id": "PAG10000001198",
    "root_version_id": 9883711099,
    "stable_version_id": 5860398457,
    "valid_through": "2023-01-30 21:18:39.043 +0800",
    "product_area_name": null,
    "page_name": "culture",
    "page_created_at": "2024-03-29 20:53:53.056 +0800",
    "page_valid_through": "2024-10-29 08:13:57.622 +0800",
    "app_display_name": "Jenkins-Fields",
    "app_platform": "mobile",
    "created_by_user_full_name": "Matthew Beard",
    "created_by_user_username": "angela83",
    "last_updated_by_user_full_name": "Sarah Stanton",
    "last_updated_by_user_username": "nolanjason",
    "count_visitors": 12,
    "count_accounts": 12,
    "sum_clicks": 6645.9,
    "count_click_events": 12,
    "first_click_at": "2021-06-28 05:13:16.799 +0800",
    "last_click_at": "2024-11-30 22:54:06.033 +0800",
    "avg_visitor_minutes": 47.697,
    "avg_visitor_events": 553.825
  },
  {
    "feature_id": "FEA10000000074",
    "app_id": "APP10000000042",
    "created_at": "2024-01-15 23:07:35.355 +0800",
    "created_by_user_id": "USE10000000086",
    "is_dirty": 0,
    "group_id": 12717805329,
    "is_core_event": 0,
    "last_updated_at": "2024-11-18 11:13:29.178 +0800",
    "last_updated_by_user_id": "USE10000000053",
    "feature_name": "serve",
    "page_id": "PAG10000000087",
    "root_version_id": 7181922407,
    "stable_version_id": 3620488440,
    "valid_through": "2024-02-03 02:08:31.422 +0800",
    "product_area_name": null,
    "page_name": "consumer",
    "page_created_at": "2021-11-22 04:46:56.666 +0800",
    "page_valid_through": "2022-01-21 18:59:43.348 +0800",
    "app_display_name": "Turner PLC",
    "app_platform": "api",
    "created_by_user_full_name": "Samantha Martinez",
    "created_by_user_username": "lauriecontreras",
    "last_updated_by_user_full_name": "Joseph Mahoney",
    "last_updated_by_user_username": "suarezmike",
    "count_visitors": 12,
    "count_accounts": 10,
    "sum_clicks": 7400.7300000000005,
    "count_click_events": 12,
    "first_click_at": "2021-02-08 17:48:42.168 +0800",
    "last_click_at": "2024-08-27 11:24:02.709 +0800",
    "avg_visitor_minutes": 43.651,
    "avg_visitor_events": 616.728
  }
]
```


## pendo__visitor

- Rows: 38544

- Columns: visitor_id (TEXT), account_id (TEXT), first_visit_at (TEXT), visitor_id_hash (REAL), last_browser_name (TEXT), last_browser_version (REAL), last_operating_system (TEXT), last_server_name (TEXT), last_updated_at (TEXT), last_user_agent (TEXT), last_visit (TEXT), n_id (INTEGER), latest_visitor_index (INTEGER), count_associated_accounts (INTEGER), latest_nps_rating (INTEGER), count_active_days (INTEGER), count_active_months (INTEGER), sum_minutes (REAL), sum_events (REAL), count_event_records (REAL), average_daily_minutes (REAL), average_daily_events (REAL), first_event_on (TIMESTAMP), last_event_on (TIMESTAMP)

```json
[
  {
    "visitor_id": "VIS0000000001",
    "account_id": "ACC00000001",
    "first_visit_at": "2024-01-14 00:00:00.000 +0800",
    "visitor_id_hash": 2207641263.0,
    "last_browser_name": "Chrome",
    "last_browser_version": 104.83100999519665,
    "last_operating_system": "Windows 11",
    "last_server_name": "app5.company.com",
    "last_updated_at": "2024-02-07 00:00:00.000 +0800",
    "last_user_agent": "Mozilla/5.0 (Windows 11) Chrome/104.83100999519665",
    "last_visit": "2024-02-07 00:00:00.000 +0800",
    "n_id": 1,
    "latest_visitor_index": 1,
    "count_associated_accounts": 1,
    "latest_nps_rating": 6,
    "count_active_days": 24,
    "count_active_months": 1,
    "sum_minutes": 49.0,
    "sum_events": 106.0,
    "count_event_records": 106.0,
    "average_daily_minutes": 2.0416666666666665,
    "average_daily_events": 4.416666666666667,
    "first_event_on": "2024-01-14 00:00:00",
    "last_event_on": "2024-02-07 00:00:00"
  },
  {
    "visitor_id": "VIS0000000002",
    "account_id": "ACC00000001",
    "first_visit_at": "2024-01-09 00:00:00.000 +0800",
    "visitor_id_hash": 7998140507.0,
    "last_browser_name": "Chrome",
    "last_browser_version": 90.59594438876141,
    "last_operating_system": "Windows 11",
    "last_server_name": "app5.company.com",
    "last_updated_at": "2024-02-01 00:00:00.000 +0800",
    "last_user_agent": "Mozilla/5.0 (Windows 11) Chrome/90.59594438876141",
    "last_visit": "2024-02-01 00:00:00.000 +0800",
    "n_id": 2,
    "latest_visitor_index": 2,
    "count_associated_accounts": 1,
    "latest_nps_rating": 7,
    "count_active_days": 23,
    "count_active_months": 1,
    "sum_minutes": 17.0,
    "sum_events": 38.0,
    "count_event_records": 45.0,
    "average_daily_minutes": 0.7391304347826086,
    "average_daily_events": 1.6521739130434783,
    "first_event_on": "2024-01-09 00:00:00",
    "last_event_on": "2024-02-01 00:00:00"
  },
  {
    "visitor_id": "VIS0000000003",
    "account_id": "ACC00000001",
    "first_visit_at": "2024-01-08 00:00:00.000 +0800",
    "visitor_id_hash": 9166134714.0,
    "last_browser_name": "Firefox",
    "last_browser_version": 94.40881244081393,
    "last_operating_system": "Android",
    "last_server_name": "app2.company.com",
    "last_updated_at": "2024-02-03 00:00:00.000 +0800",
    "last_user_agent": "Mozilla/5.0 (Android) Firefox/94.40881244081393",
    "last_visit": "2024-02-03 00:00:00.000 +0800",
    "n_id": 3,
    "latest_visitor_index": 3,
    "count_associated_accounts": 1,
    "latest_nps_rating": 7,
    "count_active_days": 26,
    "count_active_months": 1,
    "sum_minutes": 6.0,
    "sum_events": 13.0,
    "count_event_records": 35.0,
    "average_daily_minutes": 0.23076923076923078,
    "average_daily_events": 0.5,
    "first_event_on": "2024-01-08 00:00:00",
    "last_event_on": "2024-02-03 00:00:00"
  }
]
```


## pendo__visitor_daily_metrics

- Rows: 29057

- Columns: date_day (TIMESTAMP), visitor_id (TEXT), sum_minutes (REAL), sum_events (REAL), count_event_records (INTEGER), count_pages_viewed (INTEGER), count_features_clicked (INTEGER)

```json
[
  {
    "date_day": "2024-01-14 00:00:00",
    "visitor_id": "VIS0000000001",
    "sum_minutes": 2.0,
    "sum_events": 4.0,
    "count_event_records": 2,
    "count_pages_viewed": 1,
    "count_features_clicked": 0
  },
  {
    "date_day": "2024-01-15 00:00:00",
    "visitor_id": "VIS0000000001",
    "sum_minutes": 2.0,
    "sum_events": 5.0,
    "count_event_records": 3,
    "count_pages_viewed": 1,
    "count_features_clicked": 0
  },
  {
    "date_day": "2024-01-16 00:00:00",
    "visitor_id": "VIS0000000001",
    "sum_minutes": 1.0,
    "sum_events": 3.0,
    "count_event_records": 1,
    "count_pages_viewed": 1,
    "count_features_clicked": 0
  }
]
```


## pendo__visitor_feature

- Rows: 24982

- Columns: visitor_id (TEXT), feature_id (TEXT), first_click_at (TEXT), last_click_at (TEXT), sum_clicks (REAL), sum_minutes (REAL), avg_daily_minutes (REAL), count_active_days (INTEGER), count_click_events (INTEGER)

```json
[
  {
    "visitor_id": "VIS10000007711",
    "feature_id": "FEA10000000595",
    "first_click_at": "2022-01-03 01:15:57.187 +0800",
    "last_click_at": "2022-01-03 01:15:57.187 +0800",
    "sum_clicks": 304.11,
    "sum_minutes": 94.45,
    "avg_daily_minutes": 94.45,
    "count_active_days": 1,
    "count_click_events": 1
  },
  {
    "visitor_id": "VIS10000000956",
    "feature_id": "FEA10000000540",
    "first_click_at": "2024-12-25 19:49:34.978 +0800",
    "last_click_at": "2024-12-25 19:49:34.978 +0800",
    "sum_clicks": 224.64,
    "sum_minutes": 70.36,
    "avg_daily_minutes": 70.36,
    "count_active_days": 1,
    "count_click_events": 1
  },
  {
    "visitor_id": "VIS10000006258",
    "feature_id": "FEA10000001734",
    "first_click_at": "2023-04-03 03:44:50.774 +0800",
    "last_click_at": "2023-04-03 03:44:50.774 +0800",
    "sum_clicks": 434.2,
    "sum_minutes": 94.48,
    "avg_daily_minutes": 94.48,
    "count_active_days": 1,
    "count_click_events": 1
  }
]
```
