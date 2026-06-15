# HSP_ACCT_RFND_TX

> This table contains refund transaction information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account that has related transaction information. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Each refund transaction will have its own line number. |
| 3 | `RFND_TX_ID` | NUMERIC |  | This column stores the unique identifier for the refund transaction associated with the hospital account. |
| 4 | `RFND_TX_UPDATE_DT` | DATETIME |  | The date of the last update of the refund transaction associated with the hospital account. |
| 5 | `REFUND_TX_STATUS_C_NAME` | VARCHAR |  | The status of the refund transaction associated with the hospital account. i.e. 1-Posted 2-Exported 3-Comment Imported - Approved 4-Comment Imported - Rejected 5-Reversed |
| 6 | `REFUND_AMOUNT_SENT` | NUMERIC |  | The amount of the refund associated with the hospital account. |
| 7 | `REFUND_REF_NUMBER` | VARCHAR |  | The reference number of the refund associated with the hospital account. |
| 8 | `REFUND_IP_COMMENT` | VARCHAR |  | Import comment for the refund associated with the hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

