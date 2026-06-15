# PAT_DIFF_DX

> This table will contain all of the differential diagnosis entries for a particular encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the differential diagnosis associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `DIFF_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `DIFF_DX_DESC` | VARCHAR |  | The text description of the differential diagnosis. |
| 7 | `DIFF_DX_QUALIFIER_C_NAME` | VARCHAR | org | Stores the category number of the qualifier for the differential diagnosis. |
| 8 | `DIFF_DX_STATUS_C_NAME` | VARCHAR |  | Stores the category number of the status for the differential diagnosis. |
| 9 | `DIFF_DX_COMMENT` | VARCHAR |  | The comment for the differential diagnosis entered by the user. |
| 10 | `DIFF_DX_UNIQUE` | VARCHAR |  | The unique identifier associated with this differential diagnosis that is used to distinguish between other diagnosis entries. |
| 11 | `DIFF_CHRONIC_YN` | VARCHAR |  | Indicates whether the differential diagnosis is chronic. |
| 12 | `DDX_LINK_PROB_ID` | NUMERIC |  | Stores the unique ID of the problem used to create the differential diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

