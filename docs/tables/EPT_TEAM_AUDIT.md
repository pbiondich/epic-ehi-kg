# EPT_TEAM_AUDIT

> This table represents the audit trail for team-based actions taken for a patient.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `TEAM_AUDIT_ID` | NUMERIC |  | The unique ID of the Provider Care Team associated with this team audit line. |
| 6 | `TEAM_AUDIT_ID_RECORD_NAME` | VARCHAR |  | The name of the record. |
| 7 | `TEAM_ACTION_C_NAME` | VARCHAR | org | The category ID of the action taken for this line of the team audit. |
| 8 | `PRIMARYTEAM_AUDI_YN` | VARCHAR |  | Indicates whether this line of the team audit shows that the team was the primary team. |
| 9 | `CONTACT_AUDIT_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 10 | `TEAMAUDIT_USER_ID` | VARCHAR |  | The unique ID associated with the user responsible for adding the audit line. This column is frequently used to link to the CLARITY_EMP table. |
| 11 | `TEAMAUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `TEAM_AUDIT_INSTANT` | DATETIME (Local) |  | The instant when the audit line was added. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

