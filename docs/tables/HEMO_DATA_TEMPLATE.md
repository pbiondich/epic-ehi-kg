# HEMO_DATA_TEMPLATE

> This table contains the versioning information for the hemodynamic data entry templates used to document the hemodynamic measurement values for an invasive procedure. The hemodynamic data entry tables are LQF records.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HEMO_TEMPLATE_FORM_ID` | VARCHAR |  | Stores the hemodynamics template ids for this study. |
| 4 | `HEMO_TEMPLATE_FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 5 | `HEMO_TEMPLATE_DAT` | FLOAT |  | Stores the version of hemodynamics templates used for this study. |
| 6 | `HEMO_TEMPLATE_DATE_REAL` | FLOAT |  | Stores the unique contact date in decimal format for the hemodynamics template record in this row. This corresponds to the CONTACT_DATE_REAL column in the TMPLT_NESTED_COMPONENTS table. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

