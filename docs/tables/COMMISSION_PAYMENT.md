# COMMISSION_PAYMENT

> Contains information about commission payment transactions.

**Primary key:** `TX_ID`  
**Columns:** 42  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `TX_TYPE_C_NAME` | VARCHAR |  | Stores the type of the adjustment transaction. |
| 3 | `TX_STATUS_C_NAME` | VARCHAR |  | The status of the transaction. |
| 4 | `SPECIAL_TX_TYPE_C_NAME` | VARCHAR | org | This item stores the transaction type. |
| 5 | `EFFECTIVE_DATE` | DATETIME |  | Contains first of month as the date for which the batch containing this transaction is filed. |
| 6 | `POSTING_DATE` | DATETIME |  | The date this transaction was posted. |
| 7 | `ELIGIBILITY_DATE` | DATETIME |  | The eligibility date used to compute this transaction. |
| 8 | `USER_ID` | VARCHAR | FK→ | The user that created the record |
| 9 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `COMMISSION_PAT_ID` | VARCHAR | FK→ | The member associated with the commission transaction. |
| 11 | `COMM_PLAN_GRP_ID` | VARCHAR |  | The employer group of the member associated with the commission transaction. |
| 12 | `COMM_PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 13 | `COMMISSION_CVG_ID` | NUMERIC |  | The coverage associated with the commission transaction. |
| 14 | `COMMISSION_TML_ID` | NUMERIC |  | The list of members associated with the commission transaction. |
| 15 | `COMM_BUS_SEG_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 16 | `COMM_BROKER_ID_AGENT_NAME` | VARCHAR |  | The name of the agent. |
| 17 | `COMM_BROKERAGE_ID` | VARCHAR |  | The brokerage associated with the commission transaction. |
| 18 | `COMM_BROKERAGE_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 19 | `COMMISSION_TYPE_C_NAME` | VARCHAR | org | The commission type of the transaction. |
| 20 | `COMMISSION_LOB_ID` | VARCHAR |  | The line of business of the coverage for the commission transaction. |
| 21 | `COMMISSION_LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 22 | `COMM_GVT_PRGRM_C_NAME` | VARCHAR |  | The government program type of the coverage for the commission transaction. |
| 23 | `COMMISSION_VEN_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 24 | `COMMISSION_GL_CODE` | VARCHAR |  | The broker expense credit GL string for the commission transaction. |
| 25 | `COMMISSION_RUN_ID` | NUMERIC |  | The computation run record ID for the commission transaction. |
| 26 | `COMM_FORMULA_ID` | VARCHAR |  | The rate table used to compute the commission transaction. |
| 27 | `COMM_FORMULA_ID_RATE_TABLE_NAME` | VARCHAR |  | Name of the capitation rate table. |
| 28 | `COMMISSION_AMT` | NUMERIC |  | The commission amount the broker has earned. |
| 29 | `COMMISSION_UN_AMT` | NUMERIC |  | The computed commission amount withheld from payment. |
| 30 | `COMMISSION_WHLD_C_NAME` | VARCHAR |  | The reason the commission was withheld from payment. |
| 31 | `COMMISSION_ELIG_AMT` | NUMERIC |  | The eligibility portion of the commission. |
| 32 | `COMMISSION_MGR_ID_MEM_GRP_NAME` | VARCHAR |  | The name of the member group |
| 33 | `COMM_SCHED_SRC_C_NAME` | VARCHAR |  | The source of the commission schedule. |
| 34 | `TX_CANC_TX_ID` | NUMERIC |  | The transaction which cancels this transaction. |
| 35 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 36 | `END_DATE` | DATETIME |  | The end of the effective period this transaction covers. If not set, the end date is assumed to be the last day of the month relative to the effective date. |
| 37 | `COMM_CORP_ID` | VARCHAR |  | The corporation associated with the commission transaction. |
| 38 | `COMM_CORP_ID_CORP_NAME` | VARCHAR |  | The name of the corporation. |
| 39 | `COMM_INELIG_MEM_CNT` | INTEGER |  | The number of ineligible members associated with this commission transaction. Ineligible members are withheld from generating commission payments. |
| 40 | `COMMISSION_PRODUCT_LVL_RULE_ID` | VARCHAR |  | The product-level rule that validated the broker on the associated employer group. |
| 41 | `COMMISSION_PRODUCT_LVL_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 42 | `COMM_PRORATE_MTHD_C_NAME` | NUMERIC |  | This item stores the proration method used to create the commission payment transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COMMISSION_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

