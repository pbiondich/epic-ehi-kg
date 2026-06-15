# HSP_ACCT_CONS_SP_BAL

> The HSP_ACCT_CONS_SP_BAL table contains information about Received Self-Pay HARs as well as some total balance amounts. As a partial example, this includes core information such as the balance type, visit location, and type of visit, as well as total balance information such as total charges, insurance payments, etc.

**Primary key:** `HSP_ACCOUNT_ID`  
**Columns:** 16  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the hosp acct record. |
| 2 | `CONS_SP_BAL_TYPE_C_NAME` | VARCHAR |  | The type of balance for a self-pay target account. |
| 3 | `CONS_SP_VISIT_LOC` | VARCHAR |  | Stores a string description of the visit location or department for display in patient facing communication. Typically this will be a department for outpatient encounters and a location for inpatient or emergency encounters. |
| 4 | `CONS_SP_VISIT_DESC_OVRIDE` | VARCHAR |  | Stores a string description of the visit for display in patient facing communication. |
| 5 | `CONS_SP_VISIT_TYPE_C_NAME` | VARCHAR | org | The type of visit for the self-pay target account. |
| 6 | `CONS_SP_BAL_WTHDRW_RSN_C_NAME` | VARCHAR | org | This item contains the reason a self-pay target HAR was withdrawn or marked for withdrawal. |
| 7 | `CONS_SP_BAL_WTHDRW_STS_C_NAME` | VARCHAR |  | This item contains the status of a self-pay target HAR that has been withdrawn or marked for withdrawal. |
| 8 | `CONS_SP_TOT_CHG` | NUMERIC |  | Total amount of self-pay charges on this self-pay target account. |
| 9 | `CONS_SP_TOT_INS_PMT` | NUMERIC |  | Total amount of insurance payments on this self-pay target account. |
| 10 | `CONS_SP_TOT_INS_RFND` | NUMERIC |  | Total amount of insurance refunds on this self-pay target account. |
| 11 | `CONS_SP_TOT_INS_ADJ` | NUMERIC |  | Total amount of insurance adjustments on this self-pay target account. |
| 12 | `CONS_SP_TOT_SP_PMT` | NUMERIC |  | Total amount of payments on this self-pay target account. |
| 13 | `CONS_SP_TOT_SP_RFND` | NUMERIC |  | Total amount of self-pay refunds on this self-pay target account. |
| 14 | `CONS_SP_TOT_SP_ADJ` | NUMERIC |  | Total amount of self-pay adjustments on this self-pay target account. |
| 15 | `CONS_SP_TOT_INS_BAL` | NUMERIC |  | The outstanding insurance amount on this self-pay target account. |
| 16 | `CONS_SP_VISIT_SETTING_C_NAME` | VARCHAR |  | The visit setting for the consolidated self-pay target account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

