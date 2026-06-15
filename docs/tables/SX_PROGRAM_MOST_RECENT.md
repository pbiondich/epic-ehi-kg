# SX_PROGRAM_MOST_RECENT

> This table contains information about the most recent screening program assessment data. This includes the program type, as well as the assessment kind, location, and value. The records in this table are Orders (ORD) records that are exams within a screening program.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LAST_PROGRAM_C_NAME` | VARCHAR |  | The screening program category ID for the screening program being documented, such as Breast Screening or Lung Screening. |
| 4 | `LAST_ASMT_KIND_C_NAME` | VARCHAR |  | The assessment kind category ID for the screening program, such as Lung Assessment or Breast Incomplete Reason. |
| 5 | `LAST_ASMT_LOC_C_NAME` | VARCHAR |  | The location on the body category ID for the location of the assessment being documented. |
| 6 | `LAST_SX_PROG_ASMT_C_NAME` | VARCHAR |  | The assessment value category ID documented for this screening program, such as Incomplete, Negative, and Probably Benign. |
| 7 | `LST_SX_PRG_ASMT_CMT` | VARCHAR |  | The most recent comment of the assessment being documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

