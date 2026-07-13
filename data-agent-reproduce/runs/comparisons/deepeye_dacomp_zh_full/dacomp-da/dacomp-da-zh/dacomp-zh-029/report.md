工作流规划已停止：Workflow execution failed at node query_vehicles (sql.execute): (sqlite3.OperationalError) no such column: KM
[SQL: SELECT 标题, 价格, 新车含税价, 表显里程, 上牌时间, 车辆级别, 燃料类型, WLTC纯电续航里程(KM), 保险到期 FROM "汽车之家" WHERE 标签 LIKE '%准新车%' OR 标签 LIKE '%新上架%' ORDER BY 价格 DESC LIMIT 10]
(Background on this error at: https://sqlalche.me/e/20/e3q8)