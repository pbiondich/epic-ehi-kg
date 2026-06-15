# SMOKING_CESS_HX

> This table is for the Historical Smoking Cessation items: Ready to Quit Historical, Counseling Given Historical, Smoking Cessation Historical Update User, and Smoking Cessation Historical Update Instant.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `READY_QT_HX_C_NAME` | VARCHAR |  | This column holds historical data for whether or not the patient stated they were ready to quit smoking. |
| 4 | `COUNSELING_GVN_HX_C_NAME` | VARCHAR |  | This column holds historical data for whether or not counseling was given to a patient who smokes. |
| 5 | `SMK_CESS_HX_DT_DTTM` | DATETIME (UTC) |  | This column stores the date and time the corresponding entries in the Smoking Cessation Historical items were updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

