# OR_LNLG_BLOOD_PROD

> This table contains the Blood Product information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 5  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `BLOOD_PRODUCT_C_NAME` | VARCHAR | org | The blood product type. |
| 3 | `BLOOD_ESTIMATED` | NUMERIC |  | The estimated blood product. |
| 4 | `BLOOD_MSR_UNIT_C_NAME` | VARCHAR | org | The unit of measure for the estimated value. |
| 5 | `BLOOD_UNITS_USED` | NUMERIC |  | The number of units used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

