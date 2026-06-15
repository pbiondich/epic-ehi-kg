# ABN_NOTES

> The ABN_NOTES table contains information about Advanced Beneficiary Notice note records.

**Primary key:** `ABN_NOTE_ID`  
**Columns:** 19  
**Org-specific columns:** 3  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ABN_NOTE_ID` | VARCHAR | PK | The unique ID of the note (HNO) record that contains the Advance Beneficiary Notice (ABN) information. |
| 2 | `ABN_STATUS_C_NAME` | VARCHAR | org | The status of the ABN record. |
| 3 | `USER_ID` | VARCHAR | FK→ | The user who updated the ABN record. |
| 4 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CREATE_TM` | DATETIME (Local) |  | The time the ABN record was created. |
| 6 | `INITIAL_USER_ID` | VARCHAR |  | The user who created the ABN record. |
| 7 | `INITIAL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `ABN_TEMPLT_C_NAME` | VARCHAR | org | The ABN template used for the ABN form. |
| 9 | `ABN_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 10 | `ABN_PR_EST` | VARCHAR |  | The estimated price for all procedures listed on the ABN. |
| 11 | `ABN_COMM_BARRIER_C_NAME` | VARCHAR | org | The communication barrier encountered with the patient involving the ABN. |
| 12 | `ABN_UPDATE_INS_DTTM` | DATETIME (Local) |  | The instant when the ABN was updated. |
| 13 | `ABN_CMT` | VARCHAR |  | A comment for an ABN. |
| 14 | `ABN_CHECK_FROM_DATE` | DATETIME |  | Stores the starting date of service for which the ABN checks are performed. |
| 15 | `ABN_CHECK_TO_DATE` | DATETIME |  | Stores the date till which the ABN checks are performed. |
| 16 | `ABN_PLAN_ID` | NUMERIC |  | Stores the unique ID of the linked treatment or therapy plan. |
| 17 | `PAT_CSN` | NUMERIC | FK→ | Stores the contact serial number (CSN) for the telephone encounter used for follow up. |
| 18 | `REPLACED_ABN_ID` | VARCHAR |  | If this ABN was regenerated from another ABN, this column contains the ID of the original |
| 19 | `REPLACE_REASON_C_NAME` | VARCHAR |  | The reason that the ABN was regenerated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [ABN_ORDERS](ABN_ORDERS.md) | `ABN_NOTE_ID` | high |
| [IB_MESSAGES_3](IB_MESSAGES_3.md) | `ABN_NOTE_ID` | high |
| [ORDER_PROC](ORDER_PROC.md) | `ABN_NOTE_ID` | high |

