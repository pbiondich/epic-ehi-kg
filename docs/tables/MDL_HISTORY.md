# MDL_HISTORY

> The MDL_HISTORY table enables you to report on Medication Problem List history information over time.

**Primary key:** `MED_PRBLM_LIST_ID`, `CONTACT_DATE_REAL`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_PRBLM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the med problem list record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this contact in your system. The integer portion of the number specifies the date of the contact. The digits after the decimal point indicate multiple contacts on one day. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `LNG_TRM_OVERTIME_YN` | VARCHAR |  | The changes to the long-term indicator over time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MED_PRBLM_LIST_ID` | [MDL_MD_PRBLM_LIST](MDL_MD_PRBLM_LIST.md) | sole_pk | high |

