# PAT_MYC_EVIST_PMNT

> During an e-visit encounter, a message may be sent to the patient containing an e-visit payment request task. This table contains a list of those messages. Typically only one payment request will be sent per encounter, however it is possible to have multiple payment requests therefore the primary key of this table is comprised of PAT_ENC_CSN_ID, and LINE in which LINE is used to identify each payment request message associated with the encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | The line count used to identify different messages containing payment links for each encounter. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | ID of the deployment owner for this contact. |
| 5 | `PMNT_RQST_MSG_ID` | VARCHAR |  | The unique identifier for the patient message records associated with this encounter that contain payment tasks. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

