# CASE_CONTACT_INFO

> This table contains information about the case contacts.

**Primary key:** `CASE_ID`, `CONTACT_DATE_REAL`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The internal ID of the case record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `CONTACT_DATE` | DATETIME |  | Contact date in external format |
| 4 | `CONTACT_TYPE_C_NAME` | VARCHAR | org | The contact type category ID for the case event. |
| 5 | `CONTACT_SEVERITY_C_NAME` | VARCHAR | org | The contact severity category ID for the case event. |
| 6 | `REVIEWED_DATE` | DATETIME |  | Date the contact was reviewed |
| 7 | `REVIEWED_BY_USER_ID` | VARCHAR |  | User who reviewed the contact |
| 8 | `REVIEWED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `CONTACT_SUMMARY` | VARCHAR |  | The case contact summary. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

