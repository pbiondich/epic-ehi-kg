# AP_CLAIM_EOB_CD

> This table contains details regarding claim codes attached to AP claims.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier of the accounts payable claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EOB_CODE_ID_EOB_CODE_NAME` | VARCHAR |  | The name of the processing code. |
| 4 | `ENTRY_DATE` | DATETIME |  | The date the claim code was added to the claim. |
| 5 | `EOB_CODE_DATETIME` | DATETIME (Local) |  | The date and time this code was added to the claim. |
| 6 | `EOB_CODE_USER_ID` | VARCHAR |  | The unique identifier of the user who added the code to the claim. |
| 7 | `EOB_CODE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `EOB_CODE_COMMENT` | VARCHAR |  | The comment specified when the code was added to the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

