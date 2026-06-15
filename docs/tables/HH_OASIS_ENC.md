# HH_OASIS_ENC

> Contains Home Health Outcome and Assessment Information Set (OASIS) and Hospice Item Set (HIS) overtime single items.

**Primary key:** `OASIS_SET_ID`, `CONTACT_DATE_REAL`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OASIS_SET_ID` | NUMERIC | PK FK→ | Unique identifier for the OASIS data set. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | Unique identifier for this contact for this patient. |
| 3 | `CONTACT_NUM` | INTEGER |  | Contact number. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `INSTANT_OF_ENTRY` | DATETIME (Local) |  | Instant of OASIS data set data entry. |
| 6 | `DATA_ENTRY_PERSON` | VARCHAR |  | Name of user who entered data in OASIS data set. |
| 7 | `DATASET_CONTACT_TYPE_C_NAME` | VARCHAR |  | This item stores the OASIS/HIS dataset type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OASIS_SET_ID` | [HH_OASIS_INFO](HH_OASIS_INFO.md) | sole_pk | high |

