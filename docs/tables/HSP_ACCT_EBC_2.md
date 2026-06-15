# HSP_ACCT_EBC_2

> This table contains electronic birth certificate information from the Hospital Accounts Receivable (HAR) master file.

**Overflow of:** [HSP_ACCT_EBC](HSP_ACCT_EBC.md)  
**Primary key:** `HSP_ACCOUNT_ID`  
**Columns:** 51  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The unique identifier for the hospital account record. |
| 2 | `CHILD_SUF_C_NAME` | VARCHAR | org | The child suffix category ID for Electronic Birth Certificate information. |
| 3 | `MOM_RES_APT` | VARCHAR |  | Electronic Birth Certificate mother residence apartment number. |
| 4 | `MOM_STAT_RES_C_NAME` | VARCHAR | org | The mother's residence state/territory/country category ID for Electronic Birth Certificate information. |
| 5 | `MOM_EMAIL` | VARCHAR |  | Electronic Birth Certificate mother email. |
| 6 | `MOM_MAIL_APT` | VARCHAR |  | Electronic Birth Certificate mother mailing apartment number. |
| 7 | `MOM_MAIL_ST_C_NAME` | VARCHAR |  | The mother's mailing state/territory/country category ID for Electronic Birth Certificate information. |
| 8 | `MOM_SUF_C_NAME` | VARCHAR |  | The mother's suffix category ID for Electronic Birth Certificate information. |
| 9 | `MOM_BIRTH_ST_C_NAME` | VARCHAR |  | The mother's birth state/territory/country category ID for Electronic Birth Certificate information. |
| 10 | `DAD_SUF_C_NAME` | VARCHAR |  | The father's suffix category ID for Electronic Birth Certificate information. |
| 11 | `DAD_BIRTH_ST_C_NAME` | VARCHAR |  | The father's birth state/territory/country category ID for Electronic Birth Certificate information. |
| 12 | `PUB_CHILD_NM_YN` | VARCHAR |  | Indicates whether this child's name should be published for Electronic Birth Certificate information. |
| 13 | `MOM_HISP_ORGN_CMT` | VARCHAR |  | Electronic Birth Certificate mother's Hispanic origin other comment. |
| 14 | `MOM_RACE_TRIBE_CMT` | VARCHAR |  | Electronic Birth Certificate mother's tribe. |
| 15 | `MOM_RACE_ASIAN_CMT` | VARCHAR |  | Electronic Birth Certificate mother's race other Asian comment. |
| 16 | `MOM_RACE_PC_ISL_CMT` | VARCHAR |  | Electronic Birth Certificate mother's race other Pacific Islander comment. |
| 17 | `MOM_RACE_OTHER_CMT` | VARCHAR |  | Electronic Birth Certificate mother's race other comment. |
| 18 | `DAD_HISP_ORGN_CMT` | VARCHAR |  | Electronic Birth Certificate father's Hispanic origin other comment. |
| 19 | `DAD_RACE_TRIBE_CMT` | VARCHAR |  | Electronic Birth Certificate father's tribe. |
| 20 | `DAD_RACE_ASIAN_CMT` | VARCHAR |  | Electronic Birth Certificate father's race other Asian comment. |
| 21 | `DAD_RACE_PC_ISL_CMT` | VARCHAR |  | Electronic Birth Certificate father's race other Pacific Islander comment. |
| 22 | `DAD_RACE_OTHER_CMT` | VARCHAR |  | Electronic Birth Certificate father's race other comment. |
| 23 | `PLN_HM_BIRTH_YN` | VARCHAR |  | Indicates whether this birth was planned to deliver at home for Electronic Birth Certificate information. |
| 24 | `PLACE_OCCUR_CMT` | VARCHAR |  | Electronic Birth Certificate place where birth occurred comment. |
| 25 | `ATTENDANT_NPI` | VARCHAR |  | Electronic Birth Certificate attendant NPI number. |
| 26 | `ATTENDANT_TITLE_CMT` | VARCHAR |  | Electronic Birth Certificate attendant title other comment. |
| 27 | `MOM_TRANSFERRED_C_NAME` | VARCHAR |  | The mother's transfer status category ID for Electronic Birth Certificate information. |
| 28 | `MOM_TRANS_FROM` | VARCHAR |  | Electronic Birth Certificate area from which the mother was transferred. This item is free-text. |
| 29 | `FIRST_PN_VISIT_DT` | VARCHAR |  | Electronic Birth Certificate date of first prenatal care visit. This date is stored as free-text to capture unknown values. Expected format is MM/DD/YYYY, where zeroes can be substituted for any unknown month, day, or year. |
| 30 | `LAST_PN_VISIT_DT` | VARCHAR |  | Electronic Birth Certificate date of last prenatal care visit. This date is stored as free-text to capture unknown values. Expected format is MM/DD/YYYY, where zeroes can be substituted for any unknown month, day, or year. |
| 31 | `MOM_HEIGHT` | VARCHAR |  | Electronic Birth Certificate mother height. Format: ft/in. |
| 32 | `MOM_PREPREG_WEIGHT` | INTEGER |  | Electronic Birth Certificate pre-pregnancy weight. |
| 33 | `MOM_DELIVERY_WEIGHT` | INTEGER |  | Electronic Birth Certificate delivery weight. |
| 34 | `MOM_WIC_FOOD_C_NAME` | VARCHAR |  | The mother's 'Special Supplemental Nutrition Program for Women, Infants and Children' food status category ID for Electronic Birth Certificate information. |
| 35 | `CIG_BEFORE_PREG` | INTEGER |  | Electronic Birth Certificate number of cigarettes/day 3 months before pregnancy. |
| 36 | `CIG_TRIMESTER_1` | INTEGER |  | Electronic Birth Certificate number of cigarettes/day during first trimester. |
| 37 | `CIG_TRIMESTER_2` | INTEGER |  | Electronic Birth Certificate number of cigarettes/day during second trimester. |
| 38 | `CIG_TRIMESTER_3` | INTEGER |  | Electronic Birth Certificate number of cigarettes/day during third trimester. |
| 39 | `PRINCIPAL_PMT_SRC_C_NAME` | VARCHAR | org | The principal source of payment category ID for Electronic Birth Certificate information. |
| 40 | `PRINCIPAL_PMT_SRC_CMT` | VARCHAR |  | Electronic Birth Certificate principal source of payment -- comment for other. |
| 41 | `RISK_FACTORS_DIABETES_C_NAME` | VARCHAR | org | The mother's diabetes risk category ID for Electronic Birth Certificate information. |
| 42 | `RISK_FACTORS_HYPERTENSION_C_NAME` | VARCHAR | org | The mother's hypertension risk category ID for Electronic Birth Certificate information. |
| 43 | `RSKFC_PREV_CSECT` | INTEGER |  | Electronic Birth Certificate number of previous caesarian deliveries risk factor. |
| 44 | `FORCEPS_C_NAME` | VARCHAR |  | The 'forceps attempted?' category ID for Electronic Birth Certificate information. |
| 45 | `VACUUM_C_NAME` | VARCHAR |  | The 'vacuum extraction attempted?' category ID for Electronic Birth Certificate information. |
| 46 | `PRESENTATION_C_NAME` | VARCHAR | org | The fetal presentation category ID for Electronic Birth Certificate information. |
| 47 | `ROUT_AND_METHOD_C_NAME` | VARCHAR | org | The route and method category ID for Electronic Birth Certificate information. |
| 48 | `CHILD_TRANSFERRED_C_NAME` | VARCHAR |  | The child's transfer status category ID for Electronic Birth Certificate information. |
| 49 | `CHILD_TRANS_TO` | VARCHAR |  | Electronic Birth Certificate area to which the child was transferred. This item is free-text. |
| 50 | `CHILD_ALIVE_C_NAME` | VARCHAR |  | The child's living status category ID for Electronic Birth Certificate information. |
| 51 | `CHILD_BREASTFED_C_NAME` | VARCHAR |  | The child's breastfed status category ID for Electronic Birth Certificate information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

