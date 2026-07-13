工作流规划已停止：Workflow execution failed at node query_sales (sql.execute): (sqlite3.OperationalError) no such column: 千克
[SQL: SELECT 单品编码, SUM(销量(千克)) AS total_sales FROM "销售记录" WHERE 销售日期 = '2023-07-01' GROUP BY 单品编码]
(Background on this error at: https://sqlalche.me/e/20/e3q8)