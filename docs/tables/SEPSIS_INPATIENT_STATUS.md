# SEPSIS_INPATIENT_STATUS

> This table contains a patient's sepsis early detection and protocol status.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the inpatient record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SEPSIS_STATUS_C_NAME` | VARCHAR |  | This item stores a history of the patient's sepsis early detection and protocol status, as determined by GetSepsisStatus^JSEPSIS. |
| 4 | `SEPSIS_STATUS_UTC_DTTM` | DATETIME (UTC) |  | This item stores the UTC instant when a patient's sepsis status changed, as determined by GetSepsisStatus^JSEPSIS. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

