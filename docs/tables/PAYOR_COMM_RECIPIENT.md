# PAYOR_COMM_RECIPIENT

> The PAYOR_COMM_RECIPIENT table contains information related to recipients in Clinical Case Management's Payor Communication navigator section. This table contains all recipients that have been added to the Payor Communication navigator section for the related encounter, along with the IDs of any related user entered comments (HNO IDs). Note that data related to sending communications is stored in the PAYOR_COMM_HX table, not this table.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `AGENCY_ID` | VARCHAR | FK→ | The ID of a recipient that has been added to the Payor Communication navigator section. There can be several recipients added to the Payor Communication navigator section for each patient. Each recipient represents a contact (fax/phone/name) for a payor. |
| 7 | `AGENCY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 8 | `NOTE_ID` | VARCHAR | shared | The ID of a user entered note (comment) (HNO) in the Payor Communication navigator section. Each comment is related to a specific recipient in the context of a specific patient and encounter. The comment in this column is related to the recipient in the AGENCY_ID column of this table. There can be several recipients added to the Payor Comm navigator section for each patient. Each recipient represents a contact (fax/phone/name) for a payor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AGENCY_ID` | [CLARITY_AGENCY](CLARITY_AGENCY.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

