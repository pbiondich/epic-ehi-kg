# SOCIAL_HX_ALC_USE

> The SOCIAL_HX_ALC_USE table contains social alcohol history data entered in clinical system patient encounters. Note: Typically, only the most recent social history data for a patient is extracted. However, you may elect to extract all social history contacts if you wish. In this case, since one patient encounter may contain multiple social history contacts, each contact is uniquely identified by a combination of the patient encounter serial number and a line number.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The contact date on which the history information was collected. |
| 4 | `ALCOHOL_DRINKS_WK` | VARCHAR |  | Stores the alcohol history of drinks per week. |
| 5 | `HX_DRINK_TYPES_C_NAME` | VARCHAR | org | Stores the type of alcohol consumed for alcohol history. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

