# DENT_ORTHO_APPLIANCE

> Includes data for orthodontic appliances.

**Primary key:** `FINDING_ID`, `CONTACT_DATE_REAL`  
**Columns:** 16  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `APPLIANCE_STATUS_C_NAME` | VARCHAR |  | This item stores the status for an orthodontics appliance. |
| 5 | `APPL_START_DATE` | DATETIME |  | This item stores the start date for an orthodontics appliance. |
| 6 | `EST_DURATION` | INTEGER |  | This item stores the estimated duration (in months) for an orthodontics appliance. |
| 7 | `REMOVAL_DATE` | DATETIME |  | This item stores the removal date for an orthodontics appliance. |
| 8 | `MODIFIED_INST_DTTM` | DATETIME (UTC) |  | History item that tracks every instant an orthodontic appliance has been modified. |
| 9 | `MODIFIED_USER_ID` | VARCHAR |  | Stores the user that modified orthodontics appliance data for this history line. |
| 10 | `MODIFIED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `MODIFIED_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the patient CSN where data was modified for this history line. |
| 12 | `WEAR_TIME_C_NAME` | VARCHAR |  | This item stores the daily wear time for an orthodontics appliance. |
| 13 | `DENT_APP_C_NAME` | VARCHAR | org | This item stores the category for this appliance. This category maps to the LSD-98600 table. |
| 14 | `APPLNC_ND_RPL_YN` | VARCHAR |  | This item indicates whether this appliance is broken. This category maps to the ECT-101 table. |
| 15 | `APPLNC_RPL_ARCH_C_NAME` | VARCHAR |  | This item indicates which arch or arches have appliances that need replacement. |
| 16 | `BRAND_C_NAME` | VARCHAR | org | This item stores the brand for an orthodontics appliance. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MODIFIED_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

