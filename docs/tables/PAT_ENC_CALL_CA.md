# PAT_ENC_CALL_CA

> This table contains the Care Advice (LPA) records given to the Patient in a Call Center call.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE` | INTEGER | PK | The line number for the patient call care advice. |
| 2 | `CONTACT_DATE` | DATETIME |  | The date for the encounter in standard date format. |
| 3 | `CARE_ADVICE_GIVEN_CARE_ADVICE_NAME` | VARCHAR |  | The name of the care advice record. |
| 4 | `CA_GIVEN_DAT` | FLOAT |  | The version number of the care advice given. |
| 5 | `CA_GIVEN_BY` | VARCHAR |  | The unique ID of the user giving the care advice. |
| 6 | `CA_GIVEN_BY_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `CA_GIVEN_DATE` | DATETIME (Local) |  | The date when the care advice was given. |
| 8 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 9 | `CARE_ADVICE_HNO_ID` | VARCHAR |  | The Note ID that contains the modified care advice. |
| 10 | `CARE_ADVICE_PROTOCOL_ID` | NUMERIC |  | Stores the Protocol ID that the given care advice is associated with. |
| 11 | `CARE_ADVICE_PROTOCOL_ID_PROTOCOL_NAME` | VARCHAR |  | The display name of the protocol. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

