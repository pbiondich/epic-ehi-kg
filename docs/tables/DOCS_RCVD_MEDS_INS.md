# DOCS_RCVD_MEDS_INS

> This item stores medications received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number of the medication insurance in the received document. Together with DOCUMENT_ID and CONTACT_DATE_REAL, this forms the foreign key to the DOCS_RCVD_MEDS table. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple medication insurances associated with the received document and the medication from the DOCS_RCVD_MEDS table. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `MED_PAT_INSTR` | VARCHAR |  | This item stores the patient instructions associated with the med. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

