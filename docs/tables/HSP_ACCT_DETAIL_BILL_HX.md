# HSP_ACCT_DETAIL_BILL_HX

> This table contains the history of hospital billing detail bills for a given hospital account.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The hospital account ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HBP_PRINT_ID` | NUMERIC | FK→ | The hospital billing print record ID. |
| 4 | `EB_PRINT_ID` | NUMERIC |  | The enterprise statement/detail bill ID. |
| 5 | `BILL_RUN_TYPE_C_NAME` | VARCHAR |  | The run type of the detail bill. |
| 6 | `IS_DEMAND_YN` | VARCHAR |  | Flag to indicate whether this detail bill was produced on demand instead of as part of a batch. |
| 7 | `ACCEPT_DATE` | DATETIME |  | The date the detail bill was accepted. |
| 8 | `BATCH_DATE` | DATETIME |  | The batch date of the detail bill. |
| 9 | `DELIVERY_METHOD_C_NAME` | VARCHAR |  | How the detail bill was delivered. |
| 10 | `CREATION_USER_ID` | VARCHAR |  | The user who created the detail bill. |
| 11 | `CREATION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `TOT_CHG_AMT` | NUMERIC |  | The sum of all charges on the detail bill. |
| 13 | `TOT_PMT_AMT` | NUMERIC |  | The sum of all payments on the detail bill. |
| 14 | `TOT_ADJ_AMT` | NUMERIC |  | The sum of all adjustments on the detail bill. |
| 15 | `INSURANCE_BALANCE` | NUMERIC |  | The total amount of the detail bill that is currently with insurance. |
| 16 | `PATIENT_BALANCE` | NUMERIC |  | The total amount of the detail bill that is currently in self-pay. |
| 17 | `PATIENT_AMOUNT_DUE` | NUMERIC |  | The total amount due for this detail bill. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HBP_PRINT_ID` | [HBP_STMT_PRINT](HBP_STMT_PRINT.md) | sole_pk | high |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

