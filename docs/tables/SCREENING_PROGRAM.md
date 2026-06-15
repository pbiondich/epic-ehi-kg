# SCREENING_PROGRAM

> This table contains information about screening program assessment data. This includes the program type, as well as the assessment kind, location, and value. The records in this table are Orders (ORD) records that are exams within a screening program.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PROGRAM_C_NAME` | VARCHAR |  | The screening program category ID for the screening program being documented, such as Breast Screening or Lung Screening. |
| 6 | `ASSESSMENT_KIND_C_NAME` | VARCHAR |  | The assessment kind category ID for the screening program, such as Lung Assessment or Breast Incomplete Reason. |
| 7 | `ASSESSMENT_LOC_C_NAME` | VARCHAR |  | The location on the body category ID for the location of the assessment being documented. |
| 8 | `SX_PROG_ASMT_C_NAME` | VARCHAR |  | The assessment value category ID documented for this screening program, such as Incomplete, Negative, and Probably Benign. |
| 9 | `SX_PROG_ASMT_CMT` | VARCHAR |  | A comment for the assessment being documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

