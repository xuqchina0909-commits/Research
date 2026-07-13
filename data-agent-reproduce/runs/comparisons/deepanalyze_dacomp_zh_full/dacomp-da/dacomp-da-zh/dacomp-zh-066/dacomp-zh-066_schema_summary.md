# SQLite 数据摘要

文件: `dacomp-zh-066.sqlite`


## greenhouse__job_enhanced

- Rows: 191

- Columns: job_id (INTEGER), name (TEXT), status (TEXT), requisition_id (INTEGER), created_at (TIMESTAMP), departments (TEXT), offices (TEXT), hiring_managers (TEXT), recruiters (TEXT), sourcers (TEXT), count_total_applications (INTEGER), count_active_applications (INTEGER), count_hired_applications (INTEGER), count_rejected_applications (INTEGER), count_prospect_applications (INTEGER), count_total_interviews (INTEGER), count_completed_interviews (INTEGER), avg_interviews_per_application (REAL), avg_job_rating (REAL), count_rated_applications (INTEGER), rating_completion_rate (REAL), application_to_interview_rate (REAL), interview_to_hire_rate (REAL), overall_conversion_rate (REAL), created_year (INTEGER), created_month (INTEGER), days_since_created (REAL)

```json
[
  {
    "job_id": 1,
    "name": "Frontend Engineer - and Sons",
    "status": "open",
    "requisition_id": 20001,
    "created_at": "2024-07-04 00:00:00",
    "departments": "Engineering",
    "offices": "San Francisco Office",
    "hiring_managers": "Lisa Wang",
    "recruiters": "Lisa Rodriguez, David Kim",
    "sourcers": "External Recruiter",
    "count_total_applications": 90,
    "count_active_applications": 2,
    "count_hired_applications": 22,
    "count_rejected_applications": 63,
    "count_prospect_applications": 2,
    "count_total_interviews": 31,
    "count_completed_interviews": 24,
    "avg_interviews_per_application": 0.34,
    "avg_job_rating": 4.24,
    "count_rated_applications": 71,
    "rating_completion_rate": 8.9,
    "application_to_interview_rate": 34.44,
    "interview_to_hire_rate": 70.97,
    "overall_conversion_rate": 24.44,
    "created_year": 2024,
    "created_month": 7,
    "days_since_created": 180.0
  },
  {
    "job_id": 2,
    "name": "Frontend Engineer - Ltd",
    "status": "open",
    "requisition_id": 20002,
    "created_at": "2024-07-04 00:00:00",
    "departments": "Engineering",
    "offices": "New York Office",
    "hiring_managers": "David Thompson",
    "recruiters": "Lisa Rodriguez, Sarah Johnson",
    "sourcers": null,
    "count_total_applications": 96,
    "count_active_applications": 5,
    "count_hired_applications": 15,
    "count_rejected_applications": 81,
    "count_prospect_applications": 0,
    "count_total_interviews": 21,
    "count_completed_interviews": 18,
    "avg_interviews_per_application": 0.22,
    "avg_job_rating": 4.5,
    "count_rated_applications": 72,
    "rating_completion_rate": 6.4,
    "application_to_interview_rate": 21.88,
    "interview_to_hire_rate": 71.43,
    "overall_conversion_rate": 15.62,
    "created_year": 2024,
    "created_month": 7,
    "days_since_created": 180.0
  },
  {
    "job_id": 3,
    "name": "Frontend Engineer - LLC",
    "status": "open",
    "requisition_id": 20003,
    "created_at": "2024-07-04 00:00:00",
    "departments": "Engineering",
    "offices": "New York Office",
    "hiring_managers": "Mike Rodriguez",
    "recruiters": "Mike Chen, Sarah Johnson",
    "sourcers": "External Recruiter",
    "count_total_applications": 103,
    "count_active_applications": 2,
    "count_hired_applications": 19,
    "count_rejected_applications": 83,
    "count_prospect_applications": 5,
    "count_total_interviews": 24,
    "count_completed_interviews": 23,
    "avg_interviews_per_application": 0.23,
    "avg_job_rating": 3.5,
    "count_rated_applications": 73,
    "rating_completion_rate": 7.7,
    "application_to_interview_rate": 23.3,
    "interview_to_hire_rate": 79.17,
    "overall_conversion_rate": 18.45,
    "created_year": 2024,
    "created_month": 7,
    "days_since_created": 180.0
  }
]
```


## greenhouse__recruitment_performance

- Rows: 191

- Columns: job_id (INTEGER), job_title (TEXT), job_status (TEXT), job_created_at (TIMESTAMP), application_year (INTEGER), application_quarter (INTEGER), total_applications (INTEGER), unique_candidates (INTEGER), hired_count (INTEGER), active_count (INTEGER), rejected_count (INTEGER), avg_process_days (REAL), total_interviews (INTEGER), completed_interviews (INTEGER), total_scorecards (INTEGER), avg_interview_score (REAL), hire_rate (REAL), interview_rate (REAL), interview_to_hire_rate (REAL), interview_completion_rate (REAL), performance_tier (TEXT), is_fast_process (INTEGER), has_good_interview_quality (INTEGER)

```json
[
  {
    "job_id": 1,
    "job_title": "Frontend Engineer - and Sons",
    "job_status": "open",
    "job_created_at": "2024-07-04 00:00:00",
    "application_year": 2024,
    "application_quarter": 3,
    "total_applications": 90,
    "unique_candidates": 76,
    "hired_count": 22,
    "active_count": 2,
    "rejected_count": 63,
    "avg_process_days": 17.68,
    "total_interviews": 31,
    "completed_interviews": 24,
    "total_scorecards": 23,
    "avg_interview_score": 3.3,
    "hire_rate": 24.44,
    "interview_rate": 34.44,
    "interview_to_hire_rate": 70.97,
    "interview_completion_rate": 77.42,
    "performance_tier": "High",
    "is_fast_process": 0,
    "has_good_interview_quality": 1
  },
  {
    "job_id": 2,
    "job_title": "Frontend Engineer - Ltd",
    "job_status": "open",
    "job_created_at": "2024-07-04 00:00:00",
    "application_year": 2024,
    "application_quarter": 3,
    "total_applications": 96,
    "unique_candidates": 87,
    "hired_count": 15,
    "active_count": 5,
    "rejected_count": 81,
    "avg_process_days": 40.32,
    "total_interviews": 21,
    "completed_interviews": 18,
    "total_scorecards": 16,
    "avg_interview_score": 3.44,
    "hire_rate": 15.62,
    "interview_rate": 21.88,
    "interview_to_hire_rate": 71.43,
    "interview_completion_rate": 85.71,
    "performance_tier": "Low",
    "is_fast_process": 0,
    "has_good_interview_quality": 1
  },
  {
    "job_id": 3,
    "job_title": "Frontend Engineer - LLC",
    "job_status": "open",
    "job_created_at": "2024-07-04 00:00:00",
    "application_year": 2024,
    "application_quarter": 3,
    "total_applications": 103,
    "unique_candidates": 89,
    "hired_count": 19,
    "active_count": 2,
    "rejected_count": 83,
    "avg_process_days": 23.83,
    "total_interviews": 24,
    "completed_interviews": 23,
    "total_scorecards": 23,
    "avg_interview_score": 3.07,
    "hire_rate": 18.45,
    "interview_rate": 23.3,
    "interview_to_hire_rate": 79.17,
    "interview_completion_rate": 95.83,
    "performance_tier": "Low",
    "is_fast_process": 1,
    "has_good_interview_quality": 1
  }
]
```
