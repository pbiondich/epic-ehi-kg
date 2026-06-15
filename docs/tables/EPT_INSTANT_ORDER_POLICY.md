# EPT_INSTANT_ORDER_POLICY

> This table lists policies defined by an Instant Orders action in an advisory that have been acknowledged by an end user for a patient's encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `INST_ORD_LOCATOR_ID_LOCATOR_NAME` | VARCHAR |  | The name of the Locator record. |
| 7 | `INST_ORD_RESPONSE_YN` | VARCHAR |  | Stores whether the policy may be enacted upon |
| 8 | `INST_ORD_USER_ID` | VARCHAR |  | Stores the user that acknowledged the policy |
| 9 | `INST_ORD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `INST_ORD_RESP_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant that the policy was acknowledged |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

