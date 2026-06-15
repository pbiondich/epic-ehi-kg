# PAT_ENC_CALL_CMTS

> This table stores information regarding the free-text comments entered in Protocols during clinical calls.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `SEC_PROTOCOL_ID` | NUMERIC |  | ID of the Protocol Section within which a triager has left a comment. |
| 7 | `SEC_PROTOCOL_ID_PROTOCOL_NAME` | VARCHAR |  | The display name of the protocol. |
| 8 | `SEC_PROTOCOL_CNCT` | NUMERIC |  | DTE of the protocol section LPT record that the comment was left on. Note that the source item is a DAT value - Clarity does not support DAT columns, so we have to transform it into a DTE. |
| 9 | `SEC_PROTOCOL_ROW` | INTEGER |  | Number corresponding to the Protocol Section row (I LPT 230 line) on which a triager has left a comment. Special case: All Negative rows do not have a corresponding I LPT 230 line, and are stored as special value "-1". |
| 10 | `CMT_USER_ID` | VARCHAR |  | User ID of the triager who left a comment on a Nurse Triage protocol. |
| 11 | `CMT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `CMT_INST_UTC_DTTM` | DATETIME (UTC) |  | Instant (in UTC) of the last edit to this protocol comment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

