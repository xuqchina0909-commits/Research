# SQLite 数据摘要

文件: `dacomp-zh-079.sqlite`


## pendo__account

- Rows: 1000

- Columns: account_id (TEXT), last_updated_at (TEXT), account_id_hash (REAL), first_visit_at (TEXT), last_visit_at (TEXT), latest_account_index (INTEGER), count_associated_visitors (INTEGER), min_nps_rating (INTEGER), max_nps_rating (INTEGER), avg_nps_rating (REAL), count_active_visitors (REAL), count_page_viewing_visitors (REAL), count_feature_clicking_visitors (REAL), count_active_days (INTEGER), count_active_months (INTEGER), sum_minutes (REAL), sum_events (REAL), count_event_records (REAL), average_daily_minutes (REAL), average_daily_events (REAL), first_event_on (TIMESTAMP), last_event_on (TIMESTAMP)

```json
[
  {
    "account_id": "ACC10000000039",
    "last_updated_at": "2024-12-03 05:03:02.601 +0800",
    "account_id_hash": 518.0,
    "first_visit_at": "2021-10-28 05:50:05.228 +0800",
    "last_visit_at": "2022-10-15 05:50:05.228 +0800",
    "latest_account_index": 1,
    "count_associated_visitors": 8,
    "min_nps_rating": 4,
    "max_nps_rating": 10,
    "avg_nps_rating": 7.235294117647059,
    "count_active_visitors": 121.0,
    "count_page_viewing_visitors": 6.0,
    "count_feature_clicking_visitors": 6.0,
    "count_active_days": 118,
    "count_active_months": 44,
    "sum_minutes": 7264.0,
    "sum_events": 3237.0,
    "count_event_records": 122.0,
    "average_daily_minutes": 61.559322033898304,
    "average_daily_events": 27.43220338983051,
    "first_event_on": "2021-02-01 00:00:00",
    "last_event_on": "2024-12-29 00:00:00"
  },
  {
    "account_id": "ACC10000000045",
    "last_updated_at": "2025-01-20 03:11:59.930 +0800",
    "account_id_hash": 398.12,
    "first_visit_at": "2024-01-24 03:11:59.524 +0800",
    "last_visit_at": "2025-01-20 03:11:59.524 +0800",
    "latest_account_index": 1,
    "count_associated_visitors": 11,
    "min_nps_rating": 4,
    "max_nps_rating": 9,
    "avg_nps_rating": 6.809523809523809,
    "count_active_visitors": 134.0,
    "count_page_viewing_visitors": 8.0,
    "count_feature_clicking_visitors": 8.0,
    "count_active_days": 125,
    "count_active_months": 47,
    "sum_minutes": 7811.0,
    "sum_events": 3314.0,
    "count_event_records": 134.0,
    "average_daily_minutes": 62.488,
    "average_daily_events": 26.512,
    "first_event_on": "2021-01-09 00:00:00",
    "last_event_on": "2024-12-11 00:00:00"
  },
  {
    "account_id": "ACC10000000048",
    "last_updated_at": "2023-11-01 13:33:45.058 +0800",
    "account_id_hash": 535.76,
    "first_visit_at": "2023-05-29 00:02:32.906 +0800",
    "last_visit_at": "2023-08-25 00:02:32.906 +0800",
    "latest_account_index": 1,
    "count_associated_visitors": 6,
    "min_nps_rating": 5,
    "max_nps_rating": 9,
    "avg_nps_rating": 6.625,
    "count_active_visitors": 56.0,
    "count_page_viewing_visitors": 1.0,
    "count_feature_clicking_visitors": 1.0,
    "count_active_days": 56,
    "count_active_months": 37,
    "sum_minutes": 3135.0,
    "sum_events": 1316.0,
    "count_event_records": 56.0,
    "average_daily_minutes": 55.982142857142854,
    "average_daily_events": 23.5,
    "first_event_on": "2021-01-06 00:00:00",
    "last_event_on": "2024-12-24 00:00:00"
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
    "is_core_event": 1,
    "last_updated_at": "2024-10-14 22:36:07.343 +0800",
    "last_updated_by_user_id": "USE10000000092",
    "feature_name": "login",
    "page_id": "PAG10000001104",
    "root_version_id": 5920747680,
    "stable_version_id": 3267087256,
    "valid_through": "2023-06-07 13:52:45.700 +0800",
    "product_area_name": "authentication",
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
    "feature_name": "mobile_dashboard",
    "page_id": "PAG10000001198",
    "root_version_id": 9883711099,
    "stable_version_id": 5860398457,
    "valid_through": "2023-01-30 21:18:39.043 +0800",
    "product_area_name": "mobile",
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
    "is_core_event": 1,
    "last_updated_at": "2024-11-18 11:13:29.178 +0800",
    "last_updated_by_user_id": "USE10000000053",
    "feature_name": "export_dashboard_v2",
    "page_id": "PAG10000000087",
    "root_version_id": 7181922407,
    "stable_version_id": 3620488440,
    "valid_through": "2024-02-03 02:08:31.422 +0800",
    "product_area_name": "dashboard",
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

- Rows: 8000

- Columns: visitor_id (TEXT), account_id (TEXT), first_visit_at (TEXT), visitor_id_hash (REAL), last_browser_name (TEXT), last_browser_version (REAL), last_operating_system (TEXT), last_server_name (TEXT), last_updated_at (TEXT), last_user_agent (TEXT), last_visit (TEXT), n_id (INTEGER), latest_visitor_index (INTEGER), count_associated_accounts (INTEGER), latest_nps_rating (INTEGER), count_active_days (INTEGER), count_active_months (INTEGER), sum_minutes (REAL), sum_events (REAL), count_event_records (REAL), average_daily_minutes (REAL), average_daily_events (REAL), first_event_on (TIMESTAMP), last_event_on (TIMESTAMP)

```json
[
  {
    "visitor_id": "VIS10000007766",
    "account_id": "ACC10000000221",
    "first_visit_at": "2021-04-02 13:42:30.475 +0800",
    "visitor_id_hash": 260.2,
    "last_browser_name": "Opera",
    "last_browser_version": 90.0,
    "last_operating_system": "Windows 10",
    "last_server_name": "analytics.com",
    "last_updated_at": "2023-03-17 22:52:57.929 +0800",
    "last_user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "last_visit": "2022-01-12 13:42:30.475 +0800",
    "n_id": 5845155951,
    "latest_visitor_index": 1,
    "count_associated_accounts": 1,
    "latest_nps_rating": 8,
    "count_active_days": 56,
    "count_active_months": 1,
    "sum_minutes": 1271.0,
    "sum_events": 1804.0,
    "count_event_records": 6.0,
    "average_daily_minutes": 22.696428571428573,
    "average_daily_events": 32.214285714285715,
    "first_event_on": "2025-07-31 00:00:00",
    "last_event_on": "2025-10-14 00:00:00"
  },
  {
    "visitor_id": "VIS10000004523",
    "account_id": "ACC10000000086",
    "first_visit_at": "2021-03-26 22:30:37.990 +0800",
    "visitor_id_hash": 969.8,
    "last_browser_name": "Chrome",
    "last_browser_version": 90.0,
    "last_operating_system": "Ubuntu 20.04",
    "last_server_name": "analytics.com",
    "last_updated_at": "2022-02-12 00:49:47.045 +0800",
    "last_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "last_visit": "2022-01-11 22:30:37.990 +0800",
    "n_id": 2750804575,
    "latest_visitor_index": 1,
    "count_associated_accounts": 1,
    "latest_nps_rating": 7,
    "count_active_days": 31,
    "count_active_months": 1,
    "sum_minutes": 950.0,
    "sum_events": 389.0,
    "count_event_records": 10.0,
    "average_daily_minutes": 30.64516129032258,
    "average_daily_events": 12.548387096774194,
    "first_event_on": "2025-09-02 00:00:00",
    "last_event_on": "2025-10-14 00:00:00"
  },
  {
    "visitor_id": "VIS10000007245",
    "account_id": "ACC10000000412",
    "first_visit_at": "2022-11-02 08:42:16.521 +0800",
    "visitor_id_hash": 525.08,
    "last_browser_name": "Opera",
    "last_browser_version": 92.0,
    "last_operating_system": "Ubuntu 20.04",
    "last_server_name": "analytics.com",
    "last_updated_at": "2024-12-12 05:52:08.399 +0800",
    "last_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "last_visit": "2023-07-14 08:42:16.521 +0800",
    "n_id": 5828280823,
    "latest_visitor_index": 1,
    "count_associated_accounts": 1,
    "latest_nps_rating": 5,
    "count_active_days": 23,
    "count_active_months": 1,
    "sum_minutes": 1484.0,
    "sum_events": 952.0,
    "count_event_records": 8.0,
    "average_daily_minutes": 64.52173913043478,
    "average_daily_events": 41.391304347826086,
    "first_event_on": "2025-08-28 00:00:00",
    "last_event_on": "2025-10-14 00:00:00"
  }
]
```


## pendo__visitor_feature

- Rows: 62077

- Columns: visitor_id (TEXT), feature_id (TEXT), first_click_at (TEXT), last_click_at (TEXT), sum_clicks (REAL), sum_minutes (REAL), avg_daily_minutes (REAL), count_active_days (INTEGER), count_click_events (INTEGER)

```json
[
  {
    "visitor_id": "VIS10000000001",
    "feature_id": "FEA10000000009",
    "first_click_at": "2025-10-10T13:39:47.471842",
    "last_click_at": "2025-10-14T13:39:47.471844",
    "sum_clicks": 68.0,
    "sum_minutes": 42.0,
    "avg_daily_minutes": 7.0,
    "count_active_days": 6,
    "count_click_events": 68
  },
  {
    "visitor_id": "VIS10000000001",
    "feature_id": "FEA10000000014",
    "first_click_at": "2025-10-11T13:39:47.472642",
    "last_click_at": "2025-10-12T13:39:47.472643",
    "sum_clicks": 99.0,
    "sum_minutes": 35.0,
    "avg_daily_minutes": 11.666666666666666,
    "count_active_days": 3,
    "count_click_events": 99
  },
  {
    "visitor_id": "VIS10000000001",
    "feature_id": "FEA10000000010",
    "first_click_at": "2025-10-04T13:39:47.473208",
    "last_click_at": "2025-10-10T13:39:47.473209",
    "sum_clicks": 4.0,
    "sum_minutes": 17.0,
    "avg_daily_minutes": 1.7,
    "count_active_days": 10,
    "count_click_events": 4
  }
]
```
