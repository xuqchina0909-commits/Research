# SQLite 数据摘要

文件: `dacomp-zh-097.sqlite`


## intercom__company_enhanced

- Rows: 2509

- Columns: company_id (TEXT), company_name (TEXT), website (TEXT), website_domain (TEXT), industry (TEXT), created_at (TIMESTAMP), updated_at (TIMESTAMP), user_count (INTEGER), session_count (INTEGER), monthly_spend (INTEGER), plan_id (TEXT), plan_name (TEXT), company_age_days (INTEGER), all_company_tags (TEXT)

```json
[
  {
    "company_id": "cfe7d62a053448df88927ccb",
    "company_name": "Catalyst Security Group",
    "website": "https://www.catalystsecuritygroup377.com",
    "website_domain": "catalystsecuritygroup377.com",
    "industry": "Retail",
    "created_at": "2020-05-08 11:00:00",
    "updated_at": "2024-06-20 16:00:00",
    "user_count": 154,
    "session_count": 4928,
    "monthly_spend": 5302,
    "plan_id": "growth",
    "plan_name": "Growth",
    "company_age_days": 1514,
    "all_company_tags": "tier:growth,segment:renewal,region:EMEA,lifecycle:stabilize,seat_bucket:seats:130_259,arr_bucket:arr:65k_110k"
  },
  {
    "company_id": "068a2271c48d440c9e1bb5c5",
    "company_name": "Momentum Retail Inc",
    "website": "https://www.momentumretailinc164.com",
    "website_domain": "momentumretailinc164.com",
    "industry": "Nonprofit",
    "created_at": "2019-12-17 14:00:00",
    "updated_at": "2024-06-05 12:00:00",
    "user_count": 295,
    "session_count": 6785,
    "monthly_spend": 7915,
    "plan_id": "scale",
    "plan_name": "Scale",
    "company_age_days": 1657,
    "all_company_tags": "tier:scale,segment:new_contract,region:NA,lifecycle:adopt,seat_bucket:seats:260_419,arr_bucket:arr:65k_110k"
  },
  {
    "company_id": "3c422a7a45514c21a51dac64",
    "company_name": "Crimson Mobility LLC",
    "website": "https://www.crimsonmobilityllc700.com",
    "website_domain": "crimsonmobilityllc700.com",
    "industry": "Media",
    "created_at": "2019-09-04 10:00:00",
    "updated_at": "2024-06-25 15:00:00",
    "user_count": 315,
    "session_count": 7875,
    "monthly_spend": 9611,
    "plan_id": "scale",
    "plan_name": "Scale",
    "company_age_days": 1761,
    "all_company_tags": "tier:scale,segment:new_contract,region:NA,lifecycle:adopt,seat_bucket:seats:260_419,arr_bucket:arr:110k_200k"
  }
]
```


## intercom__company_metrics

- Rows: 2509

- Columns: company_id (TEXT), company_name (TEXT), website (TEXT), industry (TEXT), plan_id (TEXT), plan_name (TEXT), total_conversations (INTEGER), total_conversations_closed (INTEGER), avg_conversation_parts (REAL), avg_conversation_rating (REAL), contacts_total (INTEGER), conv_rate_overall (REAL), conv_rate_email (REAL), conv_rate_messenger (REAL), conv_rate_other (REAL), contacts_active_7d (INTEGER), contacts_active_30d (INTEGER), registration_retention_7d (REAL), registration_retention_30d (REAL), p50_time_to_first_response_min (REAL), p50_time_to_first_close_min (REAL), p50_time_to_last_close_min (REAL), p50_reopens (REAL), missing_days (INTEGER), is_date_continuous (INTEGER)

```json
[
  {
    "company_id": "cfe7d62a053448df88927ccb",
    "company_name": "Catalyst Security Group",
    "website": "https://www.catalystsecuritygroup377.com",
    "industry": "Retail",
    "plan_id": "growth",
    "plan_name": "Growth",
    "total_conversations": 96,
    "total_conversations_closed": 86,
    "avg_conversation_parts": 10.2,
    "avg_conversation_rating": 4.05,
    "contacts_total": 120,
    "conv_rate_overall": 0.5071204795204795,
    "conv_rate_email": 0.19363636363636363,
    "conv_rate_messenger": 0.37571428571428567,
    "conv_rate_other": 0.0776923076923077,
    "contacts_active_7d": 55,
    "contacts_active_30d": 85,
    "registration_retention_7d": 0.635,
    "registration_retention_30d": 0.568,
    "p50_time_to_first_response_min": 19.0,
    "p50_time_to_first_close_min": 378.0,
    "p50_time_to_last_close_min": 476.0,
    "p50_reopens": 1.0,
    "missing_days": 0,
    "is_date_continuous": 1
  },
  {
    "company_id": "068a2271c48d440c9e1bb5c5",
    "company_name": "Momentum Retail Inc",
    "website": "https://www.momentumretailinc164.com",
    "industry": "Nonprofit",
    "plan_id": "scale",
    "plan_name": "Scale",
    "total_conversations": 75,
    "total_conversations_closed": 66,
    "avg_conversation_parts": 7.8,
    "avg_conversation_rating": 4.0,
    "contacts_total": 223,
    "conv_rate_overall": 0.500608991008991,
    "conv_rate_email": 0.24818181818181817,
    "conv_rate_messenger": 0.31380952380952376,
    "conv_rate_other": 0.08923076923076924,
    "contacts_active_7d": 96,
    "contacts_active_30d": 174,
    "registration_retention_7d": 0.685,
    "registration_retention_30d": 0.563,
    "p50_time_to_first_response_min": 9.0,
    "p50_time_to_first_close_min": 185.0,
    "p50_time_to_last_close_min": 340.0,
    "p50_reopens": 0.7,
    "missing_days": 1,
    "is_date_continuous": 0
  },
  {
    "company_id": "3c422a7a45514c21a51dac64",
    "company_name": "Crimson Mobility LLC",
    "website": "https://www.crimsonmobilityllc700.com",
    "industry": "Media",
    "plan_id": "scale",
    "plan_name": "Scale",
    "total_conversations": 71,
    "total_conversations_closed": 62,
    "avg_conversation_parts": 8.8,
    "avg_conversation_rating": 3.8,
    "contacts_total": 229,
    "conv_rate_overall": 0.4641654345654346,
    "conv_rate_email": 0.18454545454545454,
    "conv_rate_messenger": 0.2947619047619047,
    "conv_rate_other": 0.07384615384615385,
    "contacts_active_7d": 91,
    "contacts_active_30d": 150,
    "registration_retention_7d": 0.568,
    "registration_retention_30d": 0.48,
    "p50_time_to_first_response_min": 9.0,
    "p50_time_to_first_close_min": 201.0,
    "p50_time_to_last_close_min": 352.0,
    "p50_reopens": 0.9,
    "missing_days": 1,
    "is_date_continuous": 0
  }
]
```


## intercom__contact_enhanced

- Rows: 2707

- Columns: contact_id (TEXT), admin_id (TEXT), created_at (TIMESTAMP), updated_at (TIMESTAMP), signed_up_at (TIMESTAMP), contact_name (TEXT), contact_role (TEXT), contact_email (TEXT), email_domain (TEXT), last_replied_ts (TIMESTAMP), last_email_clicked_ts (TIMESTAMP), last_email_opened_ts (TIMESTAMP), last_contacted_ts (TIMESTAMP), last_activity_ts (TIMESTAMP), is_active_1d (INTEGER), is_active_7d (INTEGER), is_active_30d (INTEGER), retained_7d (INTEGER), retained_30d (INTEGER), is_unsubscribed_from_emails (TEXT), all_contact_tags (TEXT), all_contact_company_names (TEXT)

```json
[
  {
    "contact_id": "7ed2cfe3b143491c918a6757",
    "admin_id": "adm-003",
    "created_at": "2020-01-15 15:00:00",
    "updated_at": "2024-06-22 17:00:00",
    "signed_up_at": "2020-01-15 19:00:00",
    "contact_name": "Jade Valdez",
    "contact_role": "customer_success",
    "contact_email": "jade.valdez@lighthousesecurityltd532.com",
    "email_domain": "lighthousesecurityltd532.com",
    "last_replied_ts": "2024-06-21 12:10:00",
    "last_email_clicked_ts": "2024-06-21 09:00:00",
    "last_email_opened_ts": "2024-06-21 10:00:00",
    "last_contacted_ts": "2024-06-21 11:00:00",
    "last_activity_ts": "2024-06-21 13:00:00",
    "is_active_1d": 0,
    "is_active_7d": 0,
    "is_active_30d": 1,
    "retained_7d": 0,
    "retained_30d": 1,
    "is_unsubscribed_from_emails": "false",
    "all_contact_tags": "role:customer_success,persona:ops_builder,segment:new_contract,region:NA,lifecycle:adopt,playbook:sales_led,status:active",
    "all_contact_company_names": "Lighthouse Security Ltd"
  },
  {
    "contact_id": "950921bc2c65477497dc3153",
    "admin_id": "adm-055",
    "created_at": "2022-01-08 13:00:00",
    "updated_at": "2024-06-15 15:00:00",
    "signed_up_at": "2022-01-08 17:00:00",
    "contact_name": "Layla Zimmerman",
    "contact_role": "technical_owner",
    "contact_email": "layla.zimmerman@pioneerretailltd774.com",
    "email_domain": "pioneerretailltd774.com",
    "last_replied_ts": "2024-06-07 11:10:00",
    "last_email_clicked_ts": "2024-06-07 08:00:00",
    "last_email_opened_ts": "2024-06-07 09:00:00",
    "last_contacted_ts": "2024-06-07 10:00:00",
    "last_activity_ts": "2024-06-07 12:00:00",
    "is_active_1d": 0,
    "is_active_7d": 0,
    "is_active_30d": 1,
    "retained_7d": 0,
    "retained_30d": 1,
    "is_unsubscribed_from_emails": "false",
    "all_contact_tags": "role:technical_owner,persona:support_agent,segment:expansion,region:APAC,lifecycle:scale,playbook:hybrid,status:active",
    "all_contact_company_names": "Pioneer Retail Ltd"
  },
  {
    "contact_id": "130bd4f8234141cb851b0c30",
    "admin_id": "adm-008",
    "created_at": "2018-07-24 09:00:00",
    "updated_at": "2024-06-28 13:20:00",
    "signed_up_at": "2018-07-24 13:00:00",
    "contact_name": "Isaac Diaz",
    "contact_role": "finance_manager",
    "contact_email": "isaac.diaz@pioneernetworksinc297.com",
    "email_domain": "pioneernetworksinc297.com",
    "last_replied_ts": "2024-06-28 12:10:00",
    "last_email_clicked_ts": "2024-06-28 09:00:00",
    "last_email_opened_ts": "2024-06-28 10:00:00",
    "last_contacted_ts": "2024-06-28 11:00:00",
    "last_activity_ts": "2024-06-28 13:00:00",
    "is_active_1d": 0,
    "is_active_7d": 1,
    "is_active_30d": 1,
    "retained_7d": 1,
    "retained_30d": 1,
    "is_unsubscribed_from_emails": "false",
    "all_contact_tags": "role:finance_manager,persona:analyst,segment:renewal,region:EMEA,lifecycle:stabilize,playbook:product_led,status:active",
    "all_contact_company_names": "Pioneer Networks Inc"
  }
]
```


## intercom__conversation_enhanced

- Rows: 6703

- Columns: conversation_id (TEXT), conversation_created_at (TIMESTAMP), conversation_last_updated_at (TIMESTAMP), conversation_type (TEXT), conversation_initiated_type (TEXT), conversation_subject (TEXT), conversation_assignee_type (TEXT), conversation_author_type (TEXT), conversation_state (TEXT), is_read (TEXT), waiting_since (TIMESTAMP), snoozed_until (TIMESTAMP), sla_name (TEXT), sla_status (TEXT), conversation_rating (REAL), conversation_remark (TEXT), first_close_at (TIMESTAMP), last_close_at (TIMESTAMP), first_admin_close_at (TIMESTAMP), last_admin_close_at (TIMESTAMP), all_conversation_tags (TEXT), all_conversation_admins (TEXT), all_conversation_contacts (TEXT), first_close_by_admin_id (TEXT), last_close_by_admin_id (TEXT), first_close_by_author_id (TEXT), last_close_by_author_id (TEXT), first_contact_author_id (TEXT), last_contact_author_id (TEXT), all_contact_company_names (TEXT)

```json
[
  {
    "conversation_id": "156643300003288",
    "conversation_created_at": "2024-02-12 09:56:00",
    "conversation_last_updated_at": "2024-02-12 13:48:00",
    "conversation_type": "email_thread",
    "conversation_initiated_type": "contact_inbound",
    "conversation_subject": "Billing adjustment follow-up - Summit Retail Inc",
    "conversation_assignee_type": "team",
    "conversation_author_type": "contact",
    "conversation_state": "closed",
    "is_read": "true",
    "waiting_since": "2024-02-12 10:18:00",
    "snoozed_until": "2024-02-12 13:28:00",
    "sla_name": "Premium Support",
    "sla_status": "breached",
    "conversation_rating": 4.25,
    "conversation_remark": "Shared cohort analysis and recommended usage goals for next month.",
    "first_close_at": "2024-02-12 13:28:00",
    "last_close_at": "2024-02-12 13:28:00",
    "first_admin_close_at": "2024-02-12 13:28:00",
    "last_admin_close_at": "2024-02-12 13:28:00",
    "all_conversation_tags": "topic:usage_insight|channel:email|segment:new_contract|first_response:human|tier:scale|sla:breached",
    "all_conversation_admins": "adm-013,adm-079",
    "all_conversation_contacts": "contact:f2ae16c5a78f4bfe89005185",
    "first_close_by_admin_id": "adm-013",
    "last_close_by_admin_id": "adm-079",
    "first_close_by_author_id": "adm-013",
    "last_close_by_author_id": "adm-079",
    "first_contact_author_id": "f2ae16c5a78f4bfe89005185",
    "last_contact_author_id": "f2ae16c5a78f4bfe89005185",
    "all_contact_company_names": "Summit Retail Inc"
  },
  {
    "conversation_id": "156643300007911",
    "conversation_created_at": "2024-04-12 07:46:00",
    "conversation_last_updated_at": "2024-04-12 11:19:00",
    "conversation_type": "user_inbox",
    "conversation_initiated_type": "contact_inbound",
    "conversation_subject": "Billing adjustment follow-up - Golden Ventures Group",
    "conversation_assignee_type": "team",
    "conversation_author_type": "contact",
    "conversation_state": "closed",
    "is_read": "true",
    "waiting_since": "2024-04-12 07:54:00",
    "snoozed_until": "2024-04-12 10:59:00",
    "sla_name": "Premium Support",
    "sla_status": "breached",
    "conversation_rating": 3.5,
    "conversation_remark": "Shared cohort analysis and recommended usage goals for next month.",
    "first_close_at": "2024-04-12 10:59:00",
    "last_close_at": "2024-04-12 10:59:00",
    "first_admin_close_at": "2024-04-12 10:59:00",
    "last_admin_close_at": "2024-04-12 10:59:00",
    "all_conversation_tags": "topic:usage_insight|channel:messenger|segment:churn_watch|first_response:human|tier:enterprise|sla:breached",
    "all_conversation_admins": "adm-073,adm-099",
    "all_conversation_contacts": "contact:b72147176a004bedbc5406a7",
    "first_close_by_admin_id": "adm-073",
    "last_close_by_admin_id": "adm-099",
    "first_close_by_author_id": "adm-073",
    "last_close_by_author_id": "adm-099",
    "first_contact_author_id": "b72147176a004bedbc5406a7",
    "last_contact_author_id": "b72147176a004bedbc5406a7",
    "all_contact_company_names": "Golden Ventures Group"
  },
  {
    "conversation_id": "156643300010660",
    "conversation_created_at": "2024-02-22 09:56:00",
    "conversation_last_updated_at": "2024-02-22 18:12:00",
    "conversation_type": "email_thread",
    "conversation_initiated_type": "contact_inbound",
    "conversation_subject": "Billing adjustment follow-up - Cascade Ventures LLC",
    "conversation_assignee_type": "team",
    "conversation_author_type": "contact",
    "conversation_state": "closed",
    "is_read": "true",
    "waiting_since": "2024-02-22 10:16:00",
    "snoozed_until": "2024-02-22 12:02:00",
    "sla_name": "Premium Support",
    "sla_status": "warning",
    "conversation_rating": 3.89,
    "conversation_remark": "Shared cohort analysis and recommended usage goals for next month.",
    "first_close_at": "2024-02-22 11:32:00",
    "last_close_at": "2024-02-22 17:52:00",
    "first_admin_close_at": "2024-02-22 11:32:00",
    "last_admin_close_at": "2024-02-22 17:52:00",
    "all_conversation_tags": "topic:usage_insight|channel:email|segment:churn_watch|first_response:human|tier:enterprise|sla:warning",
    "all_conversation_admins": "adm-103,adm-049",
    "all_conversation_contacts": "contact:2743c100a77f48bab339e1b5",
    "first_close_by_admin_id": "adm-103",
    "last_close_by_admin_id": "adm-049",
    "first_close_by_author_id": "adm-103",
    "last_close_by_author_id": "adm-049",
    "first_contact_author_id": "2743c100a77f48bab339e1b5",
    "last_contact_author_id": "2743c100a77f48bab339e1b5",
    "all_contact_company_names": "Cascade Ventures LLC"
  }
]
```


## intercom__conversation_metrics

- Rows: 6703

- Columns: conversation_id (TEXT), conversation_created_at (TIMESTAMP), conversation_last_updated_at (TIMESTAMP), conversation_type (TEXT), conversation_initiated_type (TEXT), conversation_subject (TEXT), conversation_assignee_type (TEXT), conversation_author_type (TEXT), conversation_state (TEXT), is_read (TEXT), waiting_since (TIMESTAMP), snoozed_until (TIMESTAMP), sla_name (TEXT), sla_status (TEXT), conversation_rating (REAL), conversation_rating_remark (TEXT), count_reopens (INTEGER), count_total_parts (INTEGER), count_assignments (INTEGER), first_contact_reply_at (TIMESTAMP), first_assignment_at (TIMESTAMP), time_to_first_assignment_minutes (REAL), first_admin_response_at (TIMESTAMP), time_to_first_response_minutes (REAL), time_to_admin_first_close_minutes (REAL), time_to_first_close_minutes (REAL), first_reopen_at (TIMESTAMP), last_assignment_at (TIMESTAMP), time_to_last_assignment_minutes (REAL), last_contact_reply_at (TIMESTAMP), last_admin_response_at (TIMESTAMP), last_reopen_at (TIMESTAMP), time_to_admin_last_close_minutes (REAL), time_to_last_close_minutes (REAL), first_close_by_admin_id (TEXT), last_close_by_admin_id (TEXT), first_close_by_author_id (TEXT), last_close_by_author_id (TEXT), first_contact_author_id (TEXT), last_contact_author_id (TEXT)

```json
[
  {
    "conversation_id": "156643300003288",
    "conversation_created_at": "2024-02-12 09:56:00",
    "conversation_last_updated_at": "2024-02-12 13:48:00",
    "conversation_type": "email_thread",
    "conversation_initiated_type": "contact_inbound",
    "conversation_subject": "Billing adjustment follow-up - Summit Retail Inc",
    "conversation_assignee_type": "team",
    "conversation_author_type": "contact",
    "conversation_state": "closed",
    "is_read": "true",
    "waiting_since": "2024-02-12 10:18:00",
    "snoozed_until": "2024-02-12 13:28:00",
    "sla_name": "Premium Support",
    "sla_status": "breached",
    "conversation_rating": 4.25,
    "conversation_rating_remark": "CSAT positive",
    "count_reopens": 0,
    "count_total_parts": 22,
    "count_assignments": 3,
    "first_contact_reply_at": "2024-02-12 10:18:00",
    "first_assignment_at": "2024-02-12 10:06:00",
    "time_to_first_assignment_minutes": 10.0,
    "first_admin_response_at": "2024-02-12 10:20:00",
    "time_to_first_response_minutes": 24.0,
    "time_to_admin_first_close_minutes": 188.0,
    "time_to_first_close_minutes": 212.0,
    "first_reopen_at": "2024-02-12 13:28:00",
    "last_assignment_at": "2024-02-12 11:06:00",
    "time_to_last_assignment_minutes": 70.0,
    "last_contact_reply_at": "2024-02-12 10:54:00",
    "last_admin_response_at": "2024-02-12 11:02:00",
    "last_reopen_at": "2024-02-12 13:28:00",
    "time_to_admin_last_close_minutes": 188.0,
    "time_to_last_close_minutes": 212.0,
    "first_close_by_admin_id": "adm-013",
    "last_close_by_admin_id": "adm-079",
    "first_close_by_author_id": "adm-013",
    "last_close_by_author_id": "adm-079",
    "first_contact_author_id": "f2ae16c5a78f4bfe89005185",
    "last_contact_author_id": "f2ae16c5a78f4bfe89005185"
  },
  {
    "conversation_id": "156643300007911",
    "conversation_created_at": "2024-04-12 07:46:00",
    "conversation_last_updated_at": "2024-04-12 11:19:00",
    "conversation_type": "user_inbox",
    "conversation_initiated_type": "contact_inbound",
    "conversation_subject": "Billing adjustment follow-up - Golden Ventures Group",
    "conversation_assignee_type": "team",
    "conversation_author_type": "contact",
    "conversation_state": "closed",
    "is_read": "true",
    "waiting_since": "2024-04-12 07:54:00",
    "snoozed_until": "2024-04-12 10:59:00",
    "sla_name": "Premium Support",
    "sla_status": "breached",
    "conversation_rating": 3.5,
    "conversation_rating_remark": "Follow-up scheduled",
    "count_reopens": 0,
    "count_total_parts": 15,
    "count_assignments": 2,
    "first_contact_reply_at": "2024-04-12 07:54:00",
    "first_assignment_at": "2024-04-12 07:52:00",
    "time_to_first_assignment_minutes": 6.0,
    "first_admin_response_at": "2024-04-12 08:11:00",
    "time_to_first_response_minutes": 25.0,
    "time_to_admin_first_close_minutes": 168.0,
    "time_to_first_close_minutes": 193.0,
    "first_reopen_at": "2024-04-12 10:59:00",
    "last_assignment_at": "2024-04-12 08:31:00",
    "time_to_last_assignment_minutes": 45.0,
    "last_contact_reply_at": "2024-04-12 08:26:00",
    "last_admin_response_at": "2024-04-12 08:31:00",
    "last_reopen_at": "2024-04-12 10:59:00",
    "time_to_admin_last_close_minutes": 168.0,
    "time_to_last_close_minutes": 193.0,
    "first_close_by_admin_id": "adm-073",
    "last_close_by_admin_id": "adm-099",
    "first_close_by_author_id": "adm-073",
    "last_close_by_author_id": "adm-099",
    "first_contact_author_id": "b72147176a004bedbc5406a7",
    "last_contact_author_id": "b72147176a004bedbc5406a7"
  },
  {
    "conversation_id": "156643300010660",
    "conversation_created_at": "2024-02-22 09:56:00",
    "conversation_last_updated_at": "2024-02-22 18:12:00",
    "conversation_type": "email_thread",
    "conversation_initiated_type": "contact_inbound",
    "conversation_subject": "Billing adjustment follow-up - Cascade Ventures LLC",
    "conversation_assignee_type": "team",
    "conversation_author_type": "contact",
    "conversation_state": "closed",
    "is_read": "true",
    "waiting_since": "2024-02-22 10:16:00",
    "snoozed_until": "2024-02-22 12:02:00",
    "sla_name": "Premium Support",
    "sla_status": "warning",
    "conversation_rating": 3.89,
    "conversation_rating_remark": "Follow-up scheduled",
    "count_reopens": 2,
    "count_total_parts": 22,
    "count_assignments": 3,
    "first_contact_reply_at": "2024-02-22 10:16:00",
    "first_assignment_at": "2024-02-22 10:00:00",
    "time_to_first_assignment_minutes": 4.0,
    "first_admin_response_at": "2024-02-22 10:14:00",
    "time_to_first_response_minutes": 18.0,
    "time_to_admin_first_close_minutes": 78.0,
    "time_to_first_close_minutes": 96.0,
    "first_reopen_at": "2024-02-22 12:17:00",
    "last_assignment_at": "2024-02-22 11:00:00",
    "time_to_last_assignment_minutes": 64.0,
    "last_contact_reply_at": "2024-02-22 10:52:00",
    "last_admin_response_at": "2024-02-22 11:02:00",
    "last_reopen_at": "2024-02-22 15:27:00",
    "time_to_admin_last_close_minutes": 458.0,
    "time_to_last_close_minutes": 476.0,
    "first_close_by_admin_id": "adm-103",
    "last_close_by_admin_id": "adm-049",
    "first_close_by_author_id": "adm-103",
    "last_close_by_author_id": "adm-049",
    "first_contact_author_id": "2743c100a77f48bab339e1b5",
    "last_contact_author_id": "2743c100a77f48bab339e1b5"
  }
]
```
