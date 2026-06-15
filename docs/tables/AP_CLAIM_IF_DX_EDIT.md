# AP_CLAIM_IF_DX_EDIT

> Diagnosis edits returned by the grouper/pricer.

**Primary key:** `CLAIM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `DX_EDIT` | VARCHAR |  | Diagnosis edits returned by the grouper/pricer. |
| 5 | `DX_EDIT_1` | VARCHAR |  | The first edit for the diagnosis line. |
| 6 | `DX_EDIT_2` | VARCHAR |  | The second edit for the diagnosis line. |
| 7 | `DX_EDIT_3` | VARCHAR |  | The third edit for the diagnosis line. |
| 8 | `DX_EDIT_4` | VARCHAR |  | The fourth edit for the diagnosis line. |
| 9 | `DX_EDIT_5` | VARCHAR |  | The fifth edit for the diagnosis line. |
| 10 | `DX_EDIT_6` | VARCHAR |  | The sixth edit for the diagnosis line. |
| 11 | `DX_EDIT_7` | VARCHAR |  | The seventh edit for the diagnosis line. |
| 12 | `DX_EDIT_8` | VARCHAR |  | The eighth edit for the diagnosis line. |
| 13 | `DX_EDIT_9` | VARCHAR |  | The ninth edit for the diagnosis line. |
| 14 | `DX_EDIT_10` | VARCHAR |  | The tenth edit for the diagnosis line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

