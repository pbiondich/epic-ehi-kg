# OTP_CC

> This table contains information on what users orders results will be CC'ed to. This information is held in the CC list (I OTP 105) item.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CC_LIST_USER_ID` | VARCHAR |  | This column displays the recipient user ID if appropriate. This column is linked to the identifier item (EMP .1) of the User (EMP) master file. |
| 4 | `CC_LIST_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CC_LIST_IB_POOL_ID` | NUMERIC |  | This column displays the pool record ID for the recipient if appropriate. This column is linked to the identifier item (HIP .1) of the Registry (HIP) master file. |
| 6 | `CC_LIST_IB_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 7 | `CC_LIST_CLASSES_C` | VARCHAR |  | This column displays the class recipient if appropriate. This column is linked to the classifications item (EMP-450) in the User (EMP) master file. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

