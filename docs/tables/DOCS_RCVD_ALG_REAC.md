# DOCS_RCVD_ALG_REAC

> This table stores allergy reactions received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | Contact date |
| 5 | `REAC_ALG_REF_ID` | VARCHAR |  | This item stores the allergy reference identifier that's associated with the reaction. |
| 6 | `REAC_NAME` | VARCHAR |  | This item stores the name of the reaction. |
| 7 | `REAC_ID_C_NAME` | VARCHAR | org | This item stores the reaction category value which maps to the one sent by the external source. |
| 8 | `REAC_CODE` | VARCHAR |  | This item stores the coded identifier for the reaction. |
| 9 | `REAC_CODING_SYSTEM` | VARCHAR |  | This item stores the reaction coding system associated with the code that represents the reaction. |
| 10 | `REAC_SEVERITY` | VARCHAR |  | This item stores the reaction severity. |
| 11 | `REAC_SEVERITY_ID_C_NAME` | VARCHAR |  | This item stores the mapped reaction severity. |
| 12 | `REAC_TYPE_OF_CHNG_C_NAME` | VARCHAR |  | This item stores the type of change associated with the reaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

