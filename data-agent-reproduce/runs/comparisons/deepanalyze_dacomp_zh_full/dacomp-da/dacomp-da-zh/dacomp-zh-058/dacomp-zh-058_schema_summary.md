# SQLite 数据摘要

文件: `dacomp-zh-058.sqlite`


## ad_groups

- Rows: 58

- Columns: ad_group_id (INTEGER), campaign_id (INTEGER), ad_group_name (TEXT), status (TEXT)

```json
[
  {
    "ad_group_id": 1,
    "campaign_id": 150,
    "ad_group_name": "Ad Group 1",
    "status": "ENABLED"
  },
  {
    "ad_group_id": 2,
    "campaign_id": 150,
    "ad_group_name": "Ad Group 2",
    "status": "ENABLED"
  },
  {
    "ad_group_id": 3,
    "campaign_id": 150,
    "ad_group_name": "Ad Group 3",
    "status": "ENABLED"
  }
]
```


## campaigns

- Rows: 200

- Columns: campaign_id (INTEGER), campaign_name (TEXT), campaign_type (TEXT), bidding_strategy (TEXT), industry (TEXT), status (TEXT), start_date (TIMESTAMP), budget_daily (REAL)

```json
[
  {
    "campaign_id": 1,
    "campaign_name": "SaaS - Search Campaign 1",
    "campaign_type": "Search",
    "bidding_strategy": "Maximize Conversions",
    "industry": "SaaS",
    "status": "ENABLED",
    "start_date": "2023-02-05 00:00:00",
    "budget_daily": 1486.12
  },
  {
    "campaign_id": 2,
    "campaign_name": "SaaS - Performance Max Campaign 2",
    "campaign_type": "Performance Max",
    "bidding_strategy": "Manual CPC",
    "industry": "SaaS",
    "status": "ENABLED",
    "start_date": "2023-01-03 00:00:00",
    "budget_daily": 476.34
  },
  {
    "campaign_id": 3,
    "campaign_name": "E-commerce - Performance Max Campaign 3",
    "campaign_type": "Performance Max",
    "bidding_strategy": "Target ROAS",
    "industry": "E-commerce",
    "status": "PAUSED",
    "start_date": "2023-02-15 00:00:00",
    "budget_daily": 1199.07
  }
]
```


## google_ads__campaign_report

- Rows: 714

- Columns: year_month (TEXT), campaign_id (INTEGER), campaign_name (TEXT), campaign_type (TEXT), bidding_strategy (TEXT), industry (TEXT), impressions (INTEGER), clicks (INTEGER), cost (REAL), conversions (REAL), conversion_value (REAL), ctr (REAL), cpc (REAL), conversion_rate (REAL), cost_per_conversion (REAL), roas (REAL), quality_score (REAL), impression_share (REAL)

```json
[
  {
    "year_month": "2023-05",
    "campaign_id": 150,
    "campaign_name": "Education - Video Campaign 150",
    "campaign_type": "Video",
    "bidding_strategy": "Maximize Conversions",
    "industry": "Education",
    "impressions": 4378105,
    "clicks": 35668,
    "cost": 30055.05,
    "conversions": 269.34,
    "conversion_value": 172077.1,
    "ctr": 0.0081,
    "cpc": 0.84,
    "conversion_rate": 0.0076,
    "cost_per_conversion": 111.59,
    "roas": 5.73,
    "quality_score": 6.1,
    "impression_share": 0.875
  },
  {
    "year_month": "2023-06",
    "campaign_id": 150,
    "campaign_name": "Education - Video Campaign 150",
    "campaign_type": "Video",
    "bidding_strategy": "Maximize Conversions",
    "industry": "Education",
    "impressions": 9412876,
    "clicks": 57357,
    "cost": 39419.6,
    "conversions": 461.59,
    "conversion_value": 94588.7,
    "ctr": 0.0061,
    "cpc": 0.69,
    "conversion_rate": 0.008,
    "cost_per_conversion": 85.4,
    "roas": 2.4,
    "quality_score": 4.9,
    "impression_share": 0.755
  },
  {
    "year_month": "2023-07",
    "campaign_id": 150,
    "campaign_name": "Education - Video Campaign 150",
    "campaign_type": "Video",
    "bidding_strategy": "Maximize Conversions",
    "industry": "Education",
    "impressions": 3692295,
    "clicks": 31806,
    "cost": 30038.16,
    "conversions": 308.89,
    "conversion_value": 150086.42,
    "ctr": 0.0086,
    "cpc": 0.94,
    "conversion_rate": 0.0097,
    "cost_per_conversion": 97.25,
    "roas": 5.0,
    "quality_score": 7.5,
    "impression_share": 0.709
  }
]
```


## google_ads__device_report

- Rows: 2142

- Columns: year_month (TEXT), campaign_id (INTEGER), device_type (TEXT), impressions (INTEGER), clicks (INTEGER), cost (REAL), conversions (REAL), conversion_value (REAL), ctr (REAL), cpc (REAL), conversion_rate (REAL), cost_per_conversion (REAL), roas (REAL), quality_score (REAL), impression_share (REAL)

```json
[
  {
    "year_month": "2023-05",
    "campaign_id": 150,
    "device_type": "Desktop",
    "impressions": 1298570,
    "clicks": 13085,
    "cost": 11243.33,
    "conversions": 175.96,
    "conversion_value": 19872.41,
    "ctr": 0.0091,
    "cpc": 0.86,
    "conversion_rate": 0.0174,
    "cost_per_conversion": 63.9,
    "roas": 1.77,
    "quality_score": 6.1,
    "impression_share": 0.321
  },
  {
    "year_month": "2023-06",
    "campaign_id": 150,
    "device_type": "Desktop",
    "impressions": 2057371,
    "clicks": 15474,
    "cost": 11558.15,
    "conversions": 161.77,
    "conversion_value": 101306.47,
    "ctr": 0.0067,
    "cpc": 0.75,
    "conversion_rate": 0.0137,
    "cost_per_conversion": 71.45,
    "roas": 8.76,
    "quality_score": 6.3,
    "impression_share": 0.406
  },
  {
    "year_month": "2023-07",
    "campaign_id": 150,
    "device_type": "Desktop",
    "impressions": 1748725,
    "clicks": 11103,
    "cost": 8808.65,
    "conversions": 109.99,
    "conversion_value": 74063.73,
    "ctr": 0.0057,
    "cpc": 0.79,
    "conversion_rate": 0.0129,
    "cost_per_conversion": 80.09,
    "roas": 8.41,
    "quality_score": 8.3,
    "impression_share": 0.89
  }
]
```


## google_ads__geo_report

- Rows: 2550

- Columns: year_month (TEXT), campaign_id (INTEGER), geo_target (TEXT), impressions (INTEGER), clicks (INTEGER), cost (REAL), conversions (REAL), conversion_value (REAL), ctr (REAL), cpc (REAL), conversion_rate (REAL), cost_per_conversion (REAL), roas (REAL), quality_score (REAL), impression_share (REAL)

```json
[
  {
    "year_month": "2023-05",
    "campaign_id": 150,
    "geo_target": "France",
    "impressions": 1088057,
    "clicks": 7725,
    "cost": 6009.31,
    "conversions": 70.4,
    "conversion_value": 44358.2,
    "ctr": 0.0071,
    "cpc": 0.78,
    "conversion_rate": 0.0091,
    "cost_per_conversion": 85.36,
    "roas": 7.38,
    "quality_score": 7.4,
    "impression_share": 0.594
  },
  {
    "year_month": "2023-06",
    "campaign_id": 150,
    "geo_target": "France",
    "impressions": 943747,
    "clicks": 7832,
    "cost": 6190.01,
    "conversions": 56.79,
    "conversion_value": 6822.22,
    "ctr": 0.0083,
    "cpc": 0.79,
    "conversion_rate": 0.0073,
    "cost_per_conversion": 109.0,
    "roas": 1.1,
    "quality_score": 5.6,
    "impression_share": 0.655
  },
  {
    "year_month": "2023-07",
    "campaign_id": 150,
    "geo_target": "France",
    "impressions": 972678,
    "clicks": 6775,
    "cost": 5998.51,
    "conversions": 43.98,
    "conversion_value": 22215.78,
    "ctr": 0.007,
    "cpc": 0.89,
    "conversion_rate": 0.0065,
    "cost_per_conversion": 136.39,
    "roas": 3.7,
    "quality_score": 4.8,
    "impression_share": 0.52
  }
]
```


## google_ads__keyword_report

- Rows: 1303

- Columns: year_quarter (TEXT), keyword_id (INTEGER), ad_group_id (INTEGER), campaign_id (INTEGER), keyword_text (TEXT), match_type (TEXT), impressions (INTEGER), clicks (INTEGER), cost (REAL), conversions (REAL), conversion_value (REAL), ctr (REAL), cpc (REAL), conversion_rate (REAL), cost_per_conversion (REAL), roas (REAL), quality_score (REAL), impression_share (REAL), avg_position (REAL)

```json
[
  {
    "year_quarter": "2023-Q2",
    "keyword_id": 1,
    "ad_group_id": 1,
    "campaign_id": 150,
    "keyword_text": "learning platform",
    "match_type": "PHRASE",
    "impressions": 169925,
    "clicks": 1173,
    "cost": 1044.76,
    "conversions": 14.86,
    "conversion_value": 2555.22,
    "ctr": 0.0069,
    "cpc": 0.89,
    "conversion_rate": 0.0127,
    "cost_per_conversion": 70.31,
    "roas": 2.45,
    "quality_score": 4.1,
    "impression_share": 0.492,
    "avg_position": 3.0
  },
  {
    "year_quarter": "2023-Q3",
    "keyword_id": 1,
    "ad_group_id": 1,
    "campaign_id": 150,
    "keyword_text": "learning platform",
    "match_type": "PHRASE",
    "impressions": 98677,
    "clicks": 899,
    "cost": 800.43,
    "conversions": 6.91,
    "conversion_value": 3413.5,
    "ctr": 0.0091,
    "cpc": 0.89,
    "conversion_rate": 0.0077,
    "cost_per_conversion": 115.84,
    "roas": 4.26,
    "quality_score": 9.6,
    "impression_share": 0.329,
    "avg_position": 2.4
  },
  {
    "year_quarter": "2023-Q4",
    "keyword_id": 1,
    "ad_group_id": 1,
    "campaign_id": 150,
    "keyword_text": "learning platform",
    "match_type": "PHRASE",
    "impressions": 133696,
    "clicks": 1188,
    "cost": 1084.68,
    "conversions": 12.66,
    "conversion_value": 8752.81,
    "ctr": 0.0089,
    "cpc": 0.91,
    "conversion_rate": 0.0107,
    "cost_per_conversion": 85.68,
    "roas": 8.07,
    "quality_score": 5.4,
    "impression_share": 0.463,
    "avg_position": 3.2
  }
]
```


## keywords

- Rows: 252

- Columns: keyword_id (INTEGER), ad_group_id (INTEGER), campaign_id (INTEGER), keyword_text (TEXT), match_type (TEXT), status (TEXT)

```json
[
  {
    "keyword_id": 1,
    "ad_group_id": 1,
    "campaign_id": 150,
    "keyword_text": "learning platform",
    "match_type": "PHRASE",
    "status": "ENABLED"
  },
  {
    "keyword_id": 2,
    "ad_group_id": 1,
    "campaign_id": 150,
    "keyword_text": "learning platform",
    "match_type": "BROAD",
    "status": "ENABLED"
  },
  {
    "keyword_id": 3,
    "ad_group_id": 1,
    "campaign_id": 150,
    "keyword_text": "learning platform",
    "match_type": "EXACT",
    "status": "ENABLED"
  }
]
```
