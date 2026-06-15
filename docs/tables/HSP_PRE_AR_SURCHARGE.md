# HSP_PRE_AR_SURCHARGE

> This table contains surcharge related information for Hospital Billing temporary transactions. This table is limited to charge temporary transactions that have not yet been posted to the account.

**Primary key:** `HTT_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HTT_ID` | NUMERIC | PK FK→ | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QUAL_CHG_TX_ID` | NUMERIC |  | Stores a list of charges used in the calculation of "Taxable Charges" Surcharge. |
| 4 | `SURCHARGE_PERCENT` | NUMERIC |  | Stores the percentage used for charges used in the calculation of "Taxable Charges" Surcharge. |
| 5 | `SURCHARGE_AMT` | NUMERIC |  | Stores the amount of tax applied per charge that contributes to the total calculation of "Taxable Charges" Surcharge. |
| 6 | `TAX_CLASS_C_NAME` | VARCHAR | org | Tax classification used to determine the rate used in the "Taxable Charges" surcharge calculation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HTT_ID` | [HSP_PRE_AR_SESSION](HSP_PRE_AR_SESSION.md) | sole_pk | high |

