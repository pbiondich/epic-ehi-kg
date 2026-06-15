# BILLING_ENC_HX

> This table contains a history of the encounter-level events for Billing Encounters.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `BILL_ENC_HX_EVENT_C_NAME` | VARCHAR |  | The event within the audit trail of encounter level events. |
| 6 | `BILL_ENC_HX_USER_ID` | VARCHAR |  | The user who performed the encounter level event in the audit trail. |
| 7 | `BILL_ENC_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `BILL_ENC_HX_UTC_DTTM` | DATETIME (UTC) |  | The instant at which the encounter level event was performed in the audit trail. |
| 9 | `BILL_ENC_HX_CMT` | VARCHAR |  | A user-entered comment to explain the event |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

