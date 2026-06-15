# IMM_ADMIN_COMPONENTS

> The IMM_ADMIN_COMPONENTS table contains information about the components of the immunization administered. The rows included in this table are items from DXR (Document) masterfile which include information on type of immunization, dose validity, immunization schedule, and a unique reference identifier to identify a specific instance of an immunization.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `IMM_COMP_ID` | VARCHAR |  | The unique identifier for the immunization component. |
| 6 | `IMM_REFERENCE_ID` | VARCHAR |  | The unique reference identifier for the specific instance of an immunization that the component is part of. |
| 7 | `IMM_COMP_GROUP_ID` | NUMERIC |  | The unique ID of the vaccine group for an immunization administration received from an external system. This can be either the component or the family of a vaccine. |
| 8 | `IMM_COMP_GROUP_ID_NAME` | VARCHAR |  | The name of the immunization. |
| 9 | `IMM_COMP_GROUP_FT` | VARCHAR |  | The free text value for a vaccine group for an immunization administration received from an external system. This can be either the component or the family of a vaccine. |
| 10 | `IMM_COMP_SCHED_ID_FT` | VARCHAR |  | The immunization schedule identifier used for the administered vaccination component. |
| 11 | `IMM_COMP_SCHED_NAME_FT` | VARCHAR |  | The immunization schedule name used for the administered vaccination component. |
| 12 | `IMM_COMP_SCHED_CODING_FT` | VARCHAR |  | The immunization schedule coding system used for the administered vaccination component. |
| 13 | `IMM_COMP_SCHED_VALID_YN` | VARCHAR |  | Whether or not the administered component dose was valid for the given schedule |
| 14 | `IMM_COMP_VALID_RSN_C_NAME` | VARCHAR | org | The description of why the given administration component is valid or invalid based on its immunization schedule. |
| 15 | `IMM_COMP_VALID_RSN_FT` | VARCHAR |  | The free text description of why the given administration component is valid or invalid based on its immunization schedule. |
| 16 | `IMM_COMP_SCHED_DOSE_NUM` | VARCHAR |  | Dose number for this component in the immunization series. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

