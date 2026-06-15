# MASS_DEPTH

> This table holds information about the depth of a mass documented within the mammography drawing tools if QuickForms are being utilized. SmartForms within the drawing tools will file data to the SmartData Element structures.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEPTH_C_NAME` | VARCHAR | org | The depth category ID for the mass finding documented in the BI-RADS questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

