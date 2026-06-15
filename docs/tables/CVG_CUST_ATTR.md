# CVG_CUST_ATTR

> This table holds the coverage level custom attribute values.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CUST_ATTR_TYPE_C_NAME` | VARCHAR | org | Custom attribute value type indicator. |
| 4 | `CUST_ATTR_DT1_DT` | DATETIME |  | First date value for the custom attribute. |
| 5 | `CUST_ATTR_DT2_DT` | DATETIME |  | Second date value for the custom attribute. |
| 6 | `CUST_ATTR_CD1_C_NAME` | VARCHAR | org | First coded category value for the custom attribute. |
| 7 | `CUST_ATTR_CD2_C_NAME` | VARCHAR |  | Second coded category value for the custom attribute. |
| 8 | `CUST_ATTR_TXT1` | VARCHAR |  | First free-text value for the custom attribute. |
| 9 | `CUST_ATTR_TXT2` | VARCHAR |  | Second free-text value for the custom attribute. |
| 10 | `CUST_ATTR_NUM1` | NUMERIC |  | First numeric value for the custom attribute. |
| 11 | `CUST_ATTR_NUM2` | NUMERIC |  | Second numeric value for the custom attribute. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

