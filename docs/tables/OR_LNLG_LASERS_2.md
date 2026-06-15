# OR_LNLG_LASERS_2

> This table contains the laser information for the surgical log (ORL).

**Overflow of:** [OR_LNLG_LASERS](OR_LNLG_LASERS.md)  
**Primary key:** `RECORD_ID`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LASER_SPOT_SIZE` | NUMERIC |  | The laser spot size. |
| 3 | `LASER_SPOT_SIZE_UNIT_C_NAME` | VARCHAR | org | The laser spot size unit. |
| 4 | `LASER_FLUENCE` | INTEGER |  | The laser fluence. |
| 5 | `LASER_TOTAL_TORSION_TIME` | NUMERIC |  | This item stores the total torsional time. |
| 6 | `LASER_TOTAL_LINEAR_TIME` | NUMERIC |  | This item stores the total linear time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

