# HSP_TX_RFNDEXP

> This table contains information in the refund transaction that gets filed after its temporary transaction gets imported back from the AP system which processes it. This table contains information that is related to the AP system and the actions taken by it during the processing of the temporary transaction.

**Primary key:** `TX_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account with which a hospital billing transaction is associated. |
| 3 | `RFND_AP_DATE` | DATETIME |  | Stores the date on which the A/P system processed the temporary transaction. |
| 4 | `RFND_AP_STATUS_C_NAME` | VARCHAR |  | Stores the action taken by the A/P system when it processed the temporary transaction. |
| 5 | `RFND_AMT` | NUMERIC |  | The amount of the refund associated with the refund transaction. |
| 6 | `REFERENCE_NUM` | VARCHAR |  | The reference number of the refund associated with the transaction. This reference number is sent back by the AP system after it processed the temporary transaction. |
| 7 | `TX_COMMENT` | VARCHAR |  | This column stores the import comment for the refund associated with the hospital billing transaction. This comment is sent back by the billing system after it processed the hospital temporary transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

