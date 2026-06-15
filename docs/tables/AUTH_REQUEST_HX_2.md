# AUTH_REQUEST_HX_2

> This table contains a snapshot of information about an individual authorization request as of a point in time.

**Overflow of:** [AUTH_REQUEST_HX](AUTH_REQUEST_HX.md)  
**Primary key:** `AUTH_REQUEST_ID`, `CONTACT_DATE_REAL`  
**Columns:** 18  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_REQUEST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the authorization request record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `START_DATE` | DATETIME |  | The date from which this authorization request is effective. |
| 4 | `EXPIRATION_DATE` | DATETIME |  | The date after which the authorization request is no longer valid. The system will re-calculate this date as changes are made to the authorization unless it was entered by the user. |
| 5 | `EXPIRATION_USER_SET_DATE` | DATETIME |  | The user-entered date after which the authorization request is no longer valid. |
| 6 | `SUBMIT_CLM_BY_DATE` | DATETIME |  | The date by which claims must be submitted to be paid. The system will re-calculate this date as changes are made to the authorization unless it was entered by the user. |
| 7 | `SUBMIT_CLM_BY_USER_SET_DATE` | DATETIME |  | The user-entered date by which claims must be submitted to be paid. |
| 8 | `AUTH_SERVICE_TYPE_C_NAME` | VARCHAR | org | The service type of the authorization request. This is used after the UM service type is ready for use and the authorization workspace is enabled. |
| 9 | `AUTH_CARE_SETTING_C_NAME` | VARCHAR |  | The care setting of the authorization request. This item groups service types and drives the authorization workflow. |
| 10 | `FINALIZED_EDIT_REASON_C_NAME` | VARCHAR | org | The finalized edit reason category ID for the authorization request |
| 11 | `IS_FINALIZED_EDIT_YN` | VARCHAR |  | Indicates whether this contact was created during finalized edit for this authorization request. 'Y' indicates that this contact was created during finalized edit. 'N' or NULL indicate that this contact was not created during a finalized edit. |
| 12 | `EXTCVG_PAYER_NAME` | VARCHAR |  | The external coverage's payer name. |
| 13 | `EXTCVG_PLAN_NAME` | VARCHAR |  | The external coverage's plan name. |
| 14 | `EXTCVG_MEM_NUM` | VARCHAR |  | The external coverage's member number. |
| 15 | `EXTCVG_STAT_C_NAME` | VARCHAR |  | The external coverage's status |
| 16 | `EXTCVG_FROM_DATE` | DATETIME |  | The external coverage's effective from date. |
| 17 | `EXTCVG_TO_DATE` | DATETIME |  | The external coverage's effective to date. |
| 18 | `TAT_TAX_STATE_C_NAME` | VARCHAR | org | Stores the address's state used to map the authorization to review category. State is determined using the following order: referring provider address (I RFL 301), provider role location (I PRR 24), referring location (I RFL 310), member (I RFL 100). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |

