# HH_VO_ENC

> Contains Home Health verbal order overtime single items information.

**Primary key:** `VERBAL_ORDER_ID`, `CONTACT_DATE_REAL`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VERBAL_ORDER_ID` | VARCHAR | PK FK→ | Unique identifier for the verbal order. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | Unique identifier for this contact for this patient. |
| 3 | `CONTACT_NUMBER` | VARCHAR |  | Contact number. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | ID of the contact owner deployment for this record. Links to table CL_COMMUNTY_INSTNC. |
| 6 | `INST_OF_EDIT` | DATETIME (Local) |  | Verbal order instant of edit. |
| 7 | `ENTRY_PERSON_ID` | VARCHAR |  | Name of user who entered contact data. Links to table CLARITY_EMP. |
| 8 | `ENTRY_PERSON_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VERBAL_ORDER_ID` | [HH_VO_INFO](HH_VO_INFO.md) | sole_pk | high |

