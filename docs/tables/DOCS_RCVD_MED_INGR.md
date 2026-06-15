# DOCS_RCVD_MED_INGR

> This table stores medication ingredients received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The Line Count |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ING_MED_REF_ID` | VARCHAR |  | This item stores the medication reference ID associated with the ingredient. |
| 6 | `ING_REF_ID` | VARCHAR |  | This item stores the unique ingredient reference ID. |
| 7 | `ING_NAME` | VARCHAR |  | This item store the name of the ingredient. |
| 8 | `ING_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 9 | `ING_TYPE_C_NAME` | VARCHAR | org | This item stores the mapped ingredient type. |
| 10 | `ING_DOSE` | VARCHAR |  | This item stores the textual ingredient dose. |
| 11 | `ING_DISCRETE_DOSE` | NUMERIC |  | This item stores the ingredient discrete dose information. |
| 12 | `ING_UNIT` | VARCHAR |  | This item stores the textual ingredient unit. |
| 13 | `ING_UNIT_ID_C_NAME` | VARCHAR | org | This item stores the mapped ingredient unit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

