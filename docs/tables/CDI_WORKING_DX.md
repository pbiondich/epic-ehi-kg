# CDI_WORKING_DX

> The CDI_WORKING_DX table contains information related to working diagnoses for a Clinical Documentation Improvement (CDI) review.

**Primary key:** `CODING_RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CODING_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the clinical documentation improvement (CDI) review record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the diagnosis associated with this contact. If the line number is one, the related diagnosis is the principal diagnosis. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CDI_WKG_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `CDI_WKG_DX_POA_C_NAME` | VARCHAR | org | The Present on Admission (POA) value for a working diagnosis on the clinical documentation improvement (CDI) review. |
| 7 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The unique ID of the contact that this coding record is associated with. |
| 8 | `CDI_WKG_DX_CC_C_NAME` | VARCHAR |  | The (Major) Complication / Comorbidity status for a working diagnoses in the Clinical Documentation Improvement (CDI) review. |
| 9 | `WKG_DX_HAC_YN` | VARCHAR |  | The Hospital-Acquired Condition (HAC) category this working diagnosis qualifies for, if any. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

