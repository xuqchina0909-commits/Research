工作流规划已停止：Workflow execution failed at node calculate_metrics (python.code): bash: line 1:    42 Killed                  python /workspace/.workflow_scripts/calculate_metrics.py < /workspace/.workflow_scripts/calculate_metrics_input.json

INPUT_PREVIEW (first 10 lines):
{
  "dataset_ref": [
    {
      "kind": "dataset_ref",
      "path": "/workspace/.datasets/query_promotion_sales_query.jsonl",
      "format": "jsonl",
      "source": "sql.execute",
      "name": "query_promotion_sales_query",
      "row_count": 1703800,
      "columns": [