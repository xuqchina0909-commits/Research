# SQLite 数据摘要

文件: `dacomp-zh-017.sqlite`


## 商品浏览

- Rows: 51289

- Columns: 客户编号 (TEXT), 产品类别 (TEXT), 产品 (TEXT), 浏览时间（分钟） (REAL), 点赞 (INTEGER), 分享 (INTEGER), 加入购物车 (INTEGER)

```json
[
  {
    "客户编号": "LS-001",
    "产品类别": "Auto & Accessories",
    "产品": "Car Media Players",
    "浏览时间（分钟）": 14.7,
    "点赞": 1,
    "分享": 1,
    "加入购物车": 1
  },
  {
    "客户编号": "IZ-002",
    "产品类别": "Auto & Accessories",
    "产品": "Car Speakers",
    "浏览时间（分钟）": 15.0,
    "点赞": 0,
    "分享": 0,
    "加入购物车": 1
  },
  {
    "客户编号": "EN-003",
    "产品类别": "Auto & Accessories",
    "产品": "Car Body Covers",
    "浏览时间（分钟）": 19.9,
    "点赞": 1,
    "分享": 1,
    "加入购物车": 1
  }
]
```


## 客户信息

- Rows: 51289

- Columns: 客户编号 (TEXT), 客户姓名 (TEXT), 客户细分群体 (TEXT), 城市 (TEXT), 州/省 (TEXT), 国家 (TEXT), 地区 (TEXT), 性别 (TEXT), 年龄 (INTEGER), 教育程度 (TEXT), 婚姻状况 (TEXT)

```json
[
  {
    "客户编号": "LS-001",
    "客户姓名": "Lane Daniels",
    "客户细分群体": "Consumer",
    "城市": "Brisbane",
    "州/省": "Queensland",
    "国家": "Australia",
    "地区": "Oceania",
    "性别": "Male",
    "年龄": 22,
    "教育程度": "Associate Degree",
    "婚姻状况": "Married"
  },
  {
    "客户编号": "IZ-002",
    "客户姓名": "Alvarado Kriz",
    "客户细分群体": "Home Office",
    "城市": "Berlin",
    "州/省": "Berlin",
    "国家": "Germany",
    "地区": "Central",
    "性别": "Male",
    "年龄": 32,
    "教育程度": "Bachelor",
    "婚姻状况": "Married"
  },
  {
    "客户编号": "EN-003",
    "客户姓名": "Moon Weien",
    "客户细分群体": "Consumer",
    "城市": "Porirua",
    "州/省": "Wellington",
    "国家": "New Zealand",
    "地区": "Oceania",
    "性别": "Male",
    "年龄": 21,
    "教育程度": "High School",
    "婚姻状况": "Single"
  }
]
```


## 订单信息

- Rows: 51289

- Columns: 客户编号 (TEXT), 订单编号 (TEXT), 订单日期 (TIMESTAMP), 月份 (TEXT), 运输方式 (TEXT), 产品类别 (TEXT), 产品 (TEXT), 销售额 (INTEGER), 数量 (TEXT), 折扣 (TEXT), 利润 (REAL), 运费 (TEXT), 订单优先级 (TEXT)

```json
[
  {
    "客户编号": "LS-001",
    "订单编号": "AU-2024-1",
    "订单日期": "2024-09-15 00:00:00",
    "月份": "Nov",
    "运输方式": "First Class",
    "产品类别": "Auto & Accessories",
    "产品": "Car Media Players",
    "销售额": 140,
    "数量": "2",
    "折扣": "0.05",
    "利润": 46.0,
    "运费": "4.6",
    "订单优先级": "Medium"
  },
  {
    "客户编号": "IZ-002",
    "订单编号": "AU-2024-2",
    "订单日期": "2024-06-30 00:00:00",
    "月份": "Jun",
    "运输方式": "First Class",
    "产品类别": "Auto & Accessories",
    "产品": "Car Speakers",
    "销售额": 211,
    "数量": "3",
    "折扣": "0.03",
    "利润": 112.0,
    "运费": "11.2",
    "订单优先级": "Medium"
  },
  {
    "客户编号": "EN-003",
    "订单编号": "AU-2024-3",
    "订单日期": "2024-05-15 00:00:00",
    "月份": "Dec",
    "运输方式": "First Class",
    "产品类别": "Auto & Accessories",
    "产品": "Car Body Covers",
    "销售额": 117,
    "数量": "5",
    "折扣": "0.01",
    "利润": 31.2,
    "运费": "3.1",
    "订单优先级": "Critical"
  }
]
```
