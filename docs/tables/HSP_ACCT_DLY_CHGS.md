# HSP_ACCT_DLY_CHGS

> This table contains hospital account daily charge information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. As multiple daily charges can be performed on one hospital account, each daily charge will have a unique line number. |
| 3 | `DLY_CHG_STS_HA_C_NAME` | VARCHAR |  | The status of a daily charge associated with the hospital account. Choices are Scheduled, Active, Completed, or Cancelled. |
| 4 | `DLY_CHG_START_DATE` | DATETIME |  | The start date of a daily charge associated with the hospital account. |
| 5 | `DLY_CHG_END_DATE` | DATETIME |  | The end date of a daily charge associated with the hospital account. |
| 6 | `DLY_CHG_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 7 | `DLY_CHG_PROC_DESC` | VARCHAR |  | The description of a daily charge associated with the hospital account. |
| 8 | `DLY_CHG_QUANTITY` | INTEGER |  | The quantity of a daily charge associated with the hospital account. This is the quantity of a single procedure that the system will post each day for which the procedure is scheduled as a daily charge. |
| 9 | `DLY_CHG_AMOUNT` | NUMERIC |  | The monetary amount of a daily charge associated with the hospital account. |
| 10 | `DLY_CHG_COMMENT` | VARCHAR |  | A comment on a daily charge associated with the hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

