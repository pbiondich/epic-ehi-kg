# TXP_OFFER_ENC

> Single-response items for organ offer encounters.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `TXP_TRAVEL_TIME` | VARCHAR |  | For an organ offer encounter, the travel time to the center in minutes, hours, or days. |
| 7 | `TXP_OFFER_PAT_DECISION_C_NAME` | VARCHAR |  | Whether the patient accepted or declined the offer. |
| 8 | `TXP_OFFER_DECLINE_REASON` | VARCHAR |  | For a patient who declines an organ offer, this item documents the reason they declined it. |
| 9 | `TXP_OFFER_CONTRA_OTHER` | VARCHAR |  | Recent contraindications that apply to a potential organ offer recipient and aren't represented in the Organ Offer Recent Contraindications (I EPT 98200) category list. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

