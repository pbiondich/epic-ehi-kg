# POC_SNAPSHOT_INFO

> This table contains information pertaining to PDF snapshots for a plan of care.

**Primary key:** `POC_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `POC_ID` | NUMERIC | PK | The unique identifier (.1 item) for the plan of care record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `SNAPSHOT_PDFS_DOCUMENT_ID` | VARCHAR |  | A list of document IDs that point to different versions of PDF snapshots of the plan. |
| 6 | `SNAPSHOT_ERTFS_NOTE_CSN_ID` | NUMERIC |  | This item contains a list of note CSNs that correspond to different versions of ERTF snapshots of the plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

