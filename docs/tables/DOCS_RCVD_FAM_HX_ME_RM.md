# DOCS_RCVD_FAM_HX_ME_RM

> This table stores the other IDs for a family member from the DOCS_RCVD_FAM_HX_MEM table.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number of the associated family member in this record. Together with the FAMILY_MEMBER_REFRID column, this forms the foreign key to the DOCS_RCVD_FAM_HX_MEM table. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple family member IDs associated with the received document and the family member from the DOCS_RCVD_FAM_HX_MEM table. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `FAMILY_MMB_OTHERIDS` | VARCHAR |  | Other IDs of the family member for this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

