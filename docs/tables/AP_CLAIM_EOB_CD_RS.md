# AP_CLAIM_EOB_CD_RS

> This table contains details regarding the resolution of claim codes for AP claims.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier of the accounts payable claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EOB_CODE_ID_EOB_CODE_NAME` | VARCHAR |  | The name of the processing code. |
| 4 | `RESOLUTION_C_NAME` | VARCHAR | org | The category identifier for the resolution specified when resolving the code. |
| 5 | `ENTRY_DATE` | DATETIME |  | The date the resolved code was added to the claim. |
| 6 | `ENTRY_USER_ID` | VARCHAR |  | The unique identifier of the user who added the resolved code to the claim. |
| 7 | `ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `RESOLUTION_DATE` | DATETIME |  | The date (without the time) the code was resolved from the claim. |
| 9 | `RESOLUTION_USER_ID` | VARCHAR |  | The unique identifier of the user who resolved the claim code. |
| 10 | `RESOLUTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `RESOLUTION_COMMENT` | VARCHAR |  | The comment specified when the code was added to the claim. |
| 12 | `RSLVD_EOB_CODE_ID_EOB_CODE_NAME` | VARCHAR |  | The name of the processing code. |
| 13 | `RSLVD_EOB_DATETIME` | DATETIME (Local) |  | The date and time when the code was added to the claim. |
| 14 | `RESOLUTION_DATETIME` | DATETIME (Local) |  | The date and time when the code was resolved. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

