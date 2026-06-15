# REFERRAL_HIST

> The REFERRAL_HIST table contains information on changes to referrals stored in system.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 15  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number of the change to the referral. For example, if the referral is changed twice, the first change will have a line value of 1, while the second change will have a line value of 2. |
| 3 | `CHANGE_DATE` | DATETIME |  | The date of the change to the referral. |
| 4 | `CHANGE_TYPE_C_NAME` | VARCHAR | org | The category value indicating the type of referral change. |
| 5 | `CHANGE_USER_ID` | VARCHAR |  | The ID number of the user who made the change to the referral. |
| 6 | `CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `PREVIOUS_VALUE` | VARCHAR |  | Some of the information on the referral is tracked when it changes. This stores the previous value of an item if it is tracked when it changes. |
| 8 | `CHANGE_DATETIME` | DATETIME (UTC) |  | The date and time of the change to the referral. |
| 9 | `AUTH_HX_EVENT_NO` | VARCHAR |  | The event no of the authorization history |
| 10 | `AUTH_HX_NOTE_ID` | VARCHAR |  | Referral audit trail item to store note Id |
| 11 | `CHANGE_LOCAL_DTTM` | DATETIME (Attached) |  | The authorization date and time as an instant in the local time zone |
| 12 | `NEW_RFL_STATUS_C_NAME` | VARCHAR | org | If the item being changed is Referral Status (I RFL 50), this item stores the new value for that item. |
| 13 | `NEW_PEND_RSN_C_NAME` | VARCHAR | org | If the item being changed is Reason Pending (I RFL 18003), this item stores the new value for that item. |
| 14 | `NEW_FIN_PROV_STATUS_C_NAME` | VARCHAR | org | If the item being changed is Finland - Provision Status (I RFL 72124), this item stores the new value for that item. |
| 15 | `NEW_FIN_VALID_END_DATE` | DATETIME |  | If the item being changed is Finland - Validity End Date (I RFL 72115), this item stores the new value for that item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

