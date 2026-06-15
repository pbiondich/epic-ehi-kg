# PAT_ENC_DSS_MED_COND

> The PAT_ENC_DSS_MED_COND table contains information about the medical indications or conditions associated with a patient order that have been sent to a decision support system to receive a response.

**Primary key:** `PAT_ENC_CSN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated DSS response for a patient order. Together with PAT_ENC_CSN_ID, this forms the foreign key to the PAT_ENC_DSS table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple medical indications associated with a patient order from the table PAT_ENC_DSS. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `DSS_MEDICAL_COND_ID` | NUMERIC |  | The unique ID of the medical indication that is associated with the Decision Support System (DSS) response. |
| 8 | `DSS_MEDICAL_COND_ID_MEDICAL_COND_NAME` | VARCHAR |  | This contains the name of the medical condition. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

