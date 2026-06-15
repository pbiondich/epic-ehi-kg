# DP_COMM_ATTACHMENTS

> This table contains attachments that were sent with a communication in the Continued Care and Services Coordination workflow.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `COMM_IDENTIFIER` | INTEGER |  | Unique identifier for a communication sent from CCSC. Together with the PAT_ENC_CSN_ID column, this forms the foreign key to the DP_COMM_IDENTIFIER_RM table. |
| 7 | `REPORT_ID` | VARCHAR | FK→ | The unique ID of the report sent with the communication. |
| 8 | `REPORT_ID_REPORT_NAME` | VARCHAR |  | The name of the report |
| 9 | `IS_CUSTOM_DOCUMENT_YN` | VARCHAR |  | Whether this attachment represents a custom document generated using document builder. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REPORT_ID` | [CLARITY_RPT](CLARITY_RPT.md) | sole_pk | high |

