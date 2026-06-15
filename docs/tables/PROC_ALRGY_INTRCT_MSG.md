# PROC_ALRGY_INTRCT_MSG

> This table contains procedure-allergy interaction details.

**Primary key:** `MSG_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique identifier for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROC_INTRCT_ORD_ID` | NUMERIC |  | Stores the order ID that interacts with the documented allergy. |
| 4 | `PROC_INTRCT_ELG` | VARCHAR |  | Stores the allergen associated with a procedure that interacts with a patient's documented allergies. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |

