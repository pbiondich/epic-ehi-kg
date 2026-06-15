# DOCS_RCVD_MIXTURE_INFO

> This table stores ingredient information for mixture-based external prescriptions.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `INGREDIENT_DESC` | VARCHAR |  | This column stores the descriptions of individual ingredients of a mixture-based medication. |
| 5 | `INGREDIENT_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 6 | `INGREDIENT_QUANTITY` | NUMERIC |  | This columns stores the quantities for individual ingredients of a mixture-based medication. |
| 7 | `INGREDIENT_QUANTITY_UNIT_C_NAME` | VARCHAR | org | The quantity unit category ID for individual ingredients of a mixture-based medication. |
| 8 | `INGREDIENT_NDC_CSN` | VARCHAR |  | The unique contact serial number of NDCS of the individual ingredients of a mixture-based medication. |
| 9 | `INGREDIENT_DEA_CLASS_C_NAME` | VARCHAR | org | The DEA schedule category ID for individual ingredients of a mixture-based medication. If this column is not populated, the medication on this line is not controlled. |
| 10 | `INGREDIENT_EXT_MED_REF_IDENT` | VARCHAR |  | The reference ID of the dispensed medication associated with the ingredient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

