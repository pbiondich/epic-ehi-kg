# PAT_ENC_CC_LIST

> This table extracts CC'd chart routing history information of the encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the CC'ed Charts associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CC_LIST_PRIORITY_C_NAME` | VARCHAR | org | The routing priority for the CC'd chart message. |
| 5 | `CC_LIST_SENTBY_ID` | VARCHAR |  | The user ID of the message sender. |
| 6 | `CC_LIST_SENTBY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `CC_LIST_USER_ID` | VARCHAR |  | This column displays the recipient user ID if appropriate. |
| 8 | `CC_LIST_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `CC_LIST_POOL_ID` | NUMERIC |  | This column displays the pool record ID for the recipient if appropriate. |
| 10 | `CC_LIST_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 11 | `CC_LIST_CLASS_C` | VARCHAR |  | This column displays the class recipient if appropriate. |
| 12 | `CC_LIST_ADHOC` | VARCHAR |  | This column displays the ad-hoc recipient if appropriate. |
| 13 | `CC_LIST_EX_USER_ID` | VARCHAR |  | This column displays the excluded user ID for the recipient if appropriate. |
| 14 | `CC_LIST_EX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

