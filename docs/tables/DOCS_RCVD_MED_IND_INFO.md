# DOCS_RCVD_MED_IND_INFO

> This table stores indications of use info for medications.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `INDICATION_REF_ID` | VARCHAR |  | This item stores the reference ID for an indication associated with a medication |
| 6 | `IND_MED_REF_ID` | VARCHAR |  | This item stores the reference ID of the medication associated with the indication. |
| 7 | `INDICATION_ID` | NUMERIC |  | This item stores the Medical Condition ID of the indication associated with a medication. |
| 8 | `INDICATION_ID_MEDICAL_COND_NAME` | VARCHAR |  | This contains the name of the medical condition. |
| 9 | `INDICATION_NAME` | VARCHAR |  | This item stores the indication display name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

