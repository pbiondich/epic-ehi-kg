# INVOICE_CLM_LN

> This table contains line-level information for the claim generated from this INV record. This information is common to all claims for the INV; use INVOICE_CLM_LN_ADDL for invoice-specific information or line-level overrides.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 17  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The unique ID of the invoice record. |
| 2 | `LINE` | INTEGER | PK | The line number of the transaction ID item. |
| 3 | `FROM_DATE_OF_SVC` | DATETIME |  | The earliest date of service that appears on the transaction. |
| 4 | `TO_DATE_OF_SVC` | DATETIME |  | The latest (most recent) date of service that appears on the transaction. |
| 5 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 6 | `MODIFIER_ONE` | VARCHAR |  | The first modifier on the transaction. This is the external modifier, as it would be printed on the claim. |
| 7 | `MODIFIER_TWO` | VARCHAR |  | The second modifier on the transaction. This is the external modifier, as it would be printed on the claim. |
| 8 | `MODIFIER_THREE` | VARCHAR |  | The third modifier on the transaction. This is the external modifier, as it would be printed on the claim. |
| 9 | `MODIFIER_FOUR` | VARCHAR |  | The fourth modifier on the transaction. This is the external modifier, as it would be printed on the claim. |
| 10 | `QUANTITY` | NUMERIC |  | The quantity that appears on the transaction. |
| 11 | `CHARGE_AMOUNT` | NUMERIC |  | The dollar amount that appears on the transaction. |
| 12 | `NON_COVERED_AMT` | NUMERIC |  | The amount not covered on the transaction. |
| 13 | `TYPE_OF_SERVICE_C_NAME` | VARCHAR | org | The type of service performed for the charge. |
| 14 | `SPECIAL_GRP_TYPE_C_NAME` | VARCHAR | org | This is the type of grouping for this line in the invoice. |
| 15 | `UB_MIN_SERVICE_DT` | DATETIME |  | The UB form minimum service date for the invoice. |
| 16 | `UB_MAX_SERVICE_DT` | DATETIME |  | The UB form maximum service date for the invoice. |
| 17 | `DX_POINTER` | VARCHAR |  | Diagnosis pointers. This is a comma-delimited string indicating which diagnosis or diagnoses apply to this line that would appear on the claim. Each pointer corresponds to a line in INV_DX_INFO. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

