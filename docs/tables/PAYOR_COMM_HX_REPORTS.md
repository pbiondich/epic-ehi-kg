# PAYOR_COMM_HX_REPORTS

> A list of reports sent with the payer communication.

**Primary key:** `PAT_ENC_CSN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated payer communication. Together with the PAT_ENC_CSN_ID column, this forms the foreign key to the PAYOR_COMM_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the attachments sent a communication associated with the patient encounter and communication from the PAYOR_COMM_HX table. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `REPORT_ID` | VARCHAR | FK→ | The unique ID of the report that was sent to the payor. This column should only be used as a fallback if no Release of Information (ROI) is available in ROI_ID (such as in an IntraConnect scenario). |
| 8 | `REPORT_ID_REPORT_NAME` | VARCHAR |  | The name of the report |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REPORT_ID` | [CLARITY_RPT](CLARITY_RPT.md) | sole_pk | high |

