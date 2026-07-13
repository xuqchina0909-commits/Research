# SQLite 数据摘要

文件: `dacomp-zh-056.sqlite`


## customer360__conversion_funnel_analysis

- Rows: 0

- Columns: marketo_lead_id (INTEGER), stripe_customer_id (TEXT), zendesk_user_id (INTEGER), primary_email (TEXT), primary_organization (TEXT), customer_segment (TEXT), customer_tier (TEXT), lifecycle_stage (TEXT), reached_awareness (INTEGER), reached_conversion (INTEGER), reached_support (INTEGER), journey_completeness_score (INTEGER), customer_journey_pattern (TEXT), funnel_efficiency (TEXT), marketing_to_sales_days (INTEGER), sales_to_support_days (INTEGER), awareness_to_conversion_speed (TEXT), conversion_to_support_speed (TEXT), journey_velocity (TEXT), revenue_velocity_monthly (REAL), awareness_engagement_quality (INTEGER), conversion_engagement_quality (INTEGER), support_engagement_quality (INTEGER), cross_stage_engagement_consistency (REAL), weighted_engagement_score (REAL), primary_engagement_channel (TEXT), next_stage_conversion_probability (REAL), predictive_full_journey_probability (REAL), drop_off_risk (TEXT), value_realization_pattern (TEXT), optimization_recommendation (TEXT), expected_optimization_value (REAL), intervention_priority (TEXT), success_target (TEXT), funnel_performance_grade (TEXT), journey_efficiency_index (REAL), activity_grade (TEXT), customer_health_score (REAL), estimated_customer_ltv (REAL), account_age_days (INTEGER), customer_first_touchpoint (TIMESTAMP), customer_last_activity (TIMESTAMP), funnel_analysis_timestamp (TIMESTAMP)

```json
[]
```


## customer360__customer_activity_metrics

- Rows: 0

- Columns: marketo_lead_id (INTEGER), stripe_customer_id (TEXT), zendesk_user_id (INTEGER), primary_email (TEXT), primary_organization (TEXT), customer_segment (TEXT), customer_journey_pattern (TEXT), lifecycle_stage (TEXT), composite_engagement_score (REAL), weighted_engagement_score (REAL), customer_health_score (REAL), activity_grade (TEXT), activity_priority_score (REAL), days_since_last_activity (INTEGER), weeks_since_last_activity (INTEGER), months_since_last_activity (INTEGER), account_age_days (INTEGER), active_channel_count (INTEGER), primary_engagement_channel (TEXT), marketing_engagement_score (REAL), sales_engagement_score (REAL), support_engagement_score (REAL), marketing_depth (TEXT), sales_depth (TEXT), support_depth (TEXT), engagement_velocity (TEXT), activity_momentum (TEXT), engagement_maturity (TEXT), estimated_monthly_activities (REAL), predicted_next_month_activity (REAL), seasonally_adjusted_activity (REAL), active_30_days (INTEGER), active_60_days (INTEGER), active_90_days (INTEGER), active_180_days (INTEGER), active_365_days (INTEGER), activity_risk_level (TEXT), cross_platform_consistency (REAL), activity_efficiency (REAL), recommended_activity_intervention (TEXT), in_marketo (INTEGER), in_stripe (INTEGER), in_zendesk (INTEGER), is_unsubscribed (INTEGER), is_email_invalid (INTEGER), do_not_call (INTEGER), is_delinquent (INTEGER), stripe_deleted (INTEGER), zendesk_active (INTEGER), zendesk_suspended (INTEGER), zendesk_deleted (INTEGER), customer_first_touchpoint (TIMESTAMP), customer_last_activity (TIMESTAMP), marketo_registration_date (TIMESTAMP), stripe_registration_date (TIMESTAMP), zendesk_registration_date (TIMESTAMP), activity_analysis_timestamp (TIMESTAMP)

```json
[]
```


## customer360__customer_value_analysis

- Rows: 5001

- Columns: marketo_lead_id (INTEGER), stripe_customer_id (TEXT), zendesk_user_id (INTEGER), primary_email (TEXT), primary_organization (TEXT), customer_segment (TEXT), customer_tier (TEXT), rfm_segment (TEXT), rfm_score (TEXT), rfm_avg_score (REAL), recency_score (INTEGER), frequency_score (INTEGER), monetary_score (INTEGER), estimated_customer_ltv (REAL), adjusted_ltv (REAL), expected_annual_revenue (REAL), revenue_tier (TEXT), strategic_classification (TEXT), value_stability (TEXT), upsell_potential (TEXT), churn_probability (REAL), potential_revenue_loss (REAL), revenue_risk_percentage (REAL), portfolio_contribution_pct (REAL), concentration_risk (TEXT), investment_priority_score (REAL), acquisition_roi_assessment (TEXT), recommended_engagement_model (TEXT), investment_recommendation (TEXT), success_target (TEXT), development_opportunity (TEXT), customer_health_score (REAL), lifecycle_stage (TEXT), risk_category (TEXT), account_age_days (INTEGER), days_since_last_activity (INTEGER), analysis_timestamp (TIMESTAMP)

```json
[
  {
    "marketo_lead_id": 8915,
    "stripe_customer_id": "cus_000801",
    "zendesk_user_id": 3232,
    "primary_email": "muriel.davis@gmail.com",
    "primary_organization": "AI Innovations",
    "customer_segment": "Loyal Customer",
    "customer_tier": "Platinum",
    "rfm_segment": "Loyal Customer",
    "rfm_score": "454",
    "rfm_avg_score": 4.333333333333333,
    "recency_score": 4,
    "frequency_score": 5,
    "monetary_score": 4,
    "estimated_customer_ltv": 11466.0,
    "adjusted_ltv": 9172.8,
    "expected_annual_revenue": 2276.41,
    "revenue_tier": "Tier 1 - Strategic",
    "strategic_classification": "Strategic Account",
    "value_stability": "Medium Stability",
    "upsell_potential": "Retention Focus",
    "churn_probability": 0.35,
    "potential_revenue_loss": 3210.48,
    "revenue_risk_percentage": 35.0,
    "portfolio_contribution_pct": 0.1867174419323816,
    "concentration_risk": "Low Concentration Risk",
    "investment_priority_score": 4.4,
    "acquisition_roi_assessment": "Good ROI",
    "recommended_engagement_model": "Executive Relationship Management",
    "investment_recommendation": "Medium Investment",
    "success_target": "Immediate Intervention",
    "development_opportunity": "Value Preservation",
    "customer_health_score": 3.3,
    "lifecycle_stage": "Retention",
    "risk_category": "Low Risk",
    "account_age_days": 956,
    "days_since_last_activity": 137,
    "analysis_timestamp": "2025-09-20 18:18:23.377000+08:00"
  },
  {
    "marketo_lead_id": 8915,
    "stripe_customer_id": "cus_000801",
    "zendesk_user_id": 3232,
    "primary_email": "muriel.davis@gmail.com",
    "primary_organization": "AI Innovations",
    "customer_segment": "Loyal Customer",
    "customer_tier": "Platinum",
    "rfm_segment": "Loyal Customer",
    "rfm_score": "445",
    "rfm_avg_score": 4.333333333333333,
    "recency_score": 4,
    "frequency_score": 4,
    "monetary_score": 5,
    "estimated_customer_ltv": 11466.0,
    "adjusted_ltv": 9172.8,
    "expected_annual_revenue": 2276.41,
    "revenue_tier": "Tier 1 - Strategic",
    "strategic_classification": "Strategic Account",
    "value_stability": "Medium Stability",
    "upsell_potential": "Retention Focus",
    "churn_probability": 0.35,
    "potential_revenue_loss": 3210.48,
    "revenue_risk_percentage": 35.0,
    "portfolio_contribution_pct": 0.28465236672737565,
    "concentration_risk": "Low Concentration Risk",
    "investment_priority_score": 4.4,
    "acquisition_roi_assessment": "Good ROI",
    "recommended_engagement_model": "Executive Relationship Management",
    "investment_recommendation": "Medium Investment",
    "success_target": "Immediate Intervention",
    "development_opportunity": "Value Preservation",
    "customer_health_score": 3.3,
    "lifecycle_stage": "Retention",
    "risk_category": "Low Risk",
    "account_age_days": 956,
    "days_since_last_activity": 137,
    "analysis_timestamp": "2025-09-20 18:18:23.377000+08:00"
  },
  {
    "marketo_lead_id": 6947,
    "stripe_customer_id": "cus_005460",
    "zendesk_user_id": 1108,
    "primary_email": "sylvester.wilson@enterprise.org",
    "primary_organization": "Cloud Services Co",
    "customer_segment": "Loyal Customer",
    "customer_tier": "Platinum",
    "rfm_segment": "Loyal Customer",
    "rfm_score": "444",
    "rfm_avg_score": 4.0,
    "recency_score": 4,
    "frequency_score": 4,
    "monetary_score": 4,
    "estimated_customer_ltv": 11466.0,
    "adjusted_ltv": 9172.8,
    "expected_annual_revenue": 2487.14,
    "revenue_tier": "Tier 1 - Strategic",
    "strategic_classification": "Strategic Account",
    "value_stability": "Medium Stability",
    "upsell_potential": "Retention Focus",
    "churn_probability": 0.35,
    "potential_revenue_loss": 3210.48,
    "revenue_risk_percentage": 35.0,
    "portfolio_contribution_pct": 0.24948508286667265,
    "concentration_risk": "Low Concentration Risk",
    "investment_priority_score": 4.4,
    "acquisition_roi_assessment": "Good ROI",
    "recommended_engagement_model": "Executive Relationship Management",
    "investment_recommendation": "Medium Investment",
    "success_target": "Immediate Intervention",
    "development_opportunity": "Value Preservation",
    "customer_health_score": 3.3,
    "lifecycle_stage": "Retention",
    "risk_category": "Low Risk",
    "account_age_days": 875,
    "days_since_last_activity": 166,
    "analysis_timestamp": "2025-09-20 18:18:23.377000+08:00"
  }
]
```
