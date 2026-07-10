# SQLite 数据摘要

文件: `dacomp-001.sqlite`


## annual_rate_&_churn

- Rows: 29

- Columns: Annual Loan Interest Rate (REAL), Credit Rating A Customer Churn Rate (REAL), Credit Rating B Customer Churn Rate (REAL), Credit Rating C Customer Churn Rate (REAL)

```json
[
  {
    "Annual Loan Interest Rate": 0.04,
    "Credit Rating A Customer Churn Rate": 0.0,
    "Credit Rating B Customer Churn Rate": 0.0,
    "Credit Rating C Customer Churn Rate": 0.0
  },
  {
    "Annual Loan Interest Rate": 0.0425,
    "Credit Rating A Customer Churn Rate": 0.0945741262057566,
    "Credit Rating B Customer Churn Rate": 0.0667995833242854,
    "Credit Rating C Customer Churn Rate": 0.0687253064883727
  },
  {
    "Annual Loan Interest Rate": 0.0465,
    "Credit Rating A Customer Churn Rate": 0.135727183124787,
    "Credit Rating B Customer Churn Rate": 0.135052059550382,
    "Credit Rating C Customer Churn Rate": 0.122099028926699
  }
]
```


## ch___company_info

- Rows: 123

- Columns: Enterprise Code (TEXT), Company Name (TEXT), Credit Rating (TEXT), Defaulted (TEXT)

```json
[
  {
    "Enterprise Code": "E1",
    "Company Name": "*** Electrical Appliance Sales Co., Ltd.",
    "Credit Rating": "A",
    "Defaulted": "No"
  },
  {
    "Enterprise Code": "E2",
    "Company Name": "*** Technology Limited Liability Company",
    "Credit Rating": "A",
    "Defaulted": "No"
  },
  {
    "Enterprise Code": "E3",
    "Company Name": "*** Electronics (China) Co., Ltd. *** Branch",
    "Credit Rating": "C",
    "Defaulted": "No"
  }
]
```


## ch___input_invoices

- Rows: 210947

- Columns: Enterprise Code (TEXT), Invoice Number (INTEGER), Invoice Date (TIMESTAMP), Seller Organization Code (TEXT), Amount (REAL), Tax Amount (REAL), Amount Including Tax (REAL), Invoice Status (TEXT)

```json
[
  {
    "Enterprise Code": "E1",
    "Invoice Number": 3390939,
    "Invoice Date": "2017-07-18 00:00:00",
    "Seller Organization Code": "A00297",
    "Amount": -943.4,
    "Tax Amount": -56.6,
    "Amount Including Tax": -1000.0,
    "Invoice Status": "Valid Invoice"
  },
  {
    "Enterprise Code": "E1",
    "Invoice Number": 3390940,
    "Invoice Date": "2017-07-18 00:00:00",
    "Seller Organization Code": "A00297",
    "Amount": -4780.24,
    "Tax Amount": -286.81,
    "Amount Including Tax": -5067.05,
    "Invoice Status": "Valid Invoice"
  },
  {
    "Enterprise Code": "E1",
    "Invoice Number": 3390941,
    "Invoice Date": "2017-07-18 00:00:00",
    "Seller Organization Code": "A00297",
    "Amount": 943.4,
    "Tax Amount": 56.6,
    "Amount Including Tax": 1000.0,
    "Invoice Status": "Valid Invoice"
  }
]
```


## ch___sales_invoices

- Rows: 162484

- Columns: Enterprise Code (TEXT), Invoice Number (INTEGER), Invoice Date (TIMESTAMP), Buyer organization code (TEXT), Amount (REAL), Tax Amount (REAL), Amount Including Tax (REAL), Invoice Status (TEXT)

```json
[
  {
    "Enterprise Code": "E1",
    "Invoice Number": 11459356,
    "Invoice Date": "2017-08-04 00:00:00",
    "Buyer organization code": "B03711",
    "Amount": 9401.71,
    "Tax Amount": 1598.29,
    "Amount Including Tax": 11000.0,
    "Invoice Status": "Valid Invoice"
  },
  {
    "Enterprise Code": "E1",
    "Invoice Number": 5076239,
    "Invoice Date": "2017-08-09 00:00:00",
    "Buyer organization code": "B00844",
    "Amount": 8170.94,
    "Tax Amount": 1389.06,
    "Amount Including Tax": 9560.0,
    "Invoice Status": "Valid Invoice"
  },
  {
    "Enterprise Code": "E1",
    "Invoice Number": 5076240,
    "Invoice Date": "2017-08-09 00:00:00",
    "Buyer organization code": "B00844",
    "Amount": 8170.94,
    "Tax Amount": 1389.06,
    "Amount Including Tax": 9560.0,
    "Invoice Status": "Valid Invoice"
  }
]
```


## nch___company_info

- Rows: 302

- Columns: Enterprise Code (TEXT), Company Name (TEXT)

```json
[
  {
    "Enterprise Code": "E124",
    "Company Name": "Individual Business E124"
  },
  {
    "Enterprise Code": "E125",
    "Company Name": "Sole proprietorship E125"
  },
  {
    "Enterprise Code": "E126",
    "Company Name": "Sole proprietorship E126"
  }
]
```


## nch___input_invoices

- Rows: 395175

- Columns: Enterprise Code (TEXT), Invoice Number (INTEGER), Invoice Date (TEXT), Seller Organization Code (TEXT), Amount (REAL), Tax Amount (REAL), Amount Including Tax (REAL), Invoice Status (TEXT)

```json
[
  {
    "Enterprise Code": "E125",
    "Invoice Number": 34922128,
    "Invoice Date": "2018/5/1",
    "Seller Organization Code": "C02374",
    "Amount": 172.41,
    "Tax Amount": 27.59,
    "Amount Including Tax": 200.0,
    "Invoice Status": "Valid Invoice"
  },
  {
    "Enterprise Code": "E125",
    "Invoice Number": 33365900,
    "Invoice Date": "2018/5/15",
    "Seller Organization Code": "C02374",
    "Amount": 172.41,
    "Tax Amount": 27.59,
    "Amount Including Tax": 200.0,
    "Invoice Status": "Valid Invoice"
  },
  {
    "Enterprise Code": "E125",
    "Invoice Number": 79139197,
    "Invoice Date": "2018/5/20",
    "Seller Organization Code": "C02374",
    "Amount": 172.41,
    "Tax Amount": 27.59,
    "Amount Including Tax": 200.0,
    "Invoice Status": "Valid Invoice"
  }
]
```


## nch___sales_invoices

- Rows: 330835

- Columns: Enterprise Code (TEXT), Invoice Number (INTEGER), Invoice Date (TIMESTAMP), Buyer organization code (TEXT), Amount (REAL), Tax Amount (REAL), Amount Including Tax (REAL), Invoice Status (TEXT)

```json
[
  {
    "Enterprise Code": "E186",
    "Invoice Number": 368424,
    "Invoice Date": "2018-10-31 00:00:00",
    "Buyer organization code": "D02841",
    "Amount": 97087.38,
    "Tax Amount": 2912.62,
    "Amount Including Tax": 100000.0,
    "Invoice Status": "Valid Invoice"
  },
  {
    "Enterprise Code": "E186",
    "Invoice Number": 368448,
    "Invoice Date": "2018-10-31 00:00:00",
    "Buyer organization code": "D02841",
    "Amount": 97087.38,
    "Tax Amount": 2912.62,
    "Amount Including Tax": 100000.0,
    "Invoice Status": "Valid Invoice"
  },
  {
    "Enterprise Code": "E186",
    "Invoice Number": 368425,
    "Invoice Date": "2018-10-31 00:00:00",
    "Buyer organization code": "D02841",
    "Amount": 97087.38,
    "Tax Amount": 2912.62,
    "Amount Including Tax": 100000.0,
    "Invoice Status": "Valid Invoice"
  }
]
```
