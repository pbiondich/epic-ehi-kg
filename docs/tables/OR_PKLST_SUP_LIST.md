# OR_PKLST_SUP_LIST

> The OR_PKLST_SUP_LIST table contains OR management system pick list supply list.

**Primary key:** `PICK_LIST_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PICK_LIST_ID` | VARCHAR | PK FK→ | The unique internal ID of the pick list record. |
| 2 | `LINE` | INTEGER | PK | The total number of lines of supply information in the pick list. |
| 3 | `STATIC_UDI` | VARCHAR |  | Static device identifier |
| 4 | `STATIC_UDI_TYPE_C_NAME` | VARCHAR |  | Static device identifier type |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PICK_LIST_ID` | [OR_PKLST](OR_PKLST.md) | sole_pk | high |

