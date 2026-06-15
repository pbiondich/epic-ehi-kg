# AP_CLAIM_IF_PX_EDIT

> Edits applicable to the ICD procedure code.

**Primary key:** `CLAIM_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `PX_EDIT` | VARCHAR |  | Edits applicable to the ICD procedure code. |
| 5 | `PX_EDIT_1` | VARCHAR |  | The first procedure edit for this procedure line. |
| 6 | `PX_EDIT_2` | VARCHAR |  | The second procedure edit for this procedure line. |
| 7 | `PX_EDIT_3` | VARCHAR |  | The third procedure edit for this procedure line. |
| 8 | `PX_EDIT_4` | VARCHAR |  | The fourth procedure edit for this procedure line. |
| 9 | `PX_EDIT_5` | VARCHAR |  | The fifth procedure edit for this procedure line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

