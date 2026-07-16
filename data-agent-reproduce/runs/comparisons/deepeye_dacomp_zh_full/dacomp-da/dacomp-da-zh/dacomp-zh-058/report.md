工作流规划已停止：Workflow execution failed at node calculate_health_score (python.code):   File "/workspace/.workflow_scripts/calculate_health_score.py", line 71
    campaigns_df['cost_efficiency'] = 1 / (campaigns_df['cost'] + 1)
IndentationError: unexpected indent

INPUT_PREVIEW (first 10 lines):
{
  "dataset_ref": [
    {
      "kind": "dataset_ref",
      "path": "/workspace/.datasets/select_columns_selected.jsonl",
      "format": "jsonl",
      "source": "rows.select",
      "name": "select_columns_selected",
      "row_count": 155,
      "columns": [