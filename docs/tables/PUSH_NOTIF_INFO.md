# PUSH_NOTIF_INFO

> This table contains information about push notifications. To extract data to PUSH_NOTIF_INFO: 1. In Clinical Administration, open EMR System Definitions and select Decision Support, Pop Management. 2. Go to the Push Notification Clarity Settings screen. 3. In the Types Excluded from Clarity Extracts field, enter the types of push notification you want to exclude from Clarity extraction. 4. In the Enable Clarity extraction for push notification field, enter 1-Yes.

**Primary key:** `NOTIF_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTIF_ID` | NUMERIC | PK shared | The unique identifier for the notification record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this notification. This column is frequently used to link to the PATIENT table. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 4 | `ALERT_CSN_ID` | NUMERIC |  | The unique contact serial number (CSN) of the alert linked to the notification when a push notification is sent as a follow-up action to an OurPractice Advisory (OPA). |
| 5 | `NOTIF_SEND_DATE` | DATETIME (UTC) |  | The date when the initial push notification was sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

