# TRG_ADV_ORD_GROUPS

> This table stores information about the advanced order groups that are included in a treatment day of a treatment plan.

**Primary key:** `TREATMENT_DAY_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_DAY_ID` | NUMERIC | PK | The unique identifier for the patient order group record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DT` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ADV_ORD_GRP_CSN` | NUMERIC |  | The contact serial number (CSN) of an advanced order group (OSQ) record that is included in this treatment day. |
| 6 | `ADV_ORD_GRP_MODE_C_NAME` | VARCHAR |  | The mode of this advanced order group, such as Single-Select, Multi-Select, or Select-All. |
| 7 | `ADV_ORD_GRP_TITLE` | VARCHAR |  | The title of this advanced order group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

