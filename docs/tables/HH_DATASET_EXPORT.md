# HH_DATASET_EXPORT

> This stores data for Outcome and Assessment Information Set (OASIS) or Hospice Item Set (HIS) data set exports.

**Primary key:** `DATASET_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DATASET_ID` | NUMERIC | PK shared | The unique identifier for the data set record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXPORT_TYPE_C_NAME` | VARCHAR | org | This item stores the type of export in the export history of an OASIS or HIS record. |
| 4 | `EXPORT_USER_ID` | VARCHAR |  | This item stores the exporting user in the export history of an OASIS or HIS record. |
| 5 | `EXPORT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `EXPORT_INSTANT_DTTM` | DATETIME (UTC) |  | This item stores the instant of export in the export history of an OASIS or HIS record. |
| 7 | `EXPORT_SNAPSHOT_DAT` | VARCHAR |  | The contact pointer to the OASIS snapshot data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

