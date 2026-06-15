# OR_LNLG_PSTOP_PREP

> This table contains the Postop Prep information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 5  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `POSTOP_PREP_AREA_C_NAME` | VARCHAR | org | The post-op prep area for a patient. |
| 3 | `POSTOP_PREP_LAT_C_NAME` | VARCHAR | org | The post-op prep laterality. |
| 4 | `LINKED_LDA_ID` | VARCHAR |  | This item stores the ID of the Line, Drain, or Airway (LDA) record created from this site completion documentation. |
| 5 | `POSTOP_COMP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

