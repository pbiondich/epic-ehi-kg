# RQG_DB_MAIN

> This table contains information about the Requisition Grouper (RQG) Source: ID Number, Name, Sex, Gender Identity, Sex Assigned at Birth, DOB or Age, SSN, Species, Ethnic Group, City, State, Zip Code, County, Country, House Number, District, Status, and Email. This table also contains the gamete donor ID, date of donation, age of donation, donation bank name, and the donor's relationship with the patient for gamete donor RQG records.

**Primary key:** `RQG_GROUPER_ID`  
**Columns:** 20  
**Org-specific columns:** 8  
**Joined by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RQG_GROUPER_ID` | NUMERIC | PK | This is the primary key for RQG tables and refers to the ID number of the source Requisition Grouper. |
| 2 | `RQG_GROUPER_NAME` | VARCHAR |  | This is the name of the Requisition Grouper source. |
| 3 | `RQG_RECORD_STAT_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) of the Requisition Grouper source. This category list is stored in ECT 1000. |
| 4 | `RQG_DOB_DT` | DATETIME |  | This is the Date of Birth of the Requisition Grouper source. |
| 5 | `RQG_SEX_C_NAME` | VARCHAR | org | This is the sex of the Requisition Grouper source. This category list is stored in EPT 130. |
| 6 | `RQG_SSN` | VARCHAR |  | This is the SSN of the Requisition Grouper source. |
| 7 | `RQG_AGE_UNITS_C_NAME` | VARCHAR |  | Units for the age of the requisition grouper |
| 8 | `RQG_CITY` | VARCHAR |  | The city of the requisition grouper's address. |
| 9 | `RQG_STATE_C_NAME` | VARCHAR | org | The state category number of the requisition grouper's address. |
| 10 | `RQG_ZIP` | VARCHAR |  | The ZIP code of the requisition grouper's address. |
| 11 | `RQG_COUNTY_C_NAME` | VARCHAR | org | The county category number of the requisition grouper's address. |
| 12 | `RQG_COUNTRY_C_NAME` | VARCHAR | org | The country category number of the requisition grouper's address. |
| 13 | `RQG_HOUSE_NUM` | VARCHAR |  | The house number of the requisition grouper's address. |
| 14 | `RQG_DISTRICT_C_NAME` | VARCHAR | org | The district category number of the requisition grouper's address. |
| 15 | `ETHNIC_GROUP_C_NAME` | VARCHAR | org | This item stores the ethnic group a patient belongs to. |
| 16 | `RQG_BIRTH_TM` | DATETIME (Local) |  | The date and time of birth of the Requisition Grouper source. |
| 17 | `GENDER_IDENTITY_C_NAME` | VARCHAR | org | The gender identity category ID for the patient. |
| 18 | `SEX_ASGN_AT_BIRTH_C_NAME` | VARCHAR | org | The sex assigned at birth category ID for the patient. |
| 19 | `EMAIL_ADDRESS` | VARCHAR |  | The email address of the record. |
| 20 | `RQG_AGE_NUM` | NUMERIC |  | The age of the requisition grouper, including decimal values when applicable. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (8)

| From | Column | Confidence |
|------|--------|------------|
| [ACCOUNT_RQG_GROUPERS](ACCOUNT_RQG_GROUPERS.md) | `RQG_GROUPER_ID` | high |
| [BAT_REL_GRP](BAT_REL_GRP.md) | `RQG_GROUPER_ID` | high |
| [EOW_LINKED_RQGS](EOW_LINKED_RQGS.md) | `RQG_GROUPER_ID` | high |
| [GNOM_INTPRT_IDENT](GNOM_INTPRT_IDENT.md) | `RQG_GROUPER_ID` | high |
| [HNO_LINKED_RQGS](HNO_LINKED_RQGS.md) | `RQG_GROUPER_ID` | high |
| [REQ_ALL_MAIN](REQ_ALL_MAIN.md) | `RQG_GROUPER_ID` | high |
| [RQG_NAME_HISTORY](RQG_NAME_HISTORY.md) | `RQG_GROUPER_ID` | high |
| [V_EHI_HNO_LINKED_RQGS](V_EHI_HNO_LINKED_RQGS.md) | `RQG_GROUPER_ID` | high |

