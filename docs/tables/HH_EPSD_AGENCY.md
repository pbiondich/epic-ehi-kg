# HH_EPSD_AGENCY

> This table contains episode-level agency information. It stores user-entered information about the outside agencies that will be assisting the patient while the patient is under Home Health care. This information is entered in the Referral Info 2 form as part of an Intake contact.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | Unique identifier for the episode. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AGENCY_C_NAME` | VARCHAR | org | Link to custom category list of agencies, ZC_AGENCY. |
| 4 | `AGENCY_PHONE` | VARCHAR |  | Agency phone number. |
| 5 | `AGENCY_CONTACT` | VARCHAR |  | Agency contact person. |
| 6 | `AGENCY_COMMENT` | VARCHAR |  | Agency comment text entered by a user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

