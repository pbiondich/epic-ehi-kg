# SPEC_AP_PROC_CHRG

> This is the specimen protocol charge table for anatomic pathology specimens.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AP_PRO_CHARGE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `AP_PRO_CHARGE_QTY` | NUMERIC |  | This will save the specimen-level protocol charge quantity for the anatomic pathology specimen. |
| 5 | `AP_CHG_TR_STAT_C_NAME` | VARCHAR |  | The charge trigger status category ID for the anatomic pathology (AP) protocol level charge. |
| 6 | `CHARGE_SS_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 7 | `CHARGE_QTY_SS` | INTEGER |  | The quantity associated with the last dropped charge (CHARGE_SS_PROC_ID) for the AP specimen. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

