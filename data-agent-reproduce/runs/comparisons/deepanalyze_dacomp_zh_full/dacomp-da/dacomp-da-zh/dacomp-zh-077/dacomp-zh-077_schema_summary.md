# SQLite 数据摘要

文件: `dacomp-zh-077.sqlite`


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
    "min_nps_rating": null,
    "max_nps_rating": null,
    "avg_nps_rating": null,
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
    "min_nps_rating": null,
    "max_nps_rating": null,
    "avg_nps_rating": null,
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
    "min_nps_rating": null,
    "max_nps_rating": null,
    "avg_nps_rating": null,
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


## pendo__customer_lifecycle_insights

- Rows: 8000

- Columns: visitor_id (TEXT), account_id (TEXT), first_event_on (TIMESTAMP), last_event_on (TIMESTAMP), count_active_days (INTEGER), count_active_months (INTEGER), sum_events (REAL), sum_minutes (REAL), average_daily_events (REAL), average_daily_minutes (REAL), count_associated_accounts (INTEGER), lifecycle_stage (TEXT), user_value_score (REAL), engagement_trend (TEXT), churn_risk_level (TEXT), is_valuable_user (INTEGER), needs_attention (INTEGER), is_new_user (INTEGER), activity_density (REAL), usage_intensity (TEXT), rfm_segment (TEXT), customer_value_tier (TEXT), recency_score (INTEGER), frequency_score (INTEGER), magnitude_score (INTEGER), rfm_composite_score (REAL), recommended_strategy (TEXT), predicted_clv_tier (TEXT), action_priority (TEXT), overall_health_score (REAL), health_grade (TEXT), primary_improvement_area (TEXT), product_risk_level (TEXT), net_promoter_score (REAL), feature_adoption_rate (REAL), account_retention_30d (REAL), customer_segment_label (TEXT), comprehensive_customer_value (REAL), recommended_next_action (TEXT), customer_journey_stage (TEXT), predicted_ltv_tier (TEXT), engagement_velocity (REAL), usage_trend (TEXT), account_influence_level (TEXT), calculated_at (TIMESTAMP), customer_importance_level (TEXT), investment_expectation (TEXT)

```json
[
  {
    "visitor_id": "VIS10000007766",
    "account_id": "ACC10000000221",
    "first_event_on": "2025-08-18 00:00:00",
    "last_event_on": "2025-09-27 00:00:00",
    "count_active_days": 91,
    "count_active_months": null,
    "sum_events": 396.0,
    "sum_minutes": 5441.0,
    "average_daily_events": 33.736221216841415,
    "average_daily_minutes": 106.31915043231736,
    "count_associated_accounts": null,
    "lifecycle_stage": "At Risk",
    "user_value_score": 23.054454803466797,
    "engagement_trend": null,
    "churn_risk_level": null,
    "is_valuable_user": null,
    "needs_attention": null,
    "is_new_user": null,
    "activity_density": null,
    "usage_intensity": "Heavy",
    "rfm_segment": null,
    "customer_value_tier": null,
    "recency_score": null,
    "frequency_score": null,
    "magnitude_score": null,
    "rfm_composite_score": null,
    "recommended_strategy": null,
    "predicted_clv_tier": null,
    "action_priority": null,
    "overall_health_score": 20.094316482543945,
    "health_grade": "D",
    "primary_improvement_area": null,
    "product_risk_level": null,
    "net_promoter_score": 45.0,
    "feature_adoption_rate": 0.7610238194465637,
    "account_retention_30d": null,
    "customer_segment_label": null,
    "comprehensive_customer_value": 132.23069763183594,
    "recommended_next_action": null,
    "customer_journey_stage": null,
    "predicted_ltv_tier": null,
    "engagement_velocity": null,
    "usage_trend": null,
    "account_influence_level": null,
    "calculated_at": null,
    "customer_importance_level": null,
    "investment_expectation": null
  },
  {
    "visitor_id": "VIS10000004523",
    "account_id": "ACC10000000086",
    "first_event_on": "2025-05-07 00:00:00",
    "last_event_on": "2025-09-28 00:00:00",
    "count_active_days": 134,
    "count_active_months": null,
    "sum_events": 1175.0,
    "sum_minutes": 527.0,
    "average_daily_events": 49.53886965459652,
    "average_daily_minutes": 19.229158839396984,
    "count_associated_accounts": null,
    "lifecycle_stage": "Churned",
    "user_value_score": 16.163347244262695,
    "engagement_trend": null,
    "churn_risk_level": null,
    "is_valuable_user": null,
    "needs_attention": null,
    "is_new_user": null,
    "activity_density": null,
    "usage_intensity": "Power User",
    "rfm_segment": null,
    "customer_value_tier": null,
    "recency_score": null,
    "frequency_score": null,
    "magnitude_score": null,
    "rfm_composite_score": null,
    "recommended_strategy": null,
    "predicted_clv_tier": null,
    "action_priority": null,
    "overall_health_score": 17.147485733032227,
    "health_grade": "D",
    "primary_improvement_area": null,
    "product_risk_level": null,
    "net_promoter_score": 11.0,
    "feature_adoption_rate": 0.1054738238453865,
    "account_retention_30d": null,
    "customer_segment_label": null,
    "comprehensive_customer_value": 95.01248168945312,
    "recommended_next_action": null,
    "customer_journey_stage": null,
    "predicted_ltv_tier": null,
    "engagement_velocity": null,
    "usage_trend": null,
    "account_influence_level": null,
    "calculated_at": null,
    "customer_importance_level": null,
    "investment_expectation": null
  },
  {
    "visitor_id": "VIS10000007245",
    "account_id": "ACC10000000412",
    "first_event_on": "2025-04-12 00:00:00",
    "last_event_on": "2025-09-26 00:00:00",
    "count_active_days": 6,
    "count_active_months": null,
    "sum_events": 4111.0,
    "sum_minutes": 2702.0,
    "average_daily_events": 22.69836469746071,
    "average_daily_minutes": 88.09680990429725,
    "count_associated_accounts": null,
    "lifecycle_stage": "Churned",
    "user_value_score": 16.800230026245117,
    "engagement_trend": null,
    "churn_risk_level": null,
    "is_valuable_user": null,
    "needs_attention": null,
    "is_new_user": null,
    "activity_density": null,
    "usage_intensity": "Light",
    "rfm_segment": null,
    "customer_value_tier": null,
    "recency_score": null,
    "frequency_score": null,
    "magnitude_score": null,
    "rfm_composite_score": null,
    "recommended_strategy": null,
    "predicted_clv_tier": null,
    "action_priority": null,
    "overall_health_score": 16.203615188598633,
    "health_grade": "D",
    "primary_improvement_area": null,
    "product_risk_level": null,
    "net_promoter_score": 16.0,
    "feature_adoption_rate": 0.43076518177986145,
    "account_retention_30d": null,
    "customer_segment_label": null,
    "comprehensive_customer_value": 132.92849731445312,
    "recommended_next_action": null,
    "customer_journey_stage": null,
    "predicted_ltv_tier": null,
    "engagement_velocity": null,
    "usage_trend": null,
    "account_influence_level": null,
    "calculated_at": null,
    "customer_importance_level": null,
    "investment_expectation": null
  }
]
```


## pendo__feature

- Rows: 180

- Columns: feature_id (TEXT), app_id (TEXT), created_at (TEXT), created_by_user_id (TEXT), is_dirty (INTEGER), group_id (INTEGER), is_core_event (INTEGER), last_updated_at (TEXT), last_updated_by_user_id (TEXT), feature_name (TEXT), page_id (TEXT), root_version_id (INTEGER), stable_version_id (INTEGER), valid_through (TEXT), product_area_name (TEXT), page_name (TEXT), page_created_at (TEXT), page_valid_through (TEXT), app_display_name (TEXT), app_platform (TEXT), created_by_user_full_name (TEXT), created_by_user_username (TEXT), last_updated_by_user_full_name (TEXT), last_updated_by_user_username (TEXT), count_visitors (INTEGER), count_accounts (INTEGER), sum_clicks (REAL), count_click_events (INTEGER), first_click_at (TEXT), last_click_at (TEXT), avg_visitor_minutes (REAL), avg_visitor_events (REAL)

```json
[
  {
    "feature_id": "FEAT_00001",
    "app_id": "MAIN_APP_001",
    "created_at": "2025-03-30T13:36:06.740333",
    "created_by_user_id": null,
    "is_dirty": null,
    "group_id": null,
    "is_core_event": 1,
    "last_updated_at": null,
    "last_updated_by_user_id": null,
    "feature_name": "User Profile Edit",
    "page_id": null,
    "root_version_id": null,
    "stable_version_id": null,
    "valid_through": null,
    "product_area_name": "User Management",
    "page_name": null,
    "page_created_at": null,
    "page_valid_through": null,
    "app_display_name": null,
    "app_platform": null,
    "created_by_user_full_name": null,
    "created_by_user_username": null,
    "last_updated_by_user_full_name": null,
    "last_updated_by_user_username": null,
    "count_visitors": 813,
    "count_accounts": 400,
    "sum_clicks": 5648.058724278396,
    "count_click_events": 979,
    "first_click_at": null,
    "last_click_at": null,
    "avg_visitor_minutes": 5.255233105554051,
    "avg_visitor_events": 16.77966460074008
  },
  {
    "feature_id": "FEAT_00002",
    "app_id": "MAIN_APP_001",
    "created_at": "2025-04-08T13:36:06.740354",
    "created_by_user_id": null,
    "is_dirty": null,
    "group_id": null,
    "is_core_event": 1,
    "last_updated_at": null,
    "last_updated_by_user_id": null,
    "feature_name": "Password Reset",
    "page_id": null,
    "root_version_id": null,
    "stable_version_id": null,
    "valid_through": null,
    "product_area_name": "User Management",
    "page_name": null,
    "page_created_at": null,
    "page_valid_through": null,
    "app_display_name": null,
    "app_platform": null,
    "created_by_user_full_name": null,
    "created_by_user_username": null,
    "last_updated_by_user_full_name": null,
    "last_updated_by_user_username": null,
    "count_visitors": 276,
    "count_accounts": 279,
    "sum_clicks": 4318.94271950387,
    "count_click_events": 340,
    "first_click_at": null,
    "last_click_at": null,
    "avg_visitor_minutes": 19.04782768747688,
    "avg_visitor_events": 17.457683427501834
  },
  {
    "feature_id": "FEAT_00003",
    "app_id": "MAIN_APP_001",
    "created_at": "2025-03-09T13:36:06.740360",
    "created_by_user_id": null,
    "is_dirty": null,
    "group_id": null,
    "is_core_event": 1,
    "last_updated_at": null,
    "last_updated_by_user_id": null,
    "feature_name": "Two-Factor Auth",
    "page_id": null,
    "root_version_id": null,
    "stable_version_id": null,
    "valid_through": null,
    "product_area_name": "User Management",
    "page_name": null,
    "page_created_at": null,
    "page_valid_through": null,
    "app_display_name": null,
    "app_platform": null,
    "created_by_user_full_name": null,
    "created_by_user_username": null,
    "last_updated_by_user_full_name": null,
    "last_updated_by_user_username": null,
    "count_visitors": 164,
    "count_accounts": 29,
    "sum_clicks": 263.9695949676853,
    "count_click_events": 247,
    "first_click_at": null,
    "last_click_at": null,
    "avg_visitor_minutes": 14.305622809870709,
    "avg_visitor_events": 17.068631905281578
  }
]
```


## pendo__feature_daily_metrics

- Rows: 16200

- Columns: date_day (TIMESTAMP), feature_id (TEXT), feature_name (TEXT), group_id (INTEGER), product_area_name (TEXT), page_id (TEXT), page_name (TEXT), sum_clicks (REAL), count_visitors (INTEGER), count_accounts (INTEGER), count_first_time_visitors (INTEGER), count_first_time_accounts (INTEGER), count_return_visitors (INTEGER), count_return_accounts (INTEGER), avg_daily_minutes_per_visitor (REAL), avg_daily_clicks_per_visitor (REAL), percent_of_daily_feature_clicks (REAL), percent_of_daily_feature_visitors (REAL), percent_of_daily_feature_accounts (REAL), count_click_events (INTEGER)

```json
[
  {
    "date_day": "2025-07-16 00:00:00",
    "feature_id": "FEAT_00001",
    "feature_name": "User Profile Edit",
    "group_id": null,
    "product_area_name": "User Management",
    "page_id": null,
    "page_name": null,
    "sum_clicks": 1969.7305691875113,
    "count_visitors": 339,
    "count_accounts": 165,
    "count_first_time_visitors": null,
    "count_first_time_accounts": null,
    "count_return_visitors": null,
    "count_return_accounts": null,
    "avg_daily_minutes_per_visitor": 6.46036014115336,
    "avg_daily_clicks_per_visitor": 2.953138770518113,
    "percent_of_daily_feature_clicks": null,
    "percent_of_daily_feature_visitors": null,
    "percent_of_daily_feature_accounts": null,
    "count_click_events": 340
  },
  {
    "date_day": "2025-07-17 00:00:00",
    "feature_id": "FEAT_00001",
    "feature_name": "User Profile Edit",
    "group_id": null,
    "product_area_name": "User Management",
    "page_id": null,
    "page_name": null,
    "sum_clicks": 2192.6725487320878,
    "count_visitors": 331,
    "count_accounts": 128,
    "count_first_time_visitors": null,
    "count_first_time_accounts": null,
    "count_return_visitors": null,
    "count_return_accounts": null,
    "avg_daily_minutes_per_visitor": 7.677097544905534,
    "avg_daily_clicks_per_visitor": 3.723989167994321,
    "percent_of_daily_feature_clicks": null,
    "percent_of_daily_feature_visitors": null,
    "percent_of_daily_feature_accounts": null,
    "count_click_events": 341
  },
  {
    "date_day": "2025-07-18 00:00:00",
    "feature_id": "FEAT_00001",
    "feature_name": "User Profile Edit",
    "group_id": null,
    "product_area_name": "User Management",
    "page_id": null,
    "page_name": null,
    "sum_clicks": 1053.9513357883231,
    "count_visitors": 407,
    "count_accounts": 201,
    "count_first_time_visitors": null,
    "count_first_time_accounts": null,
    "count_return_visitors": null,
    "count_return_accounts": null,
    "avg_daily_minutes_per_visitor": 2.3126188377808257,
    "avg_daily_clicks_per_visitor": 1.4045165405675524,
    "percent_of_daily_feature_clicks": null,
    "percent_of_daily_feature_visitors": null,
    "percent_of_daily_feature_accounts": null,
    "count_click_events": 432
  }
]
```


## pendo__product_adoption_analytics

- Rows: 180

- Columns: feature_id (TEXT), feature_name (TEXT), is_core_event (INTEGER), page_name (TEXT), app_id (TEXT), total_users_tried (INTEGER), avg_events_per_user (REAL), avg_minutes_per_user (REAL), avg_active_days_per_user (REAL), regular_users (INTEGER), casual_users (INTEGER), calculated_at (TIMESTAMP)

```json
[
  {
    "feature_id": "FEAT_00001",
    "feature_name": "User Profile Edit",
    "is_core_event": 1,
    "page_name": "User Profile Edit Page",
    "app_id": null,
    "total_users_tried": 550,
    "avg_events_per_user": 18.907812065530763,
    "avg_minutes_per_user": 7.213502734435224,
    "avg_active_days_per_user": 11.57651896891182,
    "regular_users": 425,
    "casual_users": 125,
    "calculated_at": "2025-10-14 13:36:18.217718+08:00"
  },
  {
    "feature_id": "FEAT_00002",
    "feature_name": "Password Reset",
    "is_core_event": 1,
    "page_name": "Password Reset Page",
    "app_id": null,
    "total_users_tried": 59,
    "avg_events_per_user": 3.339971712892824,
    "avg_minutes_per_user": 8.615512891286004,
    "avg_active_days_per_user": 9.6416674006954,
    "regular_users": 39,
    "casual_users": 20,
    "calculated_at": "2025-10-14 13:36:18.219085+08:00"
  },
  {
    "feature_id": "FEAT_00003",
    "feature_name": "Two-Factor Auth",
    "is_core_event": 1,
    "page_name": "Two-Factor Auth Page",
    "app_id": null,
    "total_users_tried": 734,
    "avg_events_per_user": 3.8135017978475707,
    "avg_minutes_per_user": 26.438513294162078,
    "avg_active_days_per_user": 8.265385039571225,
    "regular_users": 546,
    "casual_users": 188,
    "calculated_at": "2025-10-14 13:36:18.219442+08:00"
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
    "latest_nps_rating": null,
    "count_active_days": 6,
    "count_active_months": 6,
    "sum_minutes": 430.0,
    "sum_events": 139.0,
    "count_event_records": 6.0,
    "average_daily_minutes": 71.66666666666667,
    "average_daily_events": 23.166666666666668,
    "first_event_on": "2021-05-28 00:00:00",
    "last_event_on": "2024-07-17 00:00:00"
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
    "latest_nps_rating": null,
    "count_active_days": 10,
    "count_active_months": 9,
    "sum_minutes": 797.0,
    "sum_events": 282.0,
    "count_event_records": 10.0,
    "average_daily_minutes": 79.7,
    "average_daily_events": 28.2,
    "first_event_on": "2021-05-20 00:00:00",
    "last_event_on": "2024-08-20 00:00:00"
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
    "latest_nps_rating": null,
    "count_active_days": 8,
    "count_active_months": 8,
    "sum_minutes": 597.0,
    "sum_events": 226.0,
    "count_event_records": 8.0,
    "average_daily_minutes": 74.625,
    "average_daily_events": 28.25,
    "first_event_on": "2021-02-19 00:00:00",
    "last_event_on": "2024-08-06 00:00:00"
  }
]
```


## pendo__visitor_feature

- Rows: 14283

- Columns: visitor_id (TEXT), feature_id (TEXT), first_click_at (TEXT), last_click_at (TEXT), sum_clicks (REAL), sum_minutes (REAL), avg_daily_minutes (REAL), count_active_days (INTEGER), count_click_events (INTEGER)

```json
[
  {
    "visitor_id": "VIS10000007766",
    "feature_id": "FEAT_00114",
    "first_click_at": "2025-09-04T13:36:15.327344",
    "last_click_at": "2025-09-21T13:36:15.327348",
    "sum_clicks": 62.0,
    "sum_minutes": 109.37719261858933,
    "avg_daily_minutes": 4.051007134021827,
    "count_active_days": 27,
    "count_click_events": 71
  },
  {
    "visitor_id": "VIS10000007766",
    "feature_id": "FEAT_00071",
    "first_click_at": "2025-08-23T13:36:15.328279",
    "last_click_at": "2025-09-20T13:36:15.328283",
    "sum_clicks": 81.0,
    "sum_minutes": 166.82778958778658,
    "avg_daily_minutes": 3.8797160369252692,
    "count_active_days": 43,
    "count_click_events": 121
  },
  {
    "visitor_id": "VIS10000007766",
    "feature_id": "FEAT_00085",
    "first_click_at": "2025-09-03T13:36:15.328800",
    "last_click_at": "2025-09-29T13:36:15.328805",
    "sum_clicks": 140.0,
    "sum_minutes": 198.64343530653605,
    "avg_daily_minutes": 66.21447843551202,
    "count_active_days": 3,
    "count_click_events": 170
  }
]
```
