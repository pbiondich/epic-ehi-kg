# HOLOGRAM_AMBIENT_FAM_HX

> This table contains information about the Ambient family history choices that were presented to a clinician.

**Primary key:** `HOLOGRAM_ID`, `CONTACT_DATE_REAL`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HOLOGRAM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the hologram record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `FAM_STAT_REL_C_NAME` | VARCHAR | org | Contains a family history relationship that is temporarily stored in a hologram record. |
| 4 | `FAM_STAT_ID` | INTEGER |  | Contains a family history relative ID that is temporarily stored in a hologram record. |
| 5 | `FAM_STT_NAM` | VARCHAR |  | Contains a family history relative name that is temporarily stored in a hologram record. |
| 6 | `FAM_STAT_STATUS_C_NAME` | NUMERIC |  | Contains a family history relative status that is temporarily stored in a hologram record. |
| 7 | `FAM_MEDICAL_HX_C_NAME` | NUMERIC | org | Contains a family history problem category that is temporarily stored in a hologram record. |
| 8 | `FAM_MEDICAL_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 9 | `AGE_OF_ONSET` | NUMERIC |  | Contains a family history problem age of onset that is temporarily stored in a hologram record. |
| 10 | `AGE_OF_ONSET_END` | NUMERIC |  | Contains a family history problem age of onset end that is temporarily stored in a hologram record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HOLOGRAM_ID` | [HOLOGRAM_DETAILS](HOLOGRAM_DETAILS.md) | sole_pk | high |

