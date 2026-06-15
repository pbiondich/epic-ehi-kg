# PAT_CALL_DISPTRACK

> The PAT_CALL_DISPTRACK table contains the information about the disposition history of the patient. Each row contains information about the original disposition and the new disposition.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE_COUNT`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 2 | `LINE_COUNT` | INTEGER | PK | The line number of the disposition history within the encounter. |
| 3 | `CONTACT_DATE` | DATETIME |  | The contact date of the encounter associated with this social history contact. Note: There may be multiple encounters on the same calendar date. |
| 4 | `DISP_OLD_C_NAME` | VARCHAR | org | The disposition that was edited, changed, or deleted. |
| 5 | `DISP_NEW_C_NAME` | VARCHAR |  | The new disposition added to the patient record. |
| 6 | `DISP_OVERRD_TIME` | DATETIME (Local) |  | The time the disposition was overridden. |
| 7 | `DISP_OVER_COMMENT` | VARCHAR |  | The comment entered by the user when overriding the disposition. |
| 8 | `DISP_OVER_REASON_C_NAME` | VARCHAR | org | The reason, entered by the user, for overriding the disposition. |
| 9 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

