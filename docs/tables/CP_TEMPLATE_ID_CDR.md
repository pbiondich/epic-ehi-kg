# CP_TEMPLATE_ID_CDR

> It stores the Care Plan template (LCE) ID and DAT used for this Care Plan.

**Primary key:** `CARE_INTG_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CARE_INTG_ID` | VARCHAR | PK FK→ | The unique identifier for the careplan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CP_TEMP_ID_TEMPLATE_NAME` | VARCHAR |  | The name of the care plan template record. |
| 4 | `CAREPLAN_TEMP_CDR` | FLOAT |  | The contact date, stored as a real number, for the Careplan template. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CARE_INTG_ID` | [CAREPLAN_INFO](CAREPLAN_INFO.md) | sole_pk | high |

