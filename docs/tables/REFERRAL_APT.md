# REFERRAL_APT

> This table contains information about referral appointments.

**Primary key:** `REFERRAL_ID`, `LINE_COUNT`  
**Columns:** 18  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE_COUNT` | INTEGER | PK | A line number that is used to group information about contacts that have counted towards the referral. |
| 3 | `SERVICE_DATE` | DATETIME |  | The date of the service (date of the appointment, claim, charge, or admission date) that is associated with the referral |
| 4 | `SERVICE_TYPE_C_NAME` | VARCHAR |  | The type of service that has been counted as a contact toward the total of completed contacts for this referral. |
| 5 | `CHARGE_ID` | NUMERIC |  | The ID number of the charge, if the source is “Charge.” |
| 6 | `CLAIM_ID` | NUMERIC | FK→ | The ID number of the AP Claim, if the source is “Claim” |
| 7 | `SERIAL_NUMBER` | NUMERIC |  | The ID number of the contact, if the source is either "Visit" or "Admission" |
| 8 | `USER_ID` | VARCHAR | FK→ | The ID number of the user who performed an override of the counting/contact information, if the source of the contact is "User Override" |
| 9 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `REASON` | VARCHAR |  | The reason for the user override, if the source of the contact was "User Override" |
| 11 | `TABLE_COUNT` | NUMERIC |  | The number of completed contacts that have been counted for this source. |
| 12 | `EXT_SVC_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `EXT_SVC_TIME` | DATETIME (Local) |  | The time associated with the external appointment that was added to the referral. |
| 14 | `EXT_SVC_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 15 | `EXT_APPT_STATUS_C_NAME` | VARCHAR | org | This column contains the appointment status for external appointments. |
| 16 | `EXT_APPT_UNIQ_ID` | VARCHAR |  | This column contains the unique ID for external appointments. |
| 17 | `EXT_SVC_UTC_DTTM` | DATETIME (UTC) |  | This column contains the timestamp when the service is performed in UTC format. |
| 18 | `EXT_SVC_DTTM` | DATETIME (Attached) |  | This column contains the external service date and time as an instant in the local time zone. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

