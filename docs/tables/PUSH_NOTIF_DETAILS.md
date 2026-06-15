# PUSH_NOTIF_DETAILS

> Table containing push notification extra details about notification. To extract data to PUSH_NOTIF_DETAILS: 1. In Clinical Administration, open EMR System Definitions and select Decision Support, Pop Management. 2. Go to the Push Notification Clarity Settings screen. 3. In the Types Excluded from Clarity Extracts field, enter the types of push notification you want to exclude from Clarity extraction. 4. In the Enable Clarity extraction for push notification field, enter 1-Yes.

**Primary key:** `NOTIF_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTIF_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the notification record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTIFICATION_DETAIL` | VARCHAR |  | Extra details about notification. Sometimes used to display in mobile report viewer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

