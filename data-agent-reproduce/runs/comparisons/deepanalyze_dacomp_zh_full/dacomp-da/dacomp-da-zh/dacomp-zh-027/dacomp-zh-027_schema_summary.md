# SQLite 数据摘要

文件: `dacomp-zh-027.sqlite`


## 人力资源

- Rows: 999

- Columns: 人力ID (TEXT), 灾害ID (TEXT), 行动ID (TEXT), 人员配置 (TEXT)

```json
[
  {
    "人力ID": "HR_HV7U",
    "灾害ID": "DIST_SB6K7",
    "行动ID": "OPS_76ZOW",
    "人员配置": "{\"personnel\": {\"total\": 140, \"medical\": 52, \"security\": 90, \"logistics\": 99, \"volunteers\": 435}, \"readiness\": {\"ppe_status\": \"Limited\", \"comm_equipment\": \"Sufficient\", \"training_status\": \"Complete\", \"availability_percent\": 94.10}}"
  },
  {
    "人力ID": "HR_ZZXC",
    "灾害ID": "DIST_PGACZ",
    "行动ID": "OPS_QXWBZ",
    "人员配置": "{\"personnel\": {\"total\": 55, \"medical\": 30, \"security\": 53, \"logistics\": 197, \"volunteers\": 541}, \"readiness\": {\"ppe_status\": \"Critical\", \"comm_equipment\": \"Sufficient\", \"training_status\": \"In Progress\", \"availability_percent\": 87.70}}"
  },
  {
    "人力ID": "HR_JA87",
    "灾害ID": "DIST_HJ1BQ",
    "行动ID": "OPS_GGBVJ",
    "人员配置": "{\"personnel\": {\"total\": 234, \"medical\": 38, \"security\": 46, \"logistics\": 93, \"volunteers\": 781}, \"readiness\": {\"ppe_status\": \"Adequate\", \"comm_equipment\": \"Sufficient\", \"training_status\": \"In Progress\", \"availability_percent\": 82.50}}"
  }
]
```


## 分发中心

- Rows: 999

- Columns: 分发中心ID (TEXT), 灾害事件ID (TEXT), 中心容量(吨) (INTEGER), 利用率(%) (REAL), 仓储容量(m³) (INTEGER), 可用容量(m³) (INTEGER), 冷库容量(m³) (INTEGER), 冷库温度(℃) (REAL), 仓库状态 (TEXT), 库存准确率(%) (REAL), 库存周转率 (REAL)

```json
[
  {
    "分发中心ID": "HUB_HS0I",
    "灾害事件ID": "DIST_SB6K7",
    "中心容量(吨)": 5101,
    "利用率(%)": 9.4,
    "仓储容量(m³)": 93293,
    "可用容量(m³)": 7279,
    "冷库容量(m³)": 249,
    "冷库温度(℃)": 6.6,
    "仓库状态": "Fair",
    "库存准确率(%)": 91.3,
    "库存周转率": 3.31
  },
  {
    "分发中心ID": "HUB_UGZM",
    "灾害事件ID": "DIST_PGACZ",
    "中心容量(吨)": 1825,
    "利用率(%)": 52.3,
    "仓储容量(m³)": 45603,
    "可用容量(m³)": 9050,
    "冷库容量(m³)": 151,
    "冷库温度(℃)": 5.9,
    "仓库状态": "Excellent",
    "库存准确率(%)": 98.4,
    "库存周转率": 0.63
  },
  {
    "分发中心ID": "HUB_05ZL",
    "灾害事件ID": "DIST_HJ1BQ",
    "中心容量(吨)": 7553,
    "利用率(%)": 79.7,
    "仓储容量(m³)": 2908,
    "可用容量(m³)": 9396,
    "冷库容量(m³)": 395,
    "冷库温度(℃)": 4.0,
    "仓库状态": "Good",
    "库存准确率(%)": 92.9,
    "库存周转率": 1.14
  }
]
```


## 协调与评估

- Rows: 999

- Columns: 协调评估ID (TEXT), 分发ID (TEXT), 行动ID (TEXT), 安全事件数量 (INTEGER), 安全等级 (TEXT), 通行限制 (TEXT), 协调效果水平 (TEXT), 合作组织数量 (INTEGER), 信息共享状态 (TEXT), 报告合规性 (REAL), 数据质量值 (INTEGER), 监测频率 (TEXT), 评估阶段 (TEXT), 经验总结阶段 (TEXT), 应急预案阶段 (TEXT), 风险缓解措施 (TEXT), 保险覆盖范围 (TEXT), 合规状态 (TEXT), 审计状态 (TEXT), 质量控制步骤 (TEXT), 利益相关者满意度 (REAL), 媒体报道情绪 (TEXT), 公众认知 (REAL), 文档状态 (TEXT), 记录的经验 (INTEGER), 列出的最佳实践 (INTEGER), 改进建议 (INTEGER), 下次复审日期 (TEXT), 备注 (TEXT)

```json
[
  {
    "协调评估ID": "COORD_D3PK",
    "分发ID": "DIST_SB6K7",
    "行动ID": "OPS_76ZOW",
    "安全事件数量": 83,
    "安全等级": "Safe",
    "通行限制": "Partial",
    "协调效果水平": "Medium",
    "合作组织数量": 9,
    "信息共享状态": "Poor",
    "报告合规性": 91.0,
    "数据质量值": 4,
    "监测频率": "Monthly",
    "评估阶段": "Overdue",
    "经验总结阶段": "In Progress",
    "应急预案阶段": "Overdue",
    "风险缓解措施": "Insufficient",
    "保险覆盖范围": "Full",
    "合规状态": "Partial",
    "审计状态": "Completed",
    "质量控制步骤": "Moderate",
    "利益相关者满意度": 4.0,
    "媒体报道情绪": "Positive",
    "公众认知": 3.5,
    "文档状态": "Partial",
    "记录的经验": 5,
    "列出的最佳实践": 2,
    "改进建议": 25,
    "下次复审日期": "2025-04-22",
    "备注": "Record item between direction program media bed across."
  },
  {
    "协调评估ID": "COORD_Z5NY",
    "分发ID": "DIST_PGACZ",
    "行动ID": "OPS_QXWBZ",
    "安全事件数量": 45,
    "安全等级": "Safe",
    "通行限制": "Partial",
    "协调效果水平": "Low",
    "合作组织数量": 36,
    "信息共享状态": "Limited",
    "报告合规性": 77.4,
    "数据质量值": 3,
    "监测频率": "Daily",
    "评估阶段": "Overdue",
    "经验总结阶段": "Documented",
    "应急预案阶段": "Due",
    "风险缓解措施": "Insufficient",
    "保险覆盖范围": "Partial",
    "合规状态": "Partial",
    "审计状态": "Due",
    "质量控制步骤": "Moderate",
    "利益相关者满意度": 2.1,
    "媒体报道情绪": "Positive",
    "公众认知": 1.5,
    "文档状态": "Partial",
    "记录的经验": 22,
    "列出的最佳实践": 4,
    "改进建议": 16,
    "下次复审日期": "2025-03-09",
    "备注": null
  },
  {
    "协调评估ID": "COORD_67A3",
    "分发ID": "DIST_HJ1BQ",
    "行动ID": "OPS_GGBVJ",
    "安全事件数量": 49,
    "安全等级": "Moderate",
    "通行限制": "Severe",
    "协调效果水平": "Low",
    "合作组织数量": 21,
    "信息共享状态": "Limited",
    "报告合规性": 77.1,
    "数据质量值": 4,
    "监测频率": "Monthly",
    "评估阶段": "Due",
    "经验总结阶段": "Pending",
    "应急预案阶段": "Overdue",
    "风险缓解措施": "Partial",
    "保险覆盖范围": "Full",
    "合规状态": "Partial",
    "审计状态": "Completed",
    "质量控制步骤": "Strong",
    "利益相关者满意度": 3.8,
    "媒体报道情绪": "Neutral",
    "公众认知": 2.1,
    "文档状态": "Incomplete",
    "记录的经验": 19,
    "列出的最佳实践": 4,
    "改进建议": 26,
    "下次复审日期": "2025-07-05",
    "备注": "Recent discuss part seven fact."
  }
]
```


## 受益人与评估

- Rows: 999

- Columns: 受影响人口登记ID (TEXT), 分发ID (TEXT), 行动ID (TEXT), 受影响人口登记信息 (TEXT), 脆弱性评估 (TEXT), 需求评估状态 (TEXT), 分发公平性指数 (REAL), 受影响人口反馈评分 (REAL), 社区参与 (TEXT), 当地能力建设 (TEXT)

```json
[
  {
    "受影响人口登记ID": "BENE_4NZJ",
    "分发ID": "DIST_SB6K7",
    "行动ID": "OPS_76ZOW",
    "受影响人口登记信息": "Complete",
    "脆弱性评估": "Complete",
    "需求评估状态": "Due",
    "分发公平性指数": 0.54,
    "受影响人口反馈评分": 2.3,
    "社区参与": "High",
    "当地能力建设": "Limited"
  },
  {
    "受影响人口登记ID": "BENE_FJSN",
    "分发ID": "DIST_PGACZ",
    "行动ID": "OPS_QXWBZ",
    "受影响人口登记信息": "Pending",
    "脆弱性评估": "Complete",
    "需求评估状态": "Overdue",
    "分发公平性指数": 0.87,
    "受影响人口反馈评分": 1.3,
    "社区参与": "Low",
    "当地能力建设": "Limited"
  },
  {
    "受影响人口登记ID": "BENE_RCD9",
    "分发ID": "DIST_HJ1BQ",
    "行动ID": "OPS_GGBVJ",
    "受影响人口登记信息": "Complete",
    "脆弱性评估": "Pending",
    "需求评估状态": "Overdue",
    "分发公平性指数": 0.88,
    "受影响人口反馈评分": 1.5,
    "社区参与": "Medium",
    "当地能力建设": "Active"
  }
]
```


## 灾害事件

- Rows: 999

- Columns: 灾害事件ID (TEXT), 时间标记 (TEXT), 灾害类型 (TEXT), 灾害等级 (TEXT), 受灾区域 (TEXT), 区域标签 (TEXT), 纬度坐标 (REAL), 经度坐标 (REAL), 影响指标 (TEXT)

```json
[
  {
    "灾害事件ID": "DIST_SB6K7",
    "时间标记": "2024-12-21 19:49:09.72037",
    "灾害类型": "Wildfire",
    "灾害等级": "Level 3",
    "受灾区域": "East Jeremy",
    "区域标签": "RC7250    ",
    "纬度坐标": 51.203609,
    "经度坐标": 36.221141,
    "影响指标": "{\"population\": {\"injured\": 4524, \"missing\": 212, \"affected\": 228943, \"displaced\": 38806, \"casualties\": 174}, \"damage_level\": \"Severe\", \"communication\": \"Limited\", \"infrastructure\": {\"damage_percent\": 19.00, \"power_outage_percent\": 93.200, \"water_damage_percent\": 77}, \"transportation\": \"Full\"}"
  },
  {
    "灾害事件ID": "DIST_PGACZ",
    "时间标记": "2024-03-13 16:56:26.72037",
    "灾害类型": "Earthquake",
    "灾害等级": "Level 5",
    "受灾区域": "Lake Mariah",
    "区域标签": "RC2170    ",
    "纬度坐标": -89.890572,
    "经度坐标": 62.081501,
    "影响指标": "{\"population\": {\"injured\": 4304, \"missing\": 363, \"affected\": 241273, \"displaced\": 31578, \"casualties\": 8}, \"damage_level\": \"Moderate\", \"communication\": \"Operational\", \"infrastructure\": {\"damage_percent\": 68.90, \"power_outage_percent\": 22.500, \"water_damage_percent\": 40}, \"transportation\": \"Full\"}"
  },
  {
    "灾害事件ID": "DIST_HJ1BQ",
    "时间标记": "2024-12-08 06:09:09.72037",
    "灾害类型": "Earthquake",
    "灾害等级": "Level 5",
    "受灾区域": "New Kellychester",
    "区域标签": "RC8678    ",
    "纬度坐标": 80.026921,
    "经度坐标": -146.007423,
    "影响指标": "{\"population\": {\"injured\": 4333, \"missing\": 222, \"affected\": 389569, \"displaced\": 66484, \"casualties\": 355}, \"damage_level\": \"Minor\", \"communication\": \"Limited\", \"infrastructure\": {\"damage_percent\": 79.70, \"power_outage_percent\": 83.800, \"water_damage_percent\": 27}, \"transportation\": \"Limited\"}"
  }
]
```


## 物资

- Rows: 999

- Columns: 物资ID (TEXT), 灾害ID (TEXT), 分发中心ID (TEXT), 库存资源 (TEXT)

```json
[
  {
    "物资ID": "SUP_4BZN3",
    "灾害ID": "DIST_SB6K7",
    "分发中心ID": "HUB_HS0I",
    "库存资源": "{\"power\": {\"generators\": 568, \"fuel_liters\": 86011.0}, \"medical\": 50590, \"shelter\": {\"units\": 7534, \"blankets\": 46019}, \"essentials\": {\"food_tons\": 479.400, \"water_liters\": 283596.000}, \"hygiene_kits\": 46981}"
  },
  {
    "物资ID": "SUP_ZJ88H",
    "灾害ID": "DIST_PGACZ",
    "分发中心ID": "HUB_UGZM",
    "库存资源": "{\"power\": {\"generators\": 733, \"fuel_liters\": 59156.0}, \"medical\": 51298, \"shelter\": {\"units\": 1968, \"blankets\": 26671}, \"essentials\": {\"food_tons\": 187.100, \"water_liters\": 139603.000}, \"hygiene_kits\": 99277}"
  },
  {
    "物资ID": "SUP_MCBWM",
    "灾害ID": "DIST_HJ1BQ",
    "分发中心ID": "HUB_05ZL",
    "库存资源": "{\"power\": {\"generators\": 881, \"fuel_liters\": 46825.0}, \"medical\": 15593, \"shelter\": {\"units\": 6390, \"blankets\": 78690}, \"essentials\": {\"food_tons\": 640.800, \"water_liters\": 878396.000}, \"hygiene_kits\": 31061}"
  }
]
```


## 环境与健康

- Rows: 999

- Columns: 环境ID (TEXT), 灾害ID (TEXT), 环境影响率 (TEXT), 废物管理状态 (TEXT), 回收率(%) (REAL), 碳排放(吨) (REAL), 可再生能源占比(%) (REAL), 水质指数 (REAL), 卫生覆盖率 (REAL), 疾病风险 (TEXT), 医疗应急能力 (TEXT), 疫苗覆盖率 (REAL), 心理健康援助 (TEXT)

```json
[
  {
    "环境ID": "ENV_XU4H",
    "灾害ID": "DIST_SB6K7",
    "环境影响率": "Low",
    "废物管理状态": "Adequate",
    "回收率(%)": 68.4,
    "碳排放(吨)": 793.5,
    "可再生能源占比(%)": 43.3,
    "水质指数": 85.6,
    "卫生覆盖率": 53.5,
    "疾病风险": "High",
    "医疗应急能力": "Adequate",
    "疫苗覆盖率": 14.8,
    "心理健康援助": "Limited"
  },
  {
    "环境ID": "ENV_NO2C",
    "灾害ID": "DIST_PGACZ",
    "环境影响率": "Low",
    "废物管理状态": "Adequate",
    "回收率(%)": 62.4,
    "碳排放(吨)": 403.3,
    "可再生能源占比(%)": 27.5,
    "水质指数": 90.9,
    "卫生覆盖率": 65.5,
    "疾病风险": "High",
    "医疗应急能力": "Critical",
    "疫苗覆盖率": 77.7,
    "心理健康援助": "Available"
  },
  {
    "环境ID": "ENV_U9JR",
    "灾害ID": "DIST_HJ1BQ",
    "环境影响率": "High",
    "废物管理状态": "Adequate",
    "回收率(%)": 18.1,
    "碳排放(吨)": 270.2,
    "可再生能源占比(%)": 27.7,
    "水质指数": 11.7,
    "卫生覆盖率": 6.6,
    "疾病风险": "Medium",
    "医疗应急能力": "Adequate",
    "疫苗覆盖率": 24.6,
    "心理健康援助": "Limited"
  }
]
```


## 财务

- Rows: 999

- Columns: 财务ID (TEXT), 灾害ID (TEXT), 行动ID (TEXT), 预算分配(USD) (INTEGER), 资金利用率(%) (REAL), 人均成本(USD) (REAL), 行动成本(USD) (INTEGER), 运输成本(USD) (INTEGER), 仓储成本(USD) (INTEGER), 人员成本(USD) (INTEGER), 资金状态 (TEXT), 捐赠承诺(USD) (INTEGER), 资源缺口(USD) (INTEGER)

```json
[
  {
    "财务ID": "FIN_OMQ1",
    "灾害ID": "DIST_SB6K7",
    "行动ID": "OPS_76ZOW",
    "预算分配(USD)": 4227090,
    "资金利用率(%)": 9.8,
    "人均成本(USD)": 844.12,
    "行动成本(USD)": 88256,
    "运输成本(USD)": 976202,
    "仓储成本(USD)": 111548,
    "人员成本(USD)": 364821,
    "资金状态": "Critical",
    "捐赠承诺(USD)": 7699177,
    "资源缺口(USD)": 95367
  },
  {
    "财务ID": "FIN_W50I",
    "灾害ID": "DIST_PGACZ",
    "行动ID": "OPS_QXWBZ",
    "预算分配(USD)": 3625344,
    "资金利用率(%)": 35.0,
    "人均成本(USD)": 18.76,
    "行动成本(USD)": 919777,
    "运输成本(USD)": 77922,
    "仓储成本(USD)": 272650,
    "人员成本(USD)": 470856,
    "资金状态": "Adequate",
    "捐赠承诺(USD)": 4068978,
    "资源缺口(USD)": 442493
  },
  {
    "财务ID": "FIN_5B9D",
    "灾害ID": "DIST_HJ1BQ",
    "行动ID": "OPS_GGBVJ",
    "预算分配(USD)": 7987244,
    "资金利用率(%)": 42.5,
    "人均成本(USD)": 837.72,
    "行动成本(USD)": 594338,
    "运输成本(USD)": 811935,
    "仓储成本(USD)": 492222,
    "人员成本(USD)": 906025,
    "资金状态": "Adequate",
    "捐赠承诺(USD)": 6778191,
    "资源缺口(USD)": 426146
  }
]
```


## 运营

- Rows: 999

- Columns: 行动ID (TEXT), 灾害ID (TEXT), 分发中心ID (TEXT), 紧急级别 (TEXT), 响应阶段 (TEXT), 行动状态 (TEXT), 协调中心 (TEXT), 开始日期 (TEXT), 预计持续天数 (INTEGER), 优先级 (TEXT), 资源分配状态 (TEXT), 供应流动状态 (TEXT)

```json
[
  {
    "行动ID": "OPS_76ZOW",
    "灾害ID": "DIST_SB6K7",
    "分发中心ID": "HUB_HS0I",
    "紧急级别": "Black",
    "响应阶段": "Reconstruction",
    "行动状态": "Completed",
    "协调中心": "CC7649",
    "开始日期": "2025-01-26",
    "预计持续天数": 12,
    "优先级": "High",
    "资源分配状态": "Limited",
    "供应流动状态": "Disrupted"
  },
  {
    "行动ID": "OPS_QXWBZ",
    "灾害ID": "DIST_PGACZ",
    "分发中心ID": "HUB_UGZM",
    "紧急级别": "Black",
    "响应阶段": "Recovery",
    "行动状态": "Completed",
    "协调中心": "CC6010",
    "开始日期": "2025-02-08",
    "预计持续天数": 362,
    "优先级": "Medium",
    "资源分配状态": "Limited",
    "供应流动状态": "Stable"
  },
  {
    "行动ID": "OPS_GGBVJ",
    "灾害ID": "DIST_HJ1BQ",
    "分发中心ID": "HUB_05ZL",
    "紧急级别": "Orange",
    "响应阶段": "Emergency",
    "行动状态": "Scaling Down",
    "协调中心": "CC3314",
    "开始日期": "2025-02-17",
    "预计持续天数": 291,
    "优先级": "Medium",
    "资源分配状态": "Critical",
    "供应流动状态": "Strained"
  }
]
```


## 运输

- Rows: 999

- Columns: 运输ID (TEXT), 灾害ID (TEXT), 分发中心ID (TEXT), 物资ID (TEXT), 车辆数 (INTEGER), 可用卡车 (INTEGER), 可用直升机 (INTEGER), 可用船只 (INTEGER), 总运输量(吨) (INTEGER), 日运输量(吨) (INTEGER), 末端配送状态 (TEXT), 分发点数 (INTEGER), 平均交付时间 (REAL), 交付成功率 (REAL), 路线优化状态 (TEXT), 油耗(L/km) (REAL), 维护状态 (TEXT), 车辆故障率 (REAL)

```json
[
  {
    "运输ID": "TRANS_B6EA6",
    "灾害ID": "DIST_SB6K7",
    "分发中心ID": "HUB_HS0I",
    "物资ID": "SUP_4BZN3",
    "车辆数": 141,
    "可用卡车": 88,
    "可用直升机": 7,
    "可用船只": 7,
    "总运输量(吨)": 368,
    "日运输量(吨)": 227,
    "末端配送状态": "On Track",
    "分发点数": 35,
    "平均交付时间": 52.6,
    "交付成功率": 79.4,
    "路线优化状态": "In Progress",
    "油耗(L/km)": 10.6,
    "维护状态": "Overdue",
    "车辆故障率": 9.2
  },
  {
    "运输ID": "TRANS_0870R",
    "灾害ID": "DIST_PGACZ",
    "分发中心ID": "HUB_UGZM",
    "物资ID": "SUP_ZJ88H",
    "车辆数": 50,
    "可用卡车": 87,
    "可用直升机": 8,
    "可用船只": 2,
    "总运输量(吨)": 2771,
    "日运输量(吨)": 364,
    "末端配送状态": "On Track",
    "分发点数": 14,
    "平均交付时间": 20.7,
    "交付成功率": 92.6,
    "路线优化状态": "Optimized",
    "油耗(L/km)": 17.7,
    "维护状态": "Overdue",
    "车辆故障率": 6.9
  },
  {
    "运输ID": "TRANS_FGSRQ",
    "灾害ID": "DIST_HJ1BQ",
    "分发中心ID": "HUB_05ZL",
    "物资ID": "SUP_MCBWM",
    "车辆数": 20,
    "可用卡车": 77,
    "可用直升机": 4,
    "可用船只": 4,
    "总运输量(吨)": 1505,
    "日运输量(吨)": 150,
    "末端配送状态": "Delayed",
    "分发点数": 6,
    "平均交付时间": 17.8,
    "交付成功率": 79.9,
    "路线优化状态": "Optimized",
    "油耗(L/km)": 18.7,
    "维护状态": "Up to Date",
    "车辆故障率": 5.0
  }
]
```
