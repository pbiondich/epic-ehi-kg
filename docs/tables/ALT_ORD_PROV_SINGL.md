# ALT_ORD_PROV_SINGL

> This table contains single response items for alternate ordering providers.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 14  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 3 | `ALT_ORD_PRV_NAME` | VARCHAR |  | The name of the alternate ordering provider. |
| 4 | `ALT_ORD_PRV_CITY` | VARCHAR |  | The city for alternate ordering providers. |
| 5 | `ALT_ORD_PRV_ZIP` | VARCHAR |  | The zipcode for alternate ordering providers. |
| 6 | `ALT_ORD_PRV_PHONE` | VARCHAR |  | The phone number for alternate ordering providers. |
| 7 | `ALT_ORD_PRV_FAX` | VARCHAR |  | The fax number for alternate ordering providers. |
| 8 | `ALT_ORD_PRV_EMAIL` | VARCHAR |  | The email address for alternate ordering providers. |
| 9 | `ALT_ORD_PRV_UPIN` | VARCHAR |  | The Unique physician identification number (UPIN) for alternate ordering providers. |
| 10 | `ALT_ORD_PRV_TAX_ID` | VARCHAR |  | The tax identification number for alternate ordering providers. |
| 11 | `ALT_ORD_PRV_TITLE_NAME` | VARCHAR | org | The title of the alternate ordering provider. |
| 12 | `ALT_ORD_PRV_RVW_C_NAME` | VARCHAR | org | The last reviewed status of the alternate ordering provider. |
| 13 | `ALT_ORD_PRV_HOUSE_N` | VARCHAR |  | The house number for alternate ordering providers. |
| 14 | `ALT_ORD_PRV_DIST_C_NAME` | VARCHAR | org | The district for alternate ordering providers. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

