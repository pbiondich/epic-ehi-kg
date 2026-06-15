# EXT_FORMULARY_ID

> This table contains the external formulary ID values.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 25  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 7 | `EXT_FORM_ID` | VARCHAR |  | The unique ID of the external formulary that is associated with this patient encounter. |
| 8 | `EXT_ALT_ID` | VARCHAR |  | This unique ID of the external alternative formulary associated with this patient encounter. |
| 9 | `EXT_PHARM_CVG_ID` | VARCHAR |  | The unique ID of the external pharmacy coverage associated with this patient encounter. |
| 10 | `EXT_COPAY_ID` | VARCHAR |  | The unique ID of the external copay associated with this patient encounter. |
| 11 | `EXT_FORM_ID_LINE` | INTEGER |  | This column contains the external formulary ID line. |
| 12 | `EXTERNAL_RX_TYPE_C_NAME` | VARCHAR | org | The pharmacy coverage type category number for this patient encounter. |
| 13 | `EXT_PHARMACY_NETWORK_IDENT` | VARCHAR |  | The unique ID of the external pharmacy network associated with this patient encounter. |
| 14 | `EXT_PROD_EXCLUSION_IDENT` | VARCHAR |  | External Product Exclusion ID |
| 15 | `EXT_PRIOR_AUTH_IDENT` | VARCHAR |  | External Prior Authorization ID |
| 16 | `EXT_STEP_THERAPY_PRODS_IDENT` | VARCHAR |  | External Step Therapy Products ID |
| 17 | `EXT_AGE_LIMIT_IDENT` | VARCHAR |  | External Age Limit ID |
| 18 | `EXT_GENDER_LIMIT_IDENT` | VARCHAR |  | External Gender Limit ID |
| 19 | `EXT_QUANTITY_LIMIT_IDENT` | VARCHAR |  | External Quantity Limit ID |
| 20 | `EXT_SPECIALTY_PRODUCTS_IDENT` | VARCHAR |  | External Specialty Products ID |
| 21 | `EXT_ALTERNATIVE_GROUPS_IDENT` | VARCHAR |  | External Alternative Groups ID |
| 22 | `EXT_STEP_THERAPY_GROUPS_IDENT` | VARCHAR |  | External Step Therapy Product Groups ID |
| 23 | `EXT_MESSAGE_FILE_IDENT` | VARCHAR |  | External Message File ID |
| 24 | `EXT_GENERAL_MESSAGE_IDENT` | VARCHAR |  | External General Message ID |
| 25 | `EXT_PHARM_CHN_IDENT` | VARCHAR |  | External Pharmacy Chain ID |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

