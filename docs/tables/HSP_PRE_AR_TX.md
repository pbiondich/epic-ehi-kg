# HSP_PRE_AR_TX

> This table contains hospital billing temporary transaction information. This table is limited to charge temporary transactions that have not yet been posted to the account.

**Primary key:** `HTT_ID`, `LINE`  
**Columns:** 47  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HTT_ID` | NUMERIC | PK FK→ | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHARGE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `TX_COMMENT` | VARCHAR |  | The comment associated with the transaction line. |
| 5 | `CHARGE_DESCRIPTION` | VARCHAR |  | The description of the procedure associated with the transaction line. |
| 6 | `HCPCS_CODE` | VARCHAR |  | The HCPCS Code associated with the transaction line. |
| 7 | `NDC_ID` | VARCHAR | FK→ | The medication ID associated with the transaction line. |
| 8 | `NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 9 | `HIPPS_CODE` | VARCHAR |  | The HIPPS Code associated with the transaction line. |
| 10 | `HIPPS_CODE_TYPE_C_NAME` | VARCHAR |  | The HIPPS code type associated with the transaction line. |
| 11 | `MODIFIERS` | VARCHAR |  | This column stores the modifiers for a procedure. |
| 12 | `HIPPS_CODE_DESC` | VARCHAR |  | The HIPPS code description associated with the transaction line. |
| 13 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 14 | `REV_CODE_ID` | NUMERIC |  | The revenue code associated with the transaction line. |
| 15 | `REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 16 | `SUP_ID` | VARCHAR |  | The Supply ID associated with the transaction line. |
| 17 | `SUP_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 18 | `SERVICE_DATE` | DATETIME |  | The column displays the service date associated with the transaction line. |
| 19 | `PAT_ENC_CSN_ID` | VARCHAR | FK→ | The patient contact associated with the transaction line. |
| 20 | `PX_MED_NECESSITY_YN` | VARCHAR |  | Flag denoting whether or not the procedure is medically necessary. |
| 21 | `QUANTITY` | NUMERIC |  | Stores the number of units or days that this procedure was performed. |
| 22 | `PROC_START_DTTM` | DATETIME (Local) |  | Stores the start date and time of the procedure. |
| 23 | `PROC_END_DTTM` | DATETIME (Local) |  | Stores the date and time that the procedure stopped. |
| 24 | `TX_AMOUNT` | NUMERIC |  | The charge amount associated with the transaction line. |
| 25 | `DEFAULT_PRICE` | NUMERIC |  | The default price associated with the transaction line. |
| 26 | `DFLT_REV_CODE_ID` | NUMERIC |  | The default revenue code associated with the transaction line. |
| 27 | `DFLT_REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 28 | `DURATION_MINUTES` | INTEGER |  | Stores duration of service in minutes for the transaction line. |
| 29 | `PANEL_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 30 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 31 | `POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 32 | `RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 33 | `RSH_STUDY_SRC_C_NAME` | VARCHAR |  | The research study source associated with the transaction line. |
| 34 | `RSH_MOD_TYPE_C_NAME` | VARCHAR | org | Charge line's research billing modifier type. Normally, research charges with this value set should file to the patient account in order to be billed to insurance. |
| 35 | `RSH_CHG_ROUTE_C_NAME` | VARCHAR |  | This column specifies where to route the research charge. |
| 36 | `REFERENCE_AMT` | NUMERIC |  | Holds the reference amount that is calculated based on the financial class for the charge. This is set by the system and is applicable only to charges. |
| 37 | `REFERENCE_AMT_SRC_C_NAME` | VARCHAR |  | Holds the source of the reference amount that is used in the calculation of the reference amount. This is set by the system and is applicable only to charges. |
| 38 | `INST_PAT_NAME` | VARCHAR |  | The institutional patient name associated with the transaction line. |
| 39 | `INST_BIRTH_DATE` | DATETIME |  | The institutional patient date of birth associated with the transaction line. |
| 40 | `INST_EMP_NUMBER` | VARCHAR |  | The institutional employee number associated with the transaction line. |
| 41 | `INST_SEX_C_NAME` | VARCHAR | org | The legal gender for the institutional patient associated with the transaction line. |
| 42 | `INST_COMMENT` | VARCHAR |  | A comment stored in a charge transaction. If a hospital account's guarantor is of a type that is considered institutional, then certain pieces of institutional billing-related information can be stored in charges filed on that hospital account. |
| 43 | `INSTI_LINK_PAT_SN` | INTEGER |  | A linked patient serial number stored in a charge transaction. If a hospital account's guarantor is of a type that is considered institutional, then certain pieces of institutional billing-related information can be stored in charges filed on that hospital account. A linked patient serial number is one such piece of information. It is the patient serial number from which the data in the institutional billing-related information was pulled by the user while filling in those fields. |
| 44 | `SERVICE_AUTH_ID` | NUMERIC |  | The CoCM service decision authorization record associated with this charge. |
| 45 | `PANEL_DT` | DATETIME |  | The contact date of the panel procedure that is associated with this transaction. |
| 46 | `PANEL_DAT` | FLOAT |  | The contact date of the panel procedure that is associated with this transaction, in decimal format. Used to link with the CLARITY_EAP_OT table. |
| 47 | `RESEARCH_ENROLL_ID` | NUMERIC |  | Research study association per charge line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HTT_ID` | [HSP_PRE_AR_SESSION](HSP_PRE_AR_SESSION.md) | sole_pk | high |
| `NDC_ID` | [RX_NDC](RX_NDC.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

