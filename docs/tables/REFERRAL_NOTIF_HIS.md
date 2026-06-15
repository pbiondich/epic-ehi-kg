# REFERRAL_NOTIF_HIS

> The REFERRAL_NOTIF_HIS table holds the notification history information associated with the referral records stored in the REFERRAL table.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique ID of the referral in database, to which this notification history information is linked. |
| 2 | `LINE` | INTEGER | PK | The line number of the notification history for the referral. For example, if the referral has two notification events, the first will have a line value of 1, while the second will have a line value of 2. |
| 3 | `LTR_HX_DOC_TYPE_C_NAME` | VARCHAR |  | Stores the document type generated from this notification event. |
| 4 | `LTR_HX_ROI_ID` | VARCHAR |  | Stores the release of information record that the document sent is stored on. |
| 5 | `LTR_HX_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 6 | `LTR_HX_FAX_OVERRIDE` | VARCHAR |  | Stores the fax number we sent this notification to. |
| 7 | `NOTIF_HX_GRP_IDENT` | VARCHAR |  | A grouper ID shared between multiple rows in the notification history table that relate to the same event. |
| 8 | `EVENT_ID` | VARCHAR | FK→ | Stores the notification event ID triggered |
| 9 | `EVENT_ID_EVENT_NAME` | VARCHAR |  | The name of the event. |
| 10 | `NOTIF_HX_ROUTE_C_NAME` | VARCHAR | org | Stores the Routing Method of the notification event record. |
| 11 | `OWNING_INSTANCE_ID` | VARCHAR |  | Stores the owning deployment of this notification history line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

