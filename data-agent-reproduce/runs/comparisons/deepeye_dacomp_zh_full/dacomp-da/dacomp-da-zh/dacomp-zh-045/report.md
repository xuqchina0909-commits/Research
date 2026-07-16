工作流规划已停止：Workflow execution failed at node analyze_collections (python.code): Traceback (most recent call last):
  File "/workspace/.workflow_scripts/analyze_collections.py", line 70, in <module>
    product_df = load_dataset_ref(data['dataset_ref'][1])
                                  ~~~~~~~~~~~~~~~~~~~^^^
IndexError: list index out of range

INPUT_PREVIEW (first 10 lines):
{
  "dataset_ref": [
    {
      "kind": "dataset_ref",
      "path": "/workspace/.datasets/join_data_output_rows.jsonl",
      "format": "jsonl",
      "source": "python.code",
      "name": "join_data_output_rows",
      "row_count": 216,
      "columns": [