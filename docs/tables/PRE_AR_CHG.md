# PRE_AR_CHG

> This table contains one row for each line of each temporary accounts receivable (TAR) record (think of a TAR record as one charge entry screen and each line as an individual procedure). Deleting charge lines from Chronicles will delete rows from this table. This table contains basic information about the procedure and its charge review history. This table also contains the current status of the TAR record. This is found in the CHARGE_STATUS_C column.

**Overflow family:** [PRE_AR_CHG_2](PRE_AR_CHG_2.md), [PRE_AR_CHG_3](PRE_AR_CHG_3.md)  
**Primary key:** `TAR_ID`, `CHARGE_LINE`  
**Columns:** 83  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique ID of the temporary transaction record. |
| 2 | `CHARGE_LINE` | INTEGER | PK | The line number for the charge on this temporary transaction record. |
| 3 | `SERVICE_DATE` | DATETIME |  | The service date on which the charge procedure is performed. |
| 4 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `PROC_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 7 | `PROC_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 8 | `COVERAGE_ID` | NUMERIC | FK→ | The unique ID of the coverage on the charge. This column is frequently used to link to the V_COVERAGE_PAYOR_PLAN table. |
| 9 | `ACCOUNT_ID` | NUMERIC | FK→ | The unique ID of the guarantor account on the charge. This column is frequently used to link to the ACCOUNT table. |
| 10 | `PERF_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 11 | `BILL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 12 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 13 | `QTY` | NUMERIC |  | The quantity on the charge. |
| 14 | `AMOUNT` | NUMERIC |  | The dollar amount on the charge. |
| 15 | `ENTER_USER_ID` | VARCHAR |  | The unique ID of the user who entered the charge. This column is frequently used to link to the CLARITY_EMP table. |
| 16 | `ENTER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 17 | `FILE_DATE` | DATETIME |  | The date the temporary charge was posted into a transaction. If this field is blank the charge has not been posted into a transaction. It is either still in the workqueue (both the file date and delete date are blank) or has been deleted (the delete date field is populated). This date will match the post date in CLARITY_TDL. |
| 18 | `FILE_USER_ID` | VARCHAR |  | The unique ID of the user who corrected the error of the charges. This column is frequently used to link to the CLARITY_EMP table. |
| 19 | `FILE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 20 | `TX_ID` | NUMERIC | shared | The unique ID of the transaction the charge is stored within a temporary transaction. |
| 21 | `DELETE_DATE` | DATETIME |  | The date the charge was deleted. If this field is blank the charge has not been deleted. It is either still in the WQ (both the file date and delete date are blank) or has been filed into ETR (the file date field is populated). |
| 22 | `DELETE_USER_ID` | VARCHAR |  | The unique ID of the user who deleted the charge. This column is frequently used to link to the CLARITY_EMP table. |
| 23 | `DELETE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 24 | `REFERRING_PROV_ID` | VARCHAR | FK→ | The unique ID of the referral provider related to the charge. This column is frequently used to link to the CLARITY_SER table. |
| 25 | `REFERRING_PROV_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 26 | `RECEIVE_DATE` | DATETIME |  | The receive date for a charge. This date is entered by users in charge entry. |
| 27 | `CODER_USER_ID` | VARCHAR |  | The unique ID of the coder on the charge. This column is frequently used to link to the CLARITY_EMP table. This data is entered by users in charge entry. |
| 28 | `CODER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 29 | `CODED_DATE` | DATETIME |  | The date on which the charge was coded. This date is entered by users in charge entry. |
| 30 | `BILL_AREA_ID` | NUMERIC | FK→ | The unique ID of the bill area is associated with the charge. This column is frequently used to link to the BILL_AREA table. |
| 31 | `BILL_AREA_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 32 | `SESS_BILL_AREA_ID` | NUMERIC |  | The unique ID of the bill area is associated with the charge session (TAR). This column is frequently used to link to the BILL_AREA table. |
| 33 | `SESS_BILL_AREA_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 34 | `LOG_ID` | VARCHAR | shared | The unique ID associated with the surgical log record for this row. This column is frequently used to link to the OR_LOG table. This item is populated if charge is entered from OpTime (Epic's operating room management application). |
| 35 | `SUPPLY_ID` | VARCHAR | FK→ | The unique ID associated with the supply record for this row. This column is frequently used to link to the OR_SPLY table. |
| 36 | `SUPPLY_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 37 | `IMPLANT_ID` | VARCHAR | shared | The unique ID associated with the implant record for this row. This column is frequently used to link to the OR_IMP table. |
| 38 | `SESS_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 39 | `SESS_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 40 | `CHARGE_SOURCE_C_NAME` | VARCHAR |  | The source category number of the charge. This column will only be populated if the charge is not posted through the normal professional billing charge entry workflow. Charge source could be 1-Transaction Import, 2-Interface, 3-EpicCare, 4-Inpatient Charge Utility, 5-Hospital Professional Fee, 6-Inpatient Professional Charge. |
| 41 | `CHARGE_STATUS_C_NAME` | VARCHAR |  | The status category number of the charge. 1-Filed without Review, 2-Filed after Review, 3-In Review, 4-Deleted, 5-Created, 6-Deleted in Charge Review. |
| 42 | `SESS_PERF_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 43 | `SESS_BILL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 44 | `DENTAL_ENTRY_FLG` | VARCHAR |  | Indicates if the procedure is a dental procedure. |
| 45 | `DENTAL_TOOTH_NUM_C_NAME` | VARCHAR |  | The tooth number for the dental procedure. |
| 46 | `DENTAL_SURFACE` | VARCHAR |  | The tooth surface for the dental procedure. The value could be a semicolon-delimited string if there are multiple surfaces. For example, 2;3. |
| 47 | `DENTAL_ARCH_C_NAME` | VARCHAR |  | The arch info for the dental procedure. |
| 48 | `DENTAL_QUADRANT_C_NAME` | VARCHAR |  | The quadrant info for the dental procedure. |
| 49 | `DENTAL_AREA` | VARCHAR |  | The area info for dental procedure. The value is a dash-delimited string of two tooth numbers. It indicates the area between the two teeth. For example, 2-3. |
| 50 | `DENTAL_SUPNUMARY_YN` | VARCHAR |  | Indicates whether this dental procedure is for a supernumerary. |
| 51 | `DENTAL_MO_TO_RECALL` | INTEGER |  | The number of months after which follow-up is needed for the dental procedure. |
| 52 | `DENTAL_HYGIENIST_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 53 | `ANES_SUPPLEMENTAL` | VARCHAR |  | Indicate if the procedure is anesthesia or supplemental procedure. 1 means the procedure is an anesthesia procedure. 2 means the procedure is a supplemental procedure. |
| 54 | `TIMED` | VARCHAR |  | Indicate if the procedure uses timed algorithm. |
| 55 | `ADJUD_SELF_PAY_AMT` | NUMERIC |  | The adjudicated self-pay amount. |
| 56 | `ADJUD_COPAY_AMT` | NUMERIC |  | The adjudicated copay portion of the self-pay amount. |
| 57 | `ADJUD_COINS_AMT` | NUMERIC |  | The adjudicated coinsurance portion of the self-pay amount. |
| 58 | `ADJUD_DEDUCT_AMT` | NUMERIC |  | The adjudicated deductible portion of the self-pay amount. |
| 59 | `ADJUD_OVRIDE_FLAG_C_NAME` | VARCHAR |  | A flag to indicate if and how the adjudicated self-pay amount was overridden. |
| 60 | `OLD_RETRO_ETR_ID` | NUMERIC |  | Unique ID of old retroadjudication transactions. |
| 61 | `PRICE_PER_UNIT` | NUMERIC |  | The price for each unit for a procedure. |
| 62 | `NIA_NIDUS_OUTCOME_C_NAME` | VARCHAR | org | The National Imaging Association |
| 63 | `SPEC_SUP_PROC_TYP_C_NAME` | VARCHAR |  | The special supplemental procedure type category ID for the temporary transaction. |
| 64 | `ANES_PROCEDURE_LINK` | INTEGER |  | The line in the charge session that created this charge line. This happens for anesthesia supplemental procedures, charge shadowing, and charge quantity splitting. |
| 65 | `ANES_ASA_CODE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 66 | `ORDER_ID` | NUMERIC | shared | The order that is linked to this charge. |
| 67 | `RESEARCH_STUDY_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 68 | `PROTOCOL_CSN` | NUMERIC |  | Contact serial number of the charge's linked protocol version within linked research study or linked treatment plan. |
| 69 | `RSH_CHG_ROUTE_C_NAME` | VARCHAR |  | Category value to indicate how a charge related to a research study was routed, either to the research study guarantor account or to the patient's account. |
| 70 | `FIN_DIV_ID` | NUMERIC |  | The financial division associated with the charge. |
| 71 | `FIN_DIV_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 72 | `FIN_SUBDIV_ID` | NUMERIC |  | The financial subdivision associated with the charge. |
| 73 | `FIN_SUBDIV_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 74 | `CREATE_DATE` | DATETIME |  | The date the charge was created. |
| 75 | `TREATMENT_PLAN_CSN` | NUMERIC |  | The contact serial number of the treatment plan that generated this charge and order. |
| 76 | `RESEARCH_ENROLL_ID` | NUMERIC |  | The unique ID of the research study association linked to this charge. |
| 77 | `DENTAL_PREAUTH_QTY` | INTEGER |  | Stores the quantity that will be sent to insurance for preauthorization for the associated charge line |
| 78 | `PROC_INSTRUCTIONS` | VARCHAR |  | Free text regarding the specific procedure. |
| 79 | `FAST_PAY_SP_BALANCE` | NUMERIC |  | Self-pay balance for use with fast payment. |
| 80 | `REF_OVERRIDE_USER_ID` | VARCHAR |  | This item stores the user who overrode the referral associated with this charge line. |
| 81 | `REF_OVERRIDE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 82 | `REFERRAL_ID` | NUMERIC | FK→ | This items stores the referral ID for a charge line. |
| 83 | `CHARGE_COMMENT` | VARCHAR |  | This item stores a charge comment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `BILL_AREA_ID` | [V_BIL_ALL](V_BIL_ALL.md) | sole_pk | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |
| `REFERRING_PROV_ID` | [REFERRAL_SOURCE](REFERRAL_SOURCE.md) | sole_pk | high |
| `SUPPLY_ID` | [OR_SPLY](OR_SPLY.md) | sole_pk | high |

