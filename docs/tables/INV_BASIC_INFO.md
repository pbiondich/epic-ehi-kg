# INV_BASIC_INFO

> This table contains basic invoice information. Each column in this table is from the INV 100 related group, and each line in the table corresponds to a claim that was sent for this invoice (INV) record.

**Primary key:** `INV_ID`, `LINE`  
**Columns:** 51  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INV_ID` | NUMERIC | PK | The invoice ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the invoice number associated with the invoice record. Multiple invoice numbers can be associated with a single invoice record. |
| 3 | `INV_NUM` | VARCHAR |  | The specific invoice number for the bill or claim. Subsequent invoice numbers may be secondary claims or primary claims that were resubmitted to the same payer. |
| 4 | `INV_STATUS_C_NAME` | VARCHAR |  | The status for the invoice number. |
| 5 | `CVG_ID` | NUMERIC | FK→ | The coverage record ID. |
| 6 | `EPM_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 7 | `EPP_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 8 | `FROM_SVC_DATE` | DATETIME |  | The from (minimum) service date for the invoice number. This date is determined from the transaction on the invoice with the service date furthest in the past. |
| 9 | `TO_SVC_DATE` | DATETIME |  | The to (maximum) service date for the invoice number. This date is determined from the transaction on the invoice with the most recent service date. |
| 10 | `INV_TYPE_C_NAME` | VARCHAR |  | The claim type for the invoice number. This column identifies whether the invoice number is a bill/statement or a claim. |
| 11 | `DEMAND_CLM_IND_C_NAME` | VARCHAR |  | This column identifies the invoice number as being a demand claim. |
| 12 | `CROSS_OVER_YN` | VARCHAR |  | Indicates whether the invoice number is a crossover claim. This usually only applies to secondary claims and indicates that although the claim associated with the invoice was created, it was suppressed from a claim run. |
| 13 | `MAILING_NAME` | VARCHAR |  | The bill/statement or claim mailing name for the invoice number. |
| 14 | `MAILING_ADDR` | VARCHAR |  | The bill/statement or claim mailing street address for the invoice number. |
| 15 | `CITY_STATE_ZIP` | VARCHAR |  | The bill/statement or claim mailing city, state, and ZIP Code for the invoice number. |
| 16 | `CLM_ID` | NUMERIC |  | The claim information record ID. |
| 17 | `CEP_ID` | VARCHAR |  | The Episode ID. |
| 18 | `REF_ID` | VARCHAR |  | The referral ID. |
| 19 | `REF_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 20 | `VIS_NUM` | VARCHAR |  | The visit number for the invoice number. |
| 21 | `EAF_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 22 | `TAX_ID_NUM` | VARCHAR |  | The tax ID/IRS number for the invoice number. |
| 23 | `TAX_ID_TYPE` | VARCHAR |  | The tax ID/IRS number type for the invoice number. |
| 24 | `DTP_ID` | VARCHAR |  | The dental treatment plan ID. |
| 25 | `CANCELED_INV` | VARCHAR |  | Contains a list of all the canceled invoice numbers associated with the invoice record. |
| 26 | `REPLACED_INV` | VARCHAR |  | Contains a list of all the replaced invoice numbers associated with the invoice record. |
| 27 | `CLM_CHANGE_RSN_COD` | VARCHAR |  | Contains a list of all the claim change reason codes associated with the invoice record. |
| 28 | `CLM_CHANGE_COMMENT` | VARCHAR |  | Contains a list of all the claim change comments associated with the invoice record. |
| 29 | `UB_OPER_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 30 | `MAIL_PHONE` | VARCHAR |  | The mailing phone number for the invoice number. |
| 31 | `ALTPAYR_INV_YN` | VARCHAR |  | Identifies if the invoice is for an alternate payer. |
| 32 | `LATE_REPLACEMENT_C_NAME` | VARCHAR |  | Flag to indicate the late replacement claim status of the invoice. |
| 33 | `CRD_ID` | VARCHAR |  | The claim reconciliation record ID. |
| 34 | `CLM_EXT_VAL_ID` | NUMERIC |  | The unique ID associated with the claim external value record for this row. Values derived from the claim print record or edited by the user will be stored in the claim external value. Form output will be based on the claim external value. |
| 35 | `MAIL_COUNTRY_C_NAME` | VARCHAR | org | Stores the mailing address country. |
| 36 | `CLM_ACCEPT_DT` | DATETIME |  | The invoice accept date. |
| 37 | `CLM_DX_CODE_SET_C_NAME` | VARCHAR | org | The code set of the diagnoses on the invoice. |
| 38 | `FILING_ORDER_C_NAME` | VARCHAR |  | This column holds the filing order position of the claim coverage at the time claims were processed. |
| 39 | `CLAIM_RUN_NUM` | VARCHAR |  | The claim run number. |
| 40 | `DEMAND_CLAIM_YN` | VARCHAR |  | This column indicates whether the invoice was created in a demand claim run. |
| 41 | `SRC_INV_NUM` | VARCHAR |  | This column stores the invoice number that generated the current invoice number. |
| 42 | `PREDETERMINATION_YN` | VARCHAR |  | Stores a Yes/No indicator that the associated record represents a request for a predetermination of benefits. |
| 43 | `PREDICTED_PAY_DATE` | DATETIME |  | The predicted payment response date for a claim based on historical trends for the payer. |
| 44 | `SUGGESTED_FOL_UP_DATE` | DATETIME |  | The suggested initial follow-up date for a claim based on historical trends for the payer. |
| 45 | `FINAL_FOL_UP_DATE` | DATETIME |  | This item shows the final date all the follow-up records were completed and is based on the last Completed Date (I FOL 122). It will only have a value if all of the follow-up records are currently completed. Should one reopen, this value will also be cleared. |
| 46 | `CLM_CLOSED_TIMELY_YN` | VARCHAR |  | Denotes if the claim closed prior to its Suggested Initial Follow-up Date, whereby it was no longer outstanding to insurance. The claim closed date is based on the CRD item of the same name (I CRD 86) if set, else the Final Follow-up Completed Date (I INV 133). |
| 47 | `CLM_SENT_EXPRESS_YN` | VARCHAR |  | Indicates if the claim is an accepted express claim based on an invoice claim flag (I INV 137) and accept date (I INV 191) |
| 48 | `EXPRESS_DISQUAL_RULE_ID` | VARCHAR |  | The claim rule (I CDF 1431) that disqualified the claim from being sent express. |
| 49 | `EXPRESS_DISQUAL_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 50 | `CH_SENT_DATE` | DATETIME |  | This item holds the last reported date the claim was sent out of the clearinghouse. |
| 51 | `PAYER_RECEIVED_DATE` | DATETIME |  | This item holds the last reported date the payer received the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

