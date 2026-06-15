# HSP_TX_IMAGING

> This table contains imaging information from the Hospital Permanent Transactions (HTR) master file.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction with related imaging information. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Each imaging entry will have its own line. |
| 3 | `IMAGE_MNEMONIC_C_NAME` | VARCHAR | org | This column stores the image mnemonic associated with the hospital billing transaction: e.g., explanation of benefits image. |
| 4 | `IMAGE_KEY` | VARCHAR |  | Image key associated with transaction. |
| 5 | `IMAGE_KEY_PAGE_NUM` | VARCHAR |  | This column stores the key that identifies a particular invoice within an explanation of benefits image. |
| 6 | `IMAGE_DOCUMENT_ID` | VARCHAR |  | Source DCS Record used in creating this HTR from payment posting |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

