# DOCS_RCVD_OB_HX

> This table contains OB History information received from other organizations.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 28  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `ADOPTION_TYPE_C_NAME` | VARCHAR | org | Adoption type for this delivery. |
| 5 | `ADOPTION_TYPE_NAME` | VARCHAR |  | Category title for the adoption type for this delivery from the source environment. |
| 6 | `ANTENAT_STEROIDS_C_NAME` | VARCHAR |  | Antenatal steroids given. |
| 7 | `CORD_CLAMP_UTC_DTTM` | DATETIME (UTC) |  | Instant when the cord was clamped. |
| 8 | `DILA_COMPL_UTC_DTTM` | DATETIME (UTC) |  | Instant when dilation completed. |
| 9 | `FORCEPS_ATTEMPTED_YN` | VARCHAR |  | Whether delivery by forceps was attempted. |
| 10 | `LABOR_ATTEMPTED_YN` | VARCHAR |  | Whether a trial of labor was attempted. |
| 11 | `LABOR_ST_UTC_DTTM` | DATETIME (UTC) |  | Instant when labor began. |
| 12 | `LABOR_TYPE_C_NAME` | VARCHAR |  | The type of labor for this birth. |
| 13 | `LIVING_STAT_BIRTH_C_NAME` | VARCHAR | org | Living status of the baby at birth. |
| 14 | `PLAC_DEL_UTC_DTTM` | DATETIME (UTC) |  | Instant when the placenta was delivered. |
| 15 | `LIV_STAT_BIRTH_NAME` | VARCHAR |  | Category title for the living status of the baby at birth from the source environment. |
| 16 | `PUSH_START_UTC_DTTM` | DATETIME (UTC) |  | Instant when pushing began. |
| 17 | `RUPTURE_UTC_DTTM` | DATETIME (UTC) |  | Instant when rupture of membranes occurred. |
| 18 | `RUPT_2_DEL_SEC` | INTEGER |  | Time from rupture of membranes to delivery in seconds. |
| 19 | `SKIN_2_SK_UTC_DTTM` | DATETIME (UTC) |  | Instant when skin to skin was initiated. |
| 20 | `VAC_ATTEMPTED_YN` | VARCHAR |  | Whether delivery by vacuum was attempted. |
| 21 | `MOM_DEL_ENC_IDENT` | VARCHAR |  | Maternal delivery encounter associated with the birth. |
| 22 | `BABY_DEL_ENC_IDENT` | VARCHAR |  | Newborn delivery encounter associated with the birth. |
| 23 | `MOTHER_ARR_UTC_DTTM` | DATETIME (UTC) |  | Instant when the mother arrived at labor and delivery. |
| 24 | `CERV_RIPE_UTC_DTTM` | DATETIME (UTC) |  | Cervical ripening instant for this delivery. |
| 25 | `PREGRAVID_WEIGHT` | NUMERIC |  | Pregravid weight for this delivery. |
| 26 | `PLAN_DEL_MTHD_C_NAME` | VARCHAR |  | Planned delivery method for this delivery. |
| 27 | `PLAN_DEL_MTHD_NAME_STR` | VARCHAR |  | Category title for the planned delivery method from the source environment. |
| 28 | `BABY_LINK_PAT_ID` | VARCHAR | FK→ | The link to the baby that was born. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BABY_LINK_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

