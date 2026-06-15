# HSP_ACCT_CONS_SP_CHG

> The HSP_ACCT_CONS_SP_CHG table contains information about the charge documentation lines associated with a received self-pay hospital account. As a partial example, this includes common charge information like the service date, description, revenue code, quantity, and amount.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the hosp acct record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHG_UNIQUE_IDENT` | VARCHAR |  | An identifier unique to this charge documentation line related group at the HAR level. No other charge documentation lines on the same HAR should share this identifier. |
| 4 | `CHG_SERVICE_DATE` | DATETIME |  | The service date for a consolidated self-pay charge. This date is when the service occurred in the source system. |
| 5 | `CHG_POST_DATE` | DATETIME |  | The original post date for a consolidated self-pay charge. This date is when the charge was posted in the source system. |
| 6 | `CHG_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 7 | `CHG_DESCRIPTION` | VARCHAR |  | A description of a consolidated self-pay charge. Can be supplied by the source system as an override for the procedure description. |
| 8 | `CHG_REV_CODE_ID` | NUMERIC |  | The revenue code for a consolidated self-pay charge. If this was not supplied by the source system, it should be set to the procedure code's alternate revenue code. |
| 9 | `CHG_REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 10 | `CHG_HCPCS_CODE` | VARCHAR |  | The HCPCS or CPT code for a consolidated self-pay charge. |
| 11 | `CHG_MODIFIER` | VARCHAR |  | A comma delimited string of modifiers on a consolidated self-pay charge. |
| 12 | `CHG_QUANTITY` | NUMERIC |  | The quantity for a consolidated self-pay charge. |
| 13 | `CHG_AMOUNT` | NUMERIC |  | The credit or debit amount for a consolidated self-pay charge. |
| 14 | `CHG_NDC_CODE` | VARCHAR |  | The NDC code for a consolidated self-pay charge. |
| 15 | `CHG_SERV_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 16 | `CHG_REVERSAL_DATE` | DATETIME |  | The date that this charge documentation line was reversed. This date is set to the day the documentation line was marked as reversed by the source system. If this item is blank, then the charge has not been reversed. |
| 17 | `CHG_ORIG_IDENT` | VARCHAR |  | An identifier for a received self-pay charge used by the source. If this is from another system, this is the ID the source system uses. If this is from the same system, this is the original transaction ID for the source service area (HTR for HB transaction, ETR for PB). |
| 18 | `CHG_UPDATE_DATE` | DATETIME |  | The date that this charge documentation line was consolidated. This date is set to the day the documentation line was first imported from the source system. |
| 19 | `CHG_CONS_SP_DOCLN_STS_C_NAME` | VARCHAR |  | The current active status of the documentation line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

