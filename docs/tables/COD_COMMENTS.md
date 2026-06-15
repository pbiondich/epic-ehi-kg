# COD_COMMENTS

> The hospital account coding comments metadata.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier for the hospital account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COD_CMT_USER_ID` | VARCHAR |  | User who wrote the comments regarding the coding of the account |
| 4 | `COD_CMT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `COD_CMT_UTC_DTTM` | DATETIME (UTC) |  | Instant the comments regarding the coding of the account were written |
| 6 | `COD_CMT_START_LN` | INTEGER |  | This column stores the start line of the comment stored on the hospital account record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

