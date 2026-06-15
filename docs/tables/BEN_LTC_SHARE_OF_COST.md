# BEN_LTC_SHARE_OF_COST

> The BEN_SHARE_OF_COST table contains the share of cost information for the attached benefit record.

**Primary key:** `BENEFIT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BENEFIT_ID` | NUMERIC | PK | The unique identifier (.1 item) for the benefits record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EFF_DATE` | DATETIME |  | This is the effective start date for a patient's share of cost. This is the monthly amount a patient must pay for certain payers (Medicaid, for example) to cover their stay. The share of cost amount may change over time. |
| 4 | `MONTHLY_AMT` | NUMERIC |  | This is the monthly patient pay amount for a patient's share of cost. This is the monthly amount a patient must pay for certain payers (Medicaid, for example) to cover their stay. The share of cost amount may change over time. |
| 5 | `UPDATE_USER_COMMENT` | VARCHAR |  | This is a user's comment for this share of cost line. |
| 6 | `UPDATE_USER_ID` | VARCHAR |  | When a line in the share of cost table changed, this the person who made the change. |
| 7 | `UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `UPDATE_UTC_DTTM` | DATETIME (UTC) |  | When a line in the share of cost table changed, this the instant (UTC) when the change was made. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

