# LAB_COSIGN_INFO

> The LAB_COSIGN_INFO table contains cosign information for lab results.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `COSINGER_ID` | VARCHAR |  | The unique identifier of the users who have cosigned the lab result. |
| 6 | `COSINGER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `AP_BILLABLE_YN` | VARCHAR |  | Indicates whether the related cosigner is a pathologist who can charge for the Anatomic Pathology result that he/she cosigned. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

