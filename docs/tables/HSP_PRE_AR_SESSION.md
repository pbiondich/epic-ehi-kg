# HSP_PRE_AR_SESSION

> This table stores single response items for temporary hospital billing transactions. This table is limited to charge temporary transactions that have not yet been posted to the account.

**Primary key:** `HTT_ID`  
**Columns:** 43  
**Org-specific columns:** 5  
**Joined by:** 13 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HTT_ID` | NUMERIC | PK | The unique identifier for the transaction record. |
| 2 | `TX_TYPE_HA_C_NAME` | VARCHAR |  | This item indicates the type of temporary transaction record. This is used by the Hospital Billing filer to determine how to process the record. |
| 3 | `TX_SOURCE_C_NAME` | VARCHAR |  | This item contains the source for this transaction. |
| 4 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | Stores the hospital account associated with the transaction. |
| 6 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | Patient CSN associated with the transaction. |
| 7 | `RESEARCH_STUDY_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 8 | `RSH_CHG_ORIG_HSP_ACCOUNT_ID` | NUMERIC |  | Stores the hospital account for the patient enrolled in the research study, which the charges were generated from before being billed to the study account. |
| 9 | `SERVICE_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 10 | `BILLING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 11 | `COST_CENTER_ID` | NUMERIC |  | Stores the cost center to which this transaction is being attributed. |
| 12 | `COST_CENTER_ID_COST_CENTER_NAME` | VARCHAR |  | The name of the cost center. |
| 13 | `SERVICE_DATE` | DATETIME |  | The date of service or deposit associated with the transaction. |
| 14 | `REFUND_AP_DATE` | DATETIME |  | Stores the date on which the A/P system processed the transaction. |
| 15 | `REFUND_AP_STATUS_C_NAME` | VARCHAR |  | Stores the action taken by the A/P system when it processed the transaction. |
| 16 | `ACCT_CLASS_HA_C_NAME` | VARCHAR | org | Holds the account class of the account when offsetting system adjustments are created. For all other transactions, this item is not set and instead the corresponding posted transaction values are calculated at the time of filing. |
| 17 | `ACCT_FIN_CLASS_C_NAME` | VARCHAR | org | Holds the financial class of the account when offsetting system adjustments are created. |
| 18 | `PRIMARY_COVERAGE_ID` | NUMERIC |  | Holds the primary coverage of the account when offsetting system adjustments are created. |
| 19 | `PRIMARY_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 20 | `PRIMARY_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 21 | `TOTAL_CHARGE_AMT` | NUMERIC |  | Stores the total price amount for the charges in this session. |
| 22 | `ORDER_ID` | NUMERIC | shared | Stores the ID of the order associated with the charge. |
| 23 | `TREATMENT_PLAN_CSN` | NUMERIC |  | The contact serial number of the treatment plan that generated this charge session and order. |
| 24 | `TREATMENT_DAY_CSN` | NUMERIC |  | The contact serial number of the treatment day that generated this charge session's order. |
| 25 | `OPTIME_LOG_ID` | VARCHAR |  | Stores the identifier of the OpTime Log associated with this charge. |
| 26 | `SYS_RECLASS_RSN_C_NAME` | VARCHAR |  | Stores the reclassification reason for a transaction reposted for system reasons. |
| 27 | `REVERSAL_RSN_C_NAME` | VARCHAR | org | Holds the reversal reason. This is set for all transaction types. |
| 28 | `CONTEST_RSN_C_NAME` | VARCHAR | org | Stores the contested reason. This is set only for charges. |
| 29 | `CONTEST_RESOLUTION_RSN_C_NAME` | VARCHAR | org | Stores the resolution reason. This is set only for charges. |
| 30 | `NO_PAY_CLAIM_TYPE_C_NAME` | VARCHAR |  | If this charge was posted to drive no-pay claims to be generated, this charge is intended to file and bill immediately. These claims will have different types/purposes. This column defines the type of claim that should be generated for the bucket that holds this charge. |
| 31 | `BAD_DEBT_FLAG_YN` | VARCHAR |  | This column marks the account's A/R as belonging to bad debt. |
| 32 | `POS_SESSION_IDENT` | VARCHAR |  | Point of Sale session ID. |
| 33 | `POS_TX_IDENT` | VARCHAR |  | Point of Sale transaction ID. |
| 34 | `POS_TX_LINENUM` | INTEGER |  | Point of Sale transaction line number. |
| 35 | `TAX_EFFECTIVE_DATE` | DATETIME |  | Stores the date used in the system that determine when this tax line went into effect. |
| 36 | `TAXABLE_AMT` | NUMERIC |  | This column stores the amount that the tax is applied to. |
| 37 | `TAX_PERCENT` | NUMERIC |  | Percent used to calculate the tax amount. |
| 38 | `TAX_AMOUNT` | NUMERIC |  | This column stores the amount used for the tax. |
| 39 | `SURCHARGE_CLAIM_PRINT_ID` | NUMERIC |  | The unique identifier of the claim print record associated with the surcharge amount of this transaction. |
| 40 | `TAX_RATE_DEF_CSN` | NUMERIC |  | The tax rate definition CSN used in the tax calculation. |
| 41 | `DEFAULT_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 42 | `POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 43 | `EXTERN_AR_FLAG_YN` | VARCHAR |  | This column marks the account's A/R as belonging to an agency. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

## Joined in — referenced by (13)

| From | Column | Confidence |
|------|--------|------------|
| [HSP_PRE_AR_AUTH_CNT](HSP_PRE_AR_AUTH_CNT.md) | `HTT_ID` | high |
| [HSP_PRE_AR_AUTH_CVG](HSP_PRE_AR_AUTH_CVG.md) | `HTT_ID` | high |
| [HSP_PRE_AR_AUTH_ID](HSP_PRE_AR_AUTH_ID.md) | `HTT_ID` | high |
| [HSP_PRE_AR_AUTH_NUM](HSP_PRE_AR_AUTH_NUM.md) | `HTT_ID` | high |
| [HSP_PRE_AR_AUTH_SRC](HSP_PRE_AR_AUTH_SRC.md) | `HTT_ID` | high |
| [HSP_PRE_AR_AUTH_UPDATE](HSP_PRE_AR_AUTH_UPDATE.md) | `HTT_ID` | high |
| [HSP_PRE_AR_AUTH_USER](HSP_PRE_AR_AUTH_USER.md) | `HTT_ID` | high |
| [HSP_PRE_AR_BND_EPSD_HX](HSP_PRE_AR_BND_EPSD_HX.md) | `HTT_ID` | high |
| [HSP_PRE_AR_DOC_PROV](HSP_PRE_AR_DOC_PROV.md) | `HTT_ID` | high |
| [HSP_PRE_AR_DX](HSP_PRE_AR_DX.md) | `HTT_ID` | high |
| [HSP_PRE_AR_SURCHARGE](HSP_PRE_AR_SURCHARGE.md) | `HTT_ID` | high |
| [HSP_PRE_AR_TX](HSP_PRE_AR_TX.md) | `HTT_ID` | high |
| [HSP_PRE_AR_TX_FLAGS](HSP_PRE_AR_TX_FLAGS.md) | `HTT_ID` | high |

