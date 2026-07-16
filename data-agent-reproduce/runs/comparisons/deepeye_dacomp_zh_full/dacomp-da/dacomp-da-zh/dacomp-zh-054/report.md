工作流规划已停止：Workflow execution failed at node analyze_customers (python.code): bash: line 1:    42 Killed                  python /workspace/.workflow_scripts/analyze_customers.py < /workspace/.workflow_scripts/analyze_customers_input.json

INPUT_PREVIEW (first 10 lines):
{
  "dataset_ref": [
    {
      "kind": "dataset_ref",
      "path": "/workspace/.datasets/query_customers_query.jsonl",
      "format": "jsonl",
      "source": "sql.execute",
      "name": "query_customers_query",
      "row_count": 203159,
      "columns": [