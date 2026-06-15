# EXT_ELIG_STATUS

> This table stores results of eligibility queries returned by RxHub. The related External Eligibility Query Line information is stored in the EXT_ELIG_STATUS_1 table.

**Overflow family:** [EXT_ELIG_STATUS_1](EXT_ELIG_STATUS_1.md)  
**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `EXT_FORM_STATUS_C_NAME` | VARCHAR |  | The external formulary query status category number for this eligibility query. |
| 8 | `EXT_FORM_SENT_TM` | DATETIME (Local) |  | The date and time when the external formulary query was sent. |
| 9 | `EXT_FORM_RECVD_TM` | DATETIME (Local) |  | The date and time that the external formulary query was received. |
| 10 | `EXT_FORM_ACUTE_YN` | VARCHAR |  | Flag to indicate if the eligibility query was sent as an acute care query. |
| 11 | `ACUTE_CARE_MSG` | VARCHAR |  | To store the message ID returned from ISA13 in the query so we can send it in the med history request |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

