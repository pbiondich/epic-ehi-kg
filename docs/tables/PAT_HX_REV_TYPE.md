# PAT_HX_REV_TYPE

> This table contains information types of history that were reviewed for a patient, such as Medical, Surgical, Socioeconomic, Alcohol, Tobacco, etc. Where in the application a type of history was reviewed is in the PAT_HX_REV_TOPIC table. Additional information about when a patient's history was reviewed and by whom is found in the PAT_HX_REVIEW table.

**Primary key:** `PAT_ENC_CSN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated instance of history review in this encounter. Together with PAT_ENC_CSN_ID, this forms the foreign key to the PAT_HX_REVIEW table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple history types that were reviewed for the associated instance of review and encounter from the PAT_HX_REVIEW table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `HX_REVIEWED_TYPE_C_NAME` | VARCHAR |  | The category value associated with the type of History Visit Navigator topic that was reviewed, such as Medical, Surgical, Socioeconomic, etc. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

