# HSP_TX_SURCHARGE

> This table contains charge-based surcharge information.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QUAL_CHG_TX_ID` | NUMERIC |  | List of charges that were used to calculate Surcharge in "Taxable Charges Only" calculation. |
| 4 | `SURCHARGE_PERCENT` | NUMERIC |  | The percent applied in order to calculate surcharge for the specific charge. |
| 5 | `SURCHARGE_AMT` | NUMERIC |  | The amount of tax for this charge to be applied to the total surcharge on the account. |
| 6 | `TAX_CLASS_C_NAME` | VARCHAR | org | Tax classification used to determine the rate used in the "Taxable Charges" surcharge calculation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

