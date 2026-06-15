# OR_LNLG_MEDS

> This table contains the Medication information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 6  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the Line (ORM) record |
| 2 | `MEDICATION_DOSE` | NUMERIC |  | The dosage of the med. |
| 3 | `MEDICATION_UNIT_C_NAME` | VARCHAR | org | The number of units for the med. |
| 4 | `MEDICATION_ROUTE_C_NAME` | VARCHAR | org | The route of the med. |
| 5 | `MEDICATION_SITE_C_NAME` | VARCHAR | org | The site of the med. |
| 6 | `MED_SITE_LATER_C_NAME` | VARCHAR | org | The laterality of the site. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

