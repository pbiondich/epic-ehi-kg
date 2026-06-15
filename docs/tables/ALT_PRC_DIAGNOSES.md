# ALT_PRC_DIAGNOSES

> Diagnoses that are associated with Drug-Disease alerts.

**Primary key:** `ALERT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_ID` | NUMERIC | PK shared | This column stores the unique identifier of the alert record. You could link it to ALERT.ALT_ID to get patient and vendor information in table ALERT. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The Line Count |
| 4 | `CONTACT_DATE` | DATETIME |  | The date on which the encounter took place. |
| 5 | `PRC_DIAGNOSES_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

