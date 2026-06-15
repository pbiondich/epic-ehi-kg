# CAPTURE_THRESHOLD

> This table contains information regarding related items for capture threshold.

**Primary key:** `IMPLANT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the implant record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `LEAD_PSA_THRESH_R` | NUMERIC |  | This item holds the lead PSA threshold for a related group. |
| 6 | `CAPTURE_THRESH_CMT` | VARCHAR |  | This item holds the threshold comment for a related group. |
| 7 | `THRSHOLD_UNABLE_R_C_NAME` | VARCHAR | org | This item holds whether the threshold was able to be obtained for a related group. |
| 8 | `PCMKR_AT_LD_PLS_DUR` | NUMERIC |  | This item holds the pulse duration for pacemaker atrial lead for a related group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

