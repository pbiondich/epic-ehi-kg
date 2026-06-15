# MDL_RLNOTE_RW_INFO

> This table extracts related note reviewed information from the Medication Problem List master file.

**Primary key:** `MED_PRBLM_LIST_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_PRBLM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the med problem list record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REL_REVIEW_USER_ID` | VARCHAR |  | The ID of the user who reviewed the possibly related MDL notes. |
| 4 | `REL_REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MED_PRBLM_LIST_ID` | [MDL_MD_PRBLM_LIST](MDL_MD_PRBLM_LIST.md) | sole_pk | high |

