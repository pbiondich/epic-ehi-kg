# FIN_ASST_CASE

> This table contains basic information about a financial assistance case record.

**Primary key:** `FIN_ASST_CASE_ID`  
**Columns:** 39  
**Org-specific columns:** 3  
**Joined by:** 32 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK | The unique identifier for the financial assistance case record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 3 | `EXTERNAL_ID` | INTEGER |  | This column stores the external unique identifier for a financial assistance case record. |
| 4 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `APPL_PROVIDED_DATE` | DATETIME |  | The date a financial assistance application was provided to the patient. |
| 6 | `APPL_SIGNED_DATE` | DATETIME |  | The date a completed and signed financial assistance application was submitted by the patient. |
| 7 | `FAMILY_SIZE` | INTEGER |  | The size of the patient's family when this case was created. |
| 8 | `PERCENT_FPL` | NUMERIC |  | The percentage of federal poverty level of the patient calculated using income details (stored in FIN_ASST_CASE_INCOME table). |
| 9 | `PERCENT_FPL_AFTER_EXPENSES` | NUMERIC |  | The percentage of federal poverty level of the patient calculated after subtracting expenses (stored in FIN_ASST_CASE_EXPENSE table) from income details (stored in FIN_ASST_CASE_INCOME table). |
| 10 | `TOTAL_ANNUAL_INCOME_AFTER_EXP` | NUMERIC |  | The total income after expenses for the patient's household. |
| 11 | `STATUS_C_NAME` | VARCHAR |  | The status category ID for the financial assistance case record. |
| 12 | `TOTAL_ANNUAL_INCOME` | NUMERIC |  | Total annual income of the patient's household. |
| 13 | `ACCOUNT_ID` | NUMERIC | FK→ | The unique ID of the guarantor record associated with the financial assistance case record. |
| 14 | `PROPENSITY_TO_PAY_C_NAME` | VARCHAR | org | The guarantor propensity to pay category ID for the financial assistance case record. |
| 15 | `CREDIT_SCORE` | INTEGER |  | The guarantor's credit score associated with the financial assistance case record. |
| 16 | `FIN_ASST_CASE_CRT_SRC_C_NAME` | VARCHAR |  | The way this case record was created. |
| 17 | `MYCHART_USER_ENTERED_CMT` | VARCHAR |  | This column stores the free-text additional information provided with the financial assistance application by patient/requestor through MyChart. |
| 18 | `CREATED_BY_WPR_ID` | VARCHAR |  | This item stores the user ID of the MyChart user who created this case. Only populated when the case is created through MyChart. |
| 19 | `CASE_CONTACT_ACCOUNT_ID` | NUMERIC |  | The unique ID of the guarantor account who is the primary contact for this financial assistance case record. |
| 20 | `TYPE_C_NAME` | VARCHAR |  | The case type category ID for the financial assistance case record. |
| 21 | `CASE_WORKFLOW_C_NAME` | VARCHAR | org | The category ID of the workflow the financial assistance case record is created in. |
| 22 | `FISCAL_YEAR` | INTEGER |  | The fiscal year the financial information in the case record belongs to. |
| 23 | `NUMBER_OF_DEPENDENTS` | INTEGER |  | Number of dependents the patient for whom this financial assistance case record is for has. |
| 24 | `FPL_CALCULATION_DATE` | DATETIME |  | The date the federal poverty level stored in PERCENT_FPL and PERCENT_FPL_AFTER_EXPENSES columns was last calculated. |
| 25 | `NO_INCOME_YN` | VARCHAR |  | Flag that indicates that the household doesn't have any source of income |
| 26 | `REQ_LAST_WORKED_UTC_DTTM` | DATETIME (UTC) |  | Last time a patient viewed or edited the financial assistance application in MyChart. |
| 27 | `DECLINE_ASSIST_UTC_DTTM` | DATETIME (UTC) |  | The instant set after a primary contact declines financial assistance online. |
| 28 | `ENTITY_DEC_ASST_C_NAME` | VARCHAR |  | The entity that declined a Waiting for Patient financial assistance request. |
| 29 | `FIN_ASST_CASE_NAME` | VARCHAR |  | Name of the primary patient on the financial assistance case. |
| 30 | `REC_CREATION_DATE` | DATETIME |  | Stores the date the record was created |
| 31 | `SOURCE_FIN_ASST_CASE_ID` | NUMERIC |  | If this case was created and copied from an existing case, this contains the source case that the data was taken from. |
| 32 | `PAT_FAMILY_SIZE` | INTEGER |  | This item stores the family size entered by the patient. |
| 33 | `PAT_NO_INCOME_YN` | VARCHAR |  | Flag that indicates that the household doesn't have any source of income entered by the patient. |
| 34 | `PAT_PERCENT_FPL` | NUMERIC |  | The patient's income percentage, based on income reported by the patient, of the federal poverty level based on family size and annual income. |
| 35 | `PAT_PERCENT_FPL_AFTER_EXP` | NUMERIC |  | The patient's income percentage, based on income reported by the patient, of the federal poverty level based on family size, annual income, and annual expenses (reported by the patient). |
| 36 | `PAT_TOTAL_ANNUAL_INCOME` | NUMERIC |  | Total annual income of the patient's household, calculated from the patient reported income. |
| 37 | `PAT_ANNUAL_INCOME_AFTER_EXP` | NUMERIC |  | Total income after expenses for the patient's household, calculated from the patient reported income and expenses. |
| 38 | `DECLINE_ASSISTANCE_REASON_C_NAME` | VARCHAR | org | The reason the primary contact declined financial assistance. |
| 39 | `PRESCREEN_STATUS_C_NAME` | VARCHAR |  | Status of the pre-screening for the financial assistance case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |

## Joined in — referenced by (32)

| From | Column | Confidence |
|------|--------|------------|
| [FA_CASE_SERVICE_AREAS](FA_CASE_SERVICE_AREAS.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_APPL_DOC](FIN_ASST_CASE_APPL_DOC.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_ASSET](FIN_ASST_CASE_ASSET.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_ASSET_DOCS](FIN_ASST_CASE_ASSET_DOCS.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_ASSOC_PAT](FIN_ASST_CASE_ASSOC_PAT.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_ASSOC_TRKR](FIN_ASST_CASE_ASSOC_TRKR.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_DOCS_HX](FIN_ASST_CASE_DOCS_HX.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_DOCUMENTS](FIN_ASST_CASE_DOCUMENTS.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_EXPENSE](FIN_ASST_CASE_EXPENSE.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_EXP_DOCS](FIN_ASST_CASE_EXP_DOCS.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_FLAG](FIN_ASST_CASE_FLAG.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_FLAG_UPD_HX](FIN_ASST_CASE_FLAG_UPD_HX.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_INCOME](FIN_ASST_CASE_INCOME.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_INCOME_DOCS](FIN_ASST_CASE_INCOME_DOCS.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_LNKD_TRKR](FIN_ASST_CASE_LNKD_TRKR.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_PAT_ASSET](FIN_ASST_CASE_PAT_ASSET.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_PAT_AST_DOC](FIN_ASST_CASE_PAT_AST_DOC.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_PAT_EXPENSE](FIN_ASST_CASE_PAT_EXPENSE.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_PAT_EXP_DOC](FIN_ASST_CASE_PAT_EXP_DOC.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_PAT_INCOME](FIN_ASST_CASE_PAT_INCOME.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_PAT_INC_DOC](FIN_ASST_CASE_PAT_INC_DOC.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_SMARTFORM](FIN_ASST_CASE_SMARTFORM.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_TIMING](FIN_ASST_CASE_TIMING.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_CASE_UPDATE_HX](FIN_ASST_CASE_UPDATE_HX.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_LETTER](FIN_ASST_LETTER.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_NOTE](FIN_ASST_NOTE.md) | `FIN_ASST_CASE_ID` | high |
| [FIN_ASST_TRACKER](FIN_ASST_TRACKER.md) | `FIN_ASST_CASE_ID` | high |
| [HSP_BFH_ACT_DATA](HSP_BFH_ACT_DATA.md) | `FIN_ASST_CASE_ID` | high |
| [MYC_CONVO_ABT_FIN_ASST](MYC_CONVO_ABT_FIN_ASST.md) | `FIN_ASST_CASE_ID` | high |
| [SMRTDTA_ELEM_FIN_ASST_CAS](SMRTDTA_ELEM_FIN_ASST_CAS.md) | `FIN_ASST_CASE_ID` | high |
| [SOCIAL_CARE_TRACKER](SOCIAL_CARE_TRACKER.md) | `FIN_ASST_CASE_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_FNC](V_EHI_REG_ITEM_AUDIT_FNC.md) | `FIN_ASST_CASE_ID` | high |

