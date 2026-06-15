# HSP_ACCT_EBC

> This table contains electronic birth certificate information from the Hospital Accounts Receivable (HAR) master file.

**Overflow family:** [HSP_ACCT_EBC_2](HSP_ACCT_EBC_2.md)  
**Primary key:** `HSP_ACCOUNT_ID`  
**Columns:** 38  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account with associated electronic birth certificate information. |
| 2 | `EBC_MOM_AGE` | INTEGER |  | The mother's age on the electronic birth certificate associated with the hospital account. |
| 3 | `EBC_MOM_RACE` | VARCHAR |  | The mother's race on the electronic birth certificate associated with the hospital account. |
| 4 | `EBC_MOM_BIRTH_DT` | DATETIME |  | The mother's birthdate on the electronic birth certificate associated with the hospital account. |
| 5 | `EBC_DAD_AGE` | INTEGER |  | The father's age on the electronic birth certificate associated with the hospital account. |
| 6 | `EBC_DAD_RACE` | VARCHAR |  | The father's race on the electronic birth certificate associated with the hospital account. |
| 7 | `EBC_DAD_BIRTH_DT` | DATETIME |  | The father's birthdate on the electronic birth certificate associated with the hospital account. |
| 8 | `EBC_BIRTH_WEIGHT` | INTEGER |  | The birth weight in grams of the child on the electronic birth certificate associated with the hospital account. |
| 9 | `EBC_PRV_BIRTHS_LIV` | INTEGER |  | Indicates the number of previous births that are now living |
| 10 | `EBC_PRV_BIRTHS_DEA` | INTEGER |  | Indicates the number of previous births that are now deceased. |
| 11 | `EBC_PRV_TERMINATES` | INTEGER |  | Indicates the number of previous terminations on the electronic birth certificate associated with the hospital account. |
| 12 | `EBC_LST_MENSES_DT` | DATETIME |  | This column stores the last normal menses date on the electronic birth certificate associated with the hospital account. |
| 13 | `EBC_PRENATL_VISITS` | INTEGER |  | Indicates the number of prenatal visits on the electronic birth certificate associated with the hospital account. |
| 14 | `EBC_APGAR_1MIN` | INTEGER |  | Indicates the Apgar value for 1 minute on the electronic birth certificate associated with the hospital account. |
| 15 | `EBC_APGAR_5MIN` | INTEGER |  | Indicates the Apgar value for 5 minutes on the electronic birth certificate associated with the hospital account. |
| 16 | `EBC_DT_LST_LIVBTH` | VARCHAR |  | Indicates the date of the last live birth on the electronic birth certificate associated with the hospital account. |
| 17 | `EBC_DT_LST_TERMNTN` | VARCHAR |  | Indicates the date of the last termination on the electronic birth certificate associated with the hospital account. |
| 18 | `EBC_GESTATNL_AGE` | INTEGER |  | The gestational age on the electronic birth certificate associated with the hospital account. |
| 19 | `EBC_CIGARETTES_DAY` | INTEGER |  | The average number of cigarettes per day on the electronic birth certificate associated with the hospital account. |
| 20 | `EBC_DRINKS_WEEKLY` | INTEGER |  | The average number of drinks per week on the electronic birth certificate associated with the hospital account. |
| 21 | `EBC_WT_GAINED_PREG` | INTEGER |  | Weight gained in pounds during the pregnancy on the electronic birth certificate associated with the hospital account. |
| 22 | `EBC_INFECTIOUS_DIS` | VARCHAR |  | A description of infectious disease on the electronic birth certificate associated with the hospital account. |
| 23 | `EBC_MRN` | VARCHAR |  | The medical record number on the electronic birth certificate associated with the hospital account. |
| 24 | `EBC_BIRTH_WT_LBSOZ` | VARCHAR |  | The birth weight in pounds and ounces on the electronic birth certificate associated with the hospital account. |
| 25 | `EBC_BIRTH_HEIGHT` | INTEGER |  | The birth height in inches on the electronic birth certificate associated with the hospital account. |
| 26 | `EBC_COMMENTS_CMT` | VARCHAR |  | Birth certificate comments on the electronic birth certificate associated with the hospital account. |
| 27 | `EBC_CHILD_SEX_C_NAME` | VARCHAR | org | This column stores the child's sex on the electronic birth certificate associated with the hospital account. Possible values are: 1-male, 2-female, or 9-unknown. |
| 28 | `EBC_BIRTH_INST_C_NAME` | VARCHAR | org | Indicates the institution of birth on the electronic birth certificate associated with the hospital account. |
| 29 | `EBC_FACLTY_TYP_C_NAME` | VARCHAR | org | Indicates the birth facility type on the electronic birth certificate associated with the hospital account. 1-Hospital, 2-Freestanding Birthing Center, 3-Clinic, 4-Doctor's Office, 5-Nursing Home, 6-Retirement Home, 7-Hospice, 8-Residence, 9-Other |
| 30 | `EBC_ATTND_TITLE_C_NAME` | VARCHAR | org | This column stores the attendant title on the electronic birth certificate associated with the hospital account: 1-Dr of Medicine, 2-Dr of Osteopathy, 3-Certified Nurse Midwife, 4-Other Midwife, 5-Dr of Naturopathy, 6-Other, 8-Unstated, or 9-Unknown/Invalid. |
| 31 | `EBC_BIRTH_TYP_C_NAME` | VARCHAR | org | Indicates the birth type on the electronic birth certificate associated with the hospital account. 1-Single, 2-Twin, 3-Triplet, 4-Quadruplet, 5-Quintuplet, 6-Siamese, 7-Other, 8-Unstated, 9-Unknown |
| 32 | `EBC_BIRTH_ORDER_C_NAME` | VARCHAR | org | Indicates the birth order on the electronic birth certificate associated with the hospital account. 1-First, 2-Second, 3-Third, 4-Fourth, 5-Fifth, 6-Sixth, 7-Seventh, 8-Eighth, 9-Unknown |
| 33 | `EBC_PRENAT_BGN_C_NAME` | VARCHAR | org | Indicates the month of pregnancy during which prenatal care began on the electronic birth certificate associated with the hospital account. 0-None, 1-1st Month, 2-2nd Month, 3-3rd Month, 4-4th Month, 5-5th Month, 6-6th Month, 7-7th Month, 8-8th Month, 9-9th Month, 10-Unstated/Unknown |
| 34 | `EBC_MOM_TRNS_FR_C_NAME` | VARCHAR |  | Indicates the institution the mother was transferred from on the electronic birth certificate associated with the hospital account. |
| 35 | `EBC_INF_TRNS_TO_C_NAME` | VARCHAR |  | Indicates the institution the infant was transferred to on the electronic birth certificate associated with the hospital account. |
| 36 | `EBC_TOB_USE_YNU` | VARCHAR |  | Indicates the if the mother used tobacco during the pregnancy on the electronic birth certificate associated with the hospital account. 1-Yes, 2-No, 3-Unknown |
| 37 | `EBC_ALC_USE_YNU` | VARCHAR |  | Indicates the if the mother used alcohol during the pregnancy on the electronic birth certificate associated with the hospital account. 1-Yes, 2-No, 3-Unknown |
| 38 | `EBC_CH_BIRTH_DT_TM` | DATETIME |  | Indicates the date and time at which the newborn associated with the hospital account was delivered. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

