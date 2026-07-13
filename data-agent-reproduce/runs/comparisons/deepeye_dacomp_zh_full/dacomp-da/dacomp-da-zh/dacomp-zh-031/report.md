工作流规划已停止：Workflow execution failed at node combine_results (python.code): Traceback (most recent call last):
  File "/workspace/.workflow_scripts/combine_results.py", line 86, in <module>
    emit_dataframe(combined_data)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "/workspace/.workflow_scripts/combine_results.py", line 38, in emit_dataframe
    print(df.to_json(orient="records"))
          ^^^^^^^^^^
AttributeError: 'dict' object has no attribute 'to_json'

INPUT_PREVIEW (first 10 lines):
{
  "dataset_ref": [
    {
      "kind": "dataset_ref",
      "path": "/workspace/.datasets/query_employees_query.jsonl",
      "format": "jsonl",
      "source": "sql.execute",
      "name": "query_employees_query",
      "row_count": 10,
      "columns": [