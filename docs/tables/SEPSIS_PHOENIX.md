# SEPSIS_PHOENIX

> This table stores information relating to the presence of Sepsis Phoenix in patient encounters. To qualify for Sepsis Phoenix, the patient must meet the qualifications for a body fluid culture, antibiotic administration, and a Phoenix score greater than or equal to 2.

**Primary key:** `INPATIENT_DATA_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the inpatient record. |
| 2 | `INFECTION_LOCAL_DTTM` | DATETIME (Local) |  | Stores the instant (local) the patient first met the pediatric Sepsis Phoenix's criteria for suspected infection. If the patient never met these criteria, this item will be null. |
| 3 | `TIME_ZERO_LOCAL_DTTM` | DATETIME (Local) |  | Stores the instant (local) the patient first met the pediatric Sepsis Phoenix's criteria for suspected infection, only if the patient also met the criteria for sepsis. If the patient never met these criteria, this item will be null. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

