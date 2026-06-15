# DOCS_RCVD_PAT_STATUS

> This table is used for reporting on patients externally received deceased information.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `DECEASED_STAT_REFID` | VARCHAR |  | This item stores the unique reference identifier associated with the received deceased status |
| 6 | `DECEASED_PAT_LIVING_STAT_C_NAME` | VARCHAR |  | Holds status information to determine whether the patient is deceased or not |
| 7 | `DECEASED_DT_DATE` | DATETIME |  | Holds the reported date of death of the patient if known. It is null if the patient is reported as alive or the date of death isn't reported. |
| 8 | `DEC_STAT_SRC_CSN` | NUMERIC |  | This item holds the contact serial number of the source DXR record that owns this instance of the living status of the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

