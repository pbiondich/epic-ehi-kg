# PUSH_NOTIF_TEXT

> Table containing in app text for push notification. To extract data to PUSH_NOTIF_TEXT: 1. In Clinical Administration, open EMR System Definitions and select Decision Support, Pop Management. 2. Go to the Push Notification Clarity Settings screen. 3. In the Types Excluded from Clarity Extracts field, enter the types of push notification you want to exclude from Clarity extraction. 4. In the Enable Clarity extraction for push notification field, enter 1-Yes.

**Primary key:** `NOTIF_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTIF_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the notification record. |
| 2 | `IN_APP_TEXT` | VARCHAR |  | Text appearing in notification banner that appears inside the application |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

