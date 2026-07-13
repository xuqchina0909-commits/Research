from deepeye_benchmark_runner import structured_answer_from_messages


def test_structured_answer_from_messages_extracts_list_result() -> None:
    messages = [
        {
            "role": "assistant",
            "steps": [
                {
                    "output": {
                        "workspace_state": {
                            "run": {
                                "result": {
                                    "outputs": {
                                        "filter_and_calculate": {
                                            "dataset_ref": {
                                                "kind": "dataset_ref",
                                                "source": "python.code",
                                                "name": "filter_and_calculate_output_rows",
                                                "row_count": 2,
                                                "columns": ["year"],
                                                "preview_rows": [{"year": "2010"}, {"year": "2011"}],
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            ],
        }
    ]
    task = {"answer_type": "list_exact"}

    assert structured_answer_from_messages(messages, task) == "[2010, 2011]"


def test_structured_answer_from_messages_extracts_numeric_result() -> None:
    messages = [
        {
            "role": "assistant",
            "steps": [
                {
                    "output": {
                        "workspace_state": {
                            "run": {
                                "result": {
                                    "outputs": {
                                        "calculate_ratio": {
                                            "dataset_ref": {
                                                "kind": "dataset_ref",
                                                "source": "python.code",
                                                "name": "calculate_ratio_output_rows",
                                                "row_count": 1,
                                                "columns": ["ratio", "value_2024", "value_2001"],
                                                "preview_rows": [
                                                    {
                                                        "ratio": 13.16279420289855,
                                                        "value_2024": 1135291,
                                                        "value_2001": 86250,
                                                    }
                                                ],
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            ],
        }
    ]
    task = {"answer_type": "numeric_approximate"}

    assert structured_answer_from_messages(messages, task) == "13.16279420289855"
