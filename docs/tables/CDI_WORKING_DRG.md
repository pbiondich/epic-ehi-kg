# CDI_WORKING_DRG

> This table contains information about the Diagnosis Related Group (DRG) data stored as part of a Clinical Documentation Improvement (CDI) review. Each contact in this table corresponds to DRG data from one CDI review.

**Primary key:** `CODING_RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CODING_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the clinical documentation improvement (CDI) review record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CDI_WORKING_DRG_ID` | VARCHAR |  | The working diagnosis-related group (DRG) for a particular clinical documentation improvement (CDI) review. |
| 6 | `CDI_WORKING_DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 7 | `CDI_DRG_REIMBURSE` | NUMERIC |  | The expected reimbursement for a working diagnosis-related group (DRG) on the clinical documentation improvement (CDI) review. |
| 8 | `CDI_DRG_WEIGHT` | NUMERIC |  | The weight of a working diagnosis-related group (DRG) on the clinical documentation improvement (CDI) review. |
| 9 | `CDI_DRG_TYPE_ID` | NUMERIC |  | The diagnosis-related group (DRG) type of a working diagnosis-related group on the clinical documentation improvement (CDI) review. |
| 10 | `CDI_DRG_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 11 | `CDI_DRG_SOI_C_NAME` | VARCHAR |  | The Severity of Illness (SOI) value of a working diagnosis-related group (DRG) on the clinical documentation improvement (CDI) review. |
| 12 | `CDI_DRG_ROM_C_NAME` | VARCHAR |  | The Risk of Mortality (ROM) value for a working diagnosis-related group (DRG) on the clinical documentation improvement (CDI) review. |
| 13 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The unique ID of the contact that this coding record is associated with. |
| 14 | `CDI_DRG_AMLOS` | NUMERIC |  | The arithmetic mean length of stay for the working diagnosis related group in the Clinical Documentation Improvement (CDI) review. |
| 15 | `CDI_DRG_GMLOS` | NUMERIC |  | The geometric mean length of stay for the working diagnosis related group in the Clinical Documentation Improvement (CDI) review. |
| 16 | `DRG_QUALIFIER_C_NAME` | VARCHAR | org | The qualifier for the working diagnosis related group in the Clinical Documentation Improvement (CDI) review. |
| 17 | `CDI_DRG_COMP_FLAG_YN` | VARCHAR |  | This column indicates if the diagnosis-related group (DRG) is used for comparison purposes. |
| 18 | `DRG_IS_CMI_EXCLUD_YN` | VARCHAR |  | Indicates whether a DRG code from a DRG type is excluded from CMI calculation on CDI. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

