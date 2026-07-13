工作流规划已停止：Workflow execution failed at node query_inventory (sql.execute): (sqlite3.OperationalError) no such column: i.库存状态
[SQL: SELECT i.药品ID, i.近效期库存量, i.合格库存量, i.库存状态, i.近效期药品数量, i.过期药品数量, i.退货药品数量, i.破损药品数量, i.虫蛀霉变数量, i.鼠咬污染数量, i.空气污染数量, i.温湿度超标记录, p.质量层次 AS 质量层次 FROM "库存管理" i JOIN "药品基本信息" p ON i.药品ID = p.药品ID]
(Background on this error at: https://sqlalche.me/e/20/e3q8)