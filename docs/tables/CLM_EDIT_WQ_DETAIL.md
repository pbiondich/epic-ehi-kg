# CLM_EDIT_WQ_DETAIL

> This table contains one row for each transaction on a claim that is or has been in the claim error pool. This table updates records for transactions on claims that are still in the claim error pool but leaves the records for transactions on claims that are no longer in the error pool. There is only one date field concerning when the record was created, EXTRACT_DATE, which functions as in CLM_EDIT_WQ_DETAIL. After the claim has left the claim error pool, the last record will remain in the table indefinitely.

**Primary key:** `CLP_ID`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLP_ID` | NUMERIC | PK FK→ | The ID of the claim record that entered the claim edit workqueue. |
| 2 | `LINE` | INTEGER | PK | The line number of the transaction that appears on the claim record. |
| 3 | `PERFORMING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `REFERRAL_PROV_ID` | VARCHAR |  | The ID of the transaction's referring provider. |
| 5 | `REFERRAL_PROV_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 6 | `ORIG_AMOUNT` | NUMERIC |  | The original amount of the transaction. |
| 7 | `AMOUNT_DUE` | NUMERIC |  | The amount of money due for the transaction at the time of the extract. |
| 8 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 9 | `REV_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 10 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 11 | `SERVICE_DATE` | DATETIME |  | The date for which services were performed. |
| 12 | `POST_DATE` | DATETIME |  | The date the transaction was posted. |
| 13 | `BILLING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 14 | `POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 15 | `VISIT_NUMBER` | VARCHAR |  | The visit number within the account that corresponds to the transaction. This number uniquely identifies the visit within the account only. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLP_ID` | [CLM_EDIT_WQ_CLM](CLM_EDIT_WQ_CLM.md) | sole_pk | high |

