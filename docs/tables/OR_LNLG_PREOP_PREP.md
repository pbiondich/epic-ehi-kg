# OR_LNLG_PREOP_PREP

> This table contains the Preop Prep information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `PREOP_PREP_LAT_C_NAME` | VARCHAR | org | The pre-op prep laterality. |
| 3 | `PREP_DRY_YN` | VARCHAR |  | This item stores whether or not the pre-op prep site was dry before draping. |
| 4 | `PREOP_CIRC_PREP_C_NAME` | VARCHAR |  | This item stores whether or not circumferential skin preparation was performed. |
| 5 | `PREP_DRY_START_DTTM` | DATETIME |  | This column contains information regarding when the site prep solution ended and when the drying time began. |
| 6 | `PREP_DRY_STOP_DTTM` | DATETIME |  | This column contains information regarding the time which the site was determined to be dry. |
| 7 | `PREP_SOLN_APPLIED_DATETIME` | DATETIME (UTC) |  | The time prep solution is applied. |
| 8 | `DRAPING_APPLIED_DATETIME` | DATETIME (UTC) |  | The time draping is applied. |
| 9 | `PREP_QUANTITY` | INTEGER |  | The quantity of items used during pre-op preparation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

