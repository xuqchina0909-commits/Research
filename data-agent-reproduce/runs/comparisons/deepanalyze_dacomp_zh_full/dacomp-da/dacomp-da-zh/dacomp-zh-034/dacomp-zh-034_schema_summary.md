# SQLite 数据摘要

文件: `dacomp-zh-034.sqlite`


## 附件1

- Rows: 611200

- Columns: create_dt (TIMESTAMP), order_id (INTEGER), sku_id (INTEGER), sku_name (TEXT), is_finished (INTEGER), sku_cnt (INTEGER), sku_prc (REAL), sku_sale_prc (REAL), sku_cost_prc (REAL), upc_code (REAL)

```json
[
  {
    "create_dt": "2018-12-04 00:00:00",
    "order_id": 100001000000000,
    "sku_id": 2005932936,
    "sku_name": "金龙鱼 葵花籽清香型调和油 5L",
    "is_finished": 1,
    "sku_cnt": 1,
    "sku_prc": 39.8,
    "sku_sale_prc": 39.8,
    "sku_cost_prc": 0.0,
    "upc_code": 6948200000000.0
  },
  {
    "create_dt": "2016-11-30 00:00:00",
    "order_id": 628898000000000,
    "sku_id": 2005508919,
    "sku_name": "进口 香蕉 约1kg",
    "is_finished": 1,
    "sku_cnt": 1,
    "sku_prc": 8.8,
    "sku_sale_prc": 8.8,
    "sku_cost_prc": 0.0,
    "upc_code": 2400000000000.0
  },
  {
    "create_dt": "2016-11-30 00:00:00",
    "order_id": 628898000000000,
    "sku_id": 2004962651,
    "sku_name": "伊利 畅轻风味发酵乳 燕麦+芒果味酸奶 250g",
    "is_finished": 1,
    "sku_cnt": 1,
    "sku_prc": 7.5,
    "sku_sale_prc": 7.5,
    "sku_cost_prc": 0.0,
    "upc_code": 6907990000000.0
  }
]
```


## 附件1&附件2 字段说明

- Rows: 11

- Columns: 字段名 (TEXT), 字段注释 (TEXT), 字段定义 (TEXT), 字段类型 (TEXT), 涉密等级 (TEXT), 创建时间 (TEXT), 更新时间 (TEXT), 是否有效 (TEXT)

```json
[
  {
    "字段名": "order_id",
    "字段注释": "订单ID",
    "字段定义": "订单ID",
    "字段类型": "bigint",
    "涉密等级": "第四安全等级",
    "创建时间": "2017-05-17 13:15:32.0",
    "更新时间": "2018-07-06 09:06:40.0",
    "是否有效": "是"
  },
  {
    "字段名": "is_finished",
    "字段注释": "是否完成",
    "字段定义": "订单状态为4时值为1，否则为0",
    "字段类型": "int",
    "涉密等级": "第四安全等级",
    "创建时间": "2017-05-17 13:15:32.0",
    "更新时间": "2018-07-06 09:06:40.0",
    "是否有效": "是"
  },
  {
    "字段名": "sku_id",
    "字段注释": "商品ID",
    "字段定义": "商品ID",
    "字段类型": "string",
    "涉密等级": "第四安全等级",
    "创建时间": "2017-05-17 13:15:32.0",
    "更新时间": "2018-07-06 09:06:40.0",
    "是否有效": "是"
  }
]
```


## 附件2

- Rows: 610655

- Columns: create_dt (TIMESTAMP), order_id (INTEGER), sku_id (INTEGER), sku_name (TEXT), is_finished (INTEGER), sku_cnt (INTEGER), sku_prc (REAL), sku_sale_prc (REAL), sku_cost_prc (REAL), upc_code (REAL)

```json
[
  {
    "create_dt": "2017-07-22 00:00:00",
    "order_id": 717481014000141,
    "sku_id": 2006544612,
    "sku_name": "吉香居 组合装 风味豆豉 280g*2",
    "is_finished": 1,
    "sku_cnt": 1,
    "sku_prc": 12.8,
    "sku_sale_prc": 10.9,
    "sku_cost_prc": 10.9,
    "upc_code": 6926896703594.0
  },
  {
    "create_dt": "2017-07-22 00:00:00",
    "order_id": 717481014000141,
    "sku_id": 2008180827,
    "sku_name": "伊利 优酸乳果粒酸奶饮品哈密瓜味 245g*12",
    "is_finished": 1,
    "sku_cnt": 1,
    "sku_prc": 42.0,
    "sku_sale_prc": 29.5,
    "sku_cost_prc": 29.5,
    "upc_code": 6907992513126.0
  },
  {
    "create_dt": "2017-07-22 00:00:00",
    "order_id": 717484722000342,
    "sku_id": 2005526101,
    "sku_name": "优选五花肉 约500g",
    "is_finished": 1,
    "sku_cnt": 1,
    "sku_prc": 18.8,
    "sku_sale_prc": 18.8,
    "sku_cost_prc": 0.0,
    "upc_code": 2400002413071.0
  }
]
```


## 附件3

- Rows: 1048575

- Columns: id (REAL), promotion_info_id (REAL), promotion_no (TEXT), sku_id (REAL), sku_name (TEXT), promotion_price (REAL), pdj_price (REAL), begin_time (TEXT), end_time (TEXT), limit_count (REAL), sale_count (REAL), state (REAL), sys_version (TEXT), create_time (TEXT), update_time (TEXT), create_pin (TEXT), update_pin (TEXT), yn (REAL), ts (TEXT), begin_state (REAL), end_state (REAL), cost_price (REAL), allowance (REAL), business_version (REAL), promotion_type (REAL), time_id (REAL), create_dt (TIMESTAMP)

```json
[
  {
    "id": 158219382.0,
    "promotion_info_id": 5200661.0,
    "promotion_no": "\\N",
    "sku_id": 2008180830.0,
    "sku_name": "蒙牛 巴氏杀菌热处理风味酸牛奶（经典原味） 200g*16盒",
    "promotion_price": 51.0,
    "pdj_price": 88.0,
    "begin_time": "2017/9/9 9:00",
    "end_time": "2017/9/10 20:00",
    "limit_count": 500.0,
    "sale_count": 38.0,
    "state": 5.0,
    "sys_version": "\\N",
    "create_time": "2017/9/7 17:06",
    "update_time": "2017/9/7 17:06",
    "create_pin": "81372",
    "update_pin": "SYSTEM",
    "yn": 0.0,
    "ts": "2017/9/11 13:20",
    "begin_state": 0.0,
    "end_state": 0.0,
    "cost_price": 51.0,
    "allowance": 0.0,
    "business_version": 310.0,
    "promotion_type": 4.0,
    "time_id": 20170900000000.0,
    "create_dt": "2017-09-07 00:00:00"
  },
  {
    "id": 158231606.0,
    "promotion_info_id": 5200754.0,
    "promotion_no": "\\N",
    "sku_id": 2008851057.0,
    "sku_name": "鲜美来 黑椒鱼排 130g",
    "promotion_price": 9.9,
    "pdj_price": 13.8,
    "begin_time": "2017/9/9 9:00",
    "end_time": "2017/9/10 20:00",
    "limit_count": 20.0,
    "sale_count": 10.0,
    "state": 5.0,
    "sys_version": "\\N",
    "create_time": "2017/9/7 17:43",
    "update_time": "2017/9/7 17:43",
    "create_pin": "81372",
    "update_pin": "SYSTEM",
    "yn": 0.0,
    "ts": "2017/9/11 13:19",
    "begin_state": 0.0,
    "end_state": 0.0,
    "cost_price": 9.9,
    "allowance": 0.0,
    "business_version": 310.0,
    "promotion_type": 4.0,
    "time_id": 20170900000000.0,
    "create_dt": "2017-09-07 00:00:00"
  },
  {
    "id": 158147701.0,
    "promotion_info_id": 5196604.0,
    "promotion_no": "\\N",
    "sku_id": 2007007666.0,
    "sku_name": "特仑苏 新西兰进口 环球精选纯牛奶 250g*12",
    "promotion_price": 49.5,
    "pdj_price": 88.0,
    "begin_time": "2017/9/7 9:00",
    "end_time": "2017/9/13 20:00",
    "limit_count": 500.0,
    "sale_count": 119.0,
    "state": 5.0,
    "sys_version": "\\N",
    "create_time": "2017/9/7 8:46",
    "update_time": "2017/9/7 8:46",
    "create_pin": "81372",
    "update_pin": "SYSTEM",
    "yn": 0.0,
    "ts": "2017/9/13 20:00",
    "begin_state": 0.0,
    "end_state": 0.0,
    "cost_price": 49.5,
    "allowance": 0.0,
    "business_version": 310.0,
    "promotion_type": 4.0,
    "time_id": 20170900000000.0,
    "create_dt": "2017-09-07 00:00:00"
  }
]
```


## 附件3 字段说明

- Rows: 36

- Columns: 字段名 (TEXT), 字段释义 (TEXT), Explanation (TEXT)

```json
[
  {
    "字段名": "id",
    "字段释义": "无效字段",
    "Explanation": "Invalid term"
  },
  {
    "字段名": "promotion_info_id",
    "字段释义": "促销信息编号",
    "Explanation": null
  },
  {
    "字段名": "promotion_no",
    "字段释义": "促销编号",
    "Explanation": null
  }
]
```


## 附件4

- Rows: 6570

- Columns: sku_id (INTEGER), sku_name (TEXT), first_category_id (INTEGER), second_category_id (INTEGER), third_category_id (INTEGER), first_category_name (TEXT), second_category_name (TEXT), third_category_name (TEXT)

```json
[
  {
    "sku_id": 2003117399,
    "sku_name": "喜之郎蜜桔果肉果冻杯200g/杯",
    "first_category_id": 20514,
    "second_category_id": 20607,
    "third_category_id": 20617,
    "first_category_name": "休闲食品",
    "second_category_name": "果冻",
    "third_category_name": "果肉果冻"
  },
  {
    "sku_id": 2003117402,
    "sku_name": "M&M'S 牛奶巧克力豆 40g",
    "first_category_id": 20514,
    "second_category_id": 20702,
    "third_category_id": 20712,
    "first_category_name": "休闲食品",
    "second_category_name": "巧克力",
    "third_category_name": "加味巧克力"
  },
  {
    "sku_id": 2003117403,
    "sku_name": "健达 奇趣蛋可可球及牛奶可可酱糖果女生版（含新奇玩具） 20g",
    "first_category_id": 21549,
    "second_category_id": 23268,
    "third_category_id": 23272,
    "first_category_name": "进口商品",
    "second_category_name": "进口休闲食品",
    "third_category_name": "进口糖果/巧克力"
  }
]
```


## 附件4 字段说明

- Rows: 8

- Columns: 字段名 (TEXT), 字段释义 (TEXT)

```json
[
  {
    "字段名": "skuid",
    "字段释义": "sku编号"
  },
  {
    "字段名": "skuname",
    "字段释义": "sku名称"
  },
  {
    "字段名": "first_category_id",
    "字段释义": "一级类目id"
  }
]
```
