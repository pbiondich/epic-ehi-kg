# AVS_ESIG_INFO

> Contains data regarding After Visit Summary (AVS) e-signatures.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `AVS_ESIG_USER_ID` | VARCHAR |  | User that is performing the E-Signing of the After Visit Summary |
| 7 | `AVS_ESIG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `AVS_ESIG_INST_DTTM` | DATETIME (UTC) |  | Instant at which the After Visit Summary is E-Signed |
| 9 | `AVS_ESIG_DCS_ID` | VARCHAR |  | Document record that contains the After Visit Summary, including the E-Signature. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

