# CANCER_RISK_REQ_INFO

> This table contains the externally requested cancer risk scores info for a patient.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `SCORE_REQ_USER_ID` | VARCHAR |  | This column stores the user who requested cancer risk scores. |
| 4 | `SCORE_REQ_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `SCORE_REQ_INST_UTC_DTTM` | DATETIME (UTC) |  | This column stores the instant when the user requested the cancer risk scores. This column always stores a UTC instant value with no time zone marker. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

