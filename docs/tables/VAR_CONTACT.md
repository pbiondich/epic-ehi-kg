# VAR_CONTACT

> This table contains the contact specific information for each variance record.

**Primary key:** `VARIANCE_ID`, `CONTACT_DATE_REAL`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VARIANCE_ID` | VARCHAR | PK FK→ | The unique ID for the variance record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The internal contact date for this variance record. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `IMPACT_C_NAME` | VARCHAR | org | The impact rating for this variance contact. |
| 5 | `LAST_UPD_USER_ID` | VARCHAR |  | The unique ID of the user to last update this contact. |
| 6 | `LAST_UPD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `LAST_UPDATE_TIME` | DATETIME (Local) |  | The instance this contact was last updated. |
| 8 | `CONTACT_NUM` | VARCHAR |  | Contact number for the variance contact. |
| 9 | `INSTANT_OF_ENT_DTTM` | DATETIME (Local) |  | The instant of entry. |
| 10 | `READING_CAREPLAN_CSN_ID` | NUMERIC |  | Links to the care plan contact that this variance was documented under |
| 11 | `VARIANCE_COMMENT` | VARCHAR |  | The comment added to a variance on a care plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VARIANCE_ID` | [VARIANCE](VARIANCE.md) | sole_pk | high |

