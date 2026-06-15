# PAT_ENC_DX

> The patient encounter diagnosis table contains one record for each diagnosis associated with each encounter level of service. This table will contain all diagnoses specified on the Order Summary screen.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 2 | `LINE` | INTEGER | PK | The line number of the diagnosis within the encounter. This is the second column in the primary key and uniquely identifies this diagnosis on the encounter. |
| 3 | `CONTACT_DATE` | DATETIME |  | The contact date of the encounter associated with this diagnosis. Note: There may be multiple encounters on the same calendar date. |
| 4 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 5 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `ANNOTATION` | VARCHAR |  | The annotation (description) text entered for this diagnosis by the clinical system user. This field is NULL if no annotation was entered during the encounter. Order entry in clinical system limits this field to 160 characters. |
| 7 | `DX_QUALIFIER_C_NAME` | VARCHAR | org | The category value for the diagnosis qualifier. This field is null if no qualifier was entered. |
| 8 | `PRIMARY_DX_YN` | VARCHAR |  | This is a one character field that indicates whether this diagnosis was the primary diagnosis for the encounter. If the diagnosis was the primary this field will have a value of 'Y' otherwise it will have a value of 'N'. |
| 9 | `COMMENTS` | VARCHAR |  | Any text comment associated with the encounter diagnosis. This field is NULL if no comment was provided. |
| 10 | `DX_CHRONIC_YN` | VARCHAR |  | Stores the chronic flag for a diagnosis. |
| 11 | `DX_STAGE_ID` | NUMERIC |  | The stage for the diagnosis. |
| 12 | `DX_UNIQUE` | VARCHAR |  | Unique identifier given when a diagnosis is added to the encounter diagnosis list. |
| 13 | `DX_ED_YN` | VARCHAR |  | Definitively identifies an encounter diagnosis (I EDG 18400) as being an ED clinical impression. This is important to differentiate ED diagnoses from diagnoses filed to the same item as in the IP setting. |
| 14 | `DX_LINK_PROB_ID` | NUMERIC |  | Stores the problem ID of the linked problem. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

