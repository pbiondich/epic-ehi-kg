# BREAST_IMG_HORMONES

> Breast Imaging relevant hormone history data.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `HORMONE_C_NAME` | VARCHAR | org | The mammography hormones category ID for the patient. |
| 4 | `START_DATE` | DATETIME |  | The date when the patient began taking the related hormone. |
| 5 | `END_DATE` | DATETIME |  | The date when the patient stopped taking the related hormone. |
| 6 | `COMMENT_NOTE_ID` | VARCHAR |  | The note ID for free-text information about the hormone history for this patient. |
| 7 | `CURRENTLY_TAKING_YN` | VARCHAR |  | Indicates whether the patient is currently taking hormones. 'Y' indicates that the patient is currently taking hormones. 'N' or NULL indicates that the patient is not. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

