# ORD_REC_RMD_LTR

> Contains information about the reminder letters sent for a recommendation.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier of the finding record associated with this recommendation letter. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REMINDER_LTR_DT` | DATETIME |  | The date on which a reminder letter was sent to the patient. |
| 4 | `LETTER_TMPL_ID` | VARCHAR |  | Letter template used to print reminder letter |
| 5 | `LETTER_TMPL_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 6 | `RIS_LETTER_TYPE_C_NAME` | VARCHAR | org | The batch letter type category number for the reminder letter. This prevents multiple letters of the same type from printing. |
| 7 | `MAM_REMINDER_LET_ID` | VARCHAR |  | The ID of the note that contains the letter text |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

