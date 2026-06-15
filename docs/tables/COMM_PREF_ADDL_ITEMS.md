# COMM_PREF_ADDL_ITEMS

> This table contains items related to Patient Communication Preferences.

**Primary key:** `PREFERENCES_ID`  
**Columns:** 11  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PREFERENCES_ID` | NUMERIC | PK | The unique identifier (.1 item) for the subject name record. |
| 2 | `APPT_REMDR_OFFSET_C_NAME` | VARCHAR |  | This column stores the offset of time prior to the appointment time when the system should send out a quick reminder. |
| 3 | `APPT_NOTIF_SCHEDULED_YN` | VARCHAR |  | This item stores a Yes No category value indicating whether the patient accepts Cadence Scheduled Appointment Notifications. |
| 4 | `APPT_NOTIF_CHANGED_YN` | VARCHAR |  | This item stores a Yes No category value indicating whether the patient accepts Cadence Changed Appointment Notifications. |
| 5 | `APPT_NOTIF_CANCELED_YN` | VARCHAR |  | This item stores a Yes No category value indicating whether the patient accepts Cadence Cancelled Appointment Notifications. |
| 6 | `APPT_NOTIF_MISSED_YN` | VARCHAR |  | This item stores a Yes No category value indicating whether or not a patient accepts Cadence Missed Appointment Notifications. |
| 7 | `USE_DAILY_DIGEST_YN` | VARCHAR |  | Indicates whether a user wants to receive To Do task notifications only once daily. |
| 8 | `DAILY_DIGEST_TM` | DATETIME (Local) |  | The time at which the user wants to receive once daily To Do task reminder notifications. If the time zone column is populated, then the time is in that time zone. Otherwise, it is in UTC. |
| 9 | `AUTO_ADD_TO_WAITLIST_YN` | VARCHAR |  | Indicates whether an appointment will be automatically added to the Wait List upon scheduling based on the patient preference. 'Y' indicates that the appointment is auto-added when scheduling if the DEP/SDF settings allow for it. 'N' or NULL indicate that the appointment will not be auto-added. |
| 10 | `RSLT_DAILY_DIGEST_YN` | VARCHAR |  | This item stores whether the user has signed up to receive a Daily Digest tickler for test results. |
| 11 | `DAILY_DIGEST_TIME_ZONE_C_NAME` | VARCHAR |  | The time zone of the time which the user wants to receive once daily To Do task reminder notifications. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [COMMUNICATION_PREFERENCES](COMMUNICATION_PREFERENCES.md) | `PREFERENCES_ID` | high |
| [COMM_PREFERENCES_APRV](COMM_PREFERENCES_APRV.md) | `PREFERENCES_ID` | high |
| [PATIENT_4](PATIENT_4.md) | `PREFERENCES_ID` | high |
| [V_EHI_AUDIT_OYO](V_EHI_AUDIT_OYO.md) | `PREFERENCES_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_OYO](V_EHI_REG_ITEM_AUDIT_OYO.md) | `PREFERENCES_ID` | high |

