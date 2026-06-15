# DETAIL_BILL_HX

> Hospital account based detail bill history for the guarantor.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the guarantor record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HB_PRINT_ID` | NUMERIC |  | This column stores the unique identifier for this hospital detail bill in detail bill history. |
| 4 | `EB_PRINT_ID` | NUMERIC |  | This column stores the unique identifier for this enterprise detail bill record in detail bill history. |
| 5 | `BILL_RUN_TYPE_C_NAME` | VARCHAR |  | The run type for this detail bill. |
| 6 | `IS_DEMAND_DB_YN` | VARCHAR |  | Flag to indicate whether this detail bill was produced on demand or as part of the batch. |
| 7 | `ACCEPT_DT` | DATETIME |  | The date the detail bill record was created. |
| 8 | `END_BATCH_DT` | DATETIME |  | The batch date of the detail bill. |
| 9 | `DB_DVRY_MTHD_C_NAME` | VARCHAR |  | Stores how the detail bill was delivered. |
| 10 | `USER_ID` | VARCHAR | FK→ | The user who created the detail bill. |
| 11 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `TOTAL_CHG_AMT` | NUMERIC |  | The sum of all charges on the detail bill. |
| 13 | `TOTAL_PMT_AMT` | NUMERIC |  | The sum of all payments on the detail bill. |
| 14 | `TOTAL_ADJ_AMT` | NUMERIC |  | The sum of all adjustments on the detail bill. |
| 15 | `CUR_INS_BAL_AMT` | NUMERIC |  | The total amount of the detail bill that is currently with insurance. |
| 16 | `CUR_PAT_BAL_AMT` | NUMERIC |  | The total amount of the detail bill that is currently in self-pay. |
| 17 | `TOTAL_AMT_DUE` | NUMERIC |  | The total amount due for this detail bill. |
| 18 | `DB_IS_MYC_NOTIF_YN` | VARCHAR |  | Stores if the detail bill notification was sent via MyChart. |
| 19 | `DB_PAPER_RSN_C_NAME` | VARCHAR |  | Stores the reason why the detail bill was sent via paper. |
| 20 | `INVOICE_NUMBER` | VARCHAR |  | Invoice number for a detail bill. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

