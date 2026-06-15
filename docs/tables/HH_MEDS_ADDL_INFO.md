# HH_MEDS_ADDL_INFO

> The HH_MEDS_ADDL_INFO table contains information specific to Home Health/Hospice medications. This includes the hospice coverage status of a medication.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ENC_CSN` | NUMERIC | FK→ | The item stores the patient (EPT) contact serial number (CSN) associated with the update to the order's additional info. |
| 4 | `ENTRY_EMP_ID` | VARCHAR |  | Stores the user that updated an order's additional info |
| 5 | `ENTRY_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `ENTRY_DTTM` | DATETIME (Local) |  | Stores the instant that the additional information was synchronized from the Remote Client |
| 7 | `HSPC_CVG_STAT_C_NAME` | VARCHAR |  | Stores the hospice coverage status of a medication which helps to determine if the Hospice is responsible for paying for a medication |
| 8 | `TAKING_DIFF_POC_YN` | VARCHAR |  | Stores whether or not for this order (ORD) that the patient taking different sig should be pulled on to the Plan of Care (POC). |
| 9 | `HSPC_NONCVRD_MED_RSN_C_NAME` | VARCHAR | org | This column contains the reason why a medication is not covered by the hospice benefit. |
| 10 | `HSPC_NONCVRD_MED_RSN_C_CMT` | VARCHAR |  | This column contains the comment for the reason why a medication isn't covered by the hospice benefit. |
| 11 | `WHICH_SIG_ON_POC_C_NAME` | VARCHAR |  | This item stores which sigs to show on the plan of care. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | sole_pk | high |

