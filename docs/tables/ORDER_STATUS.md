# ORDER_STATUS

> The ORDER_STATUS table contains overtime single response orders information.

**Overflow family:** [ORDER_STATUS_2](ORDER_STATUS_2.md)  
**Primary key:** `ORDER_ID`, `ORD_DATE_REAL`  
**Columns:** 88  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | Unique ID for this order record |
| 2 | `ORD_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_NUMBER` | INTEGER |  | The contact number of the orders record. |
| 5 | `CONTACT_TYPE_C_NAME` | VARCHAR |  | The category value for the contact type, such as "1" for "Ordered" or "2" for "Resulted" |
| 6 | `ABNORMAL_YN` | VARCHAR |  | This Y/N flag reports Y if a result component in the order is reported as abnormal or N if the order is normal. |
| 7 | `ORDER_CREATOR_ID` | VARCHAR |  | The unique ID of the person creating the order. |
| 8 | `ORDER_CREATOR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `RESULTING_PROV` | VARCHAR |  | The name of the provider signing off on the results. |
| 10 | `LAB_TECHNICIAN` | VARCHAR |  | The technician responsible for the order tests. |
| 11 | `RESULTING_LAB_ID` | NUMERIC | FK→ | The unique ID of the lab running the test. |
| 12 | `RESULTING_LAB_ID_LLB_NAME` | VARCHAR |  | Interface laboratory name. |
| 13 | `INSTANT_OF_ENTRY` | DATETIME (Local) |  | The instant the record was last entered. |
| 14 | `INSTANT_OF_EDIT` | DATETIME |  | The instant the record was last edited. |
| 15 | `RX_DISPENSE_CODE_C_NAME` | VARCHAR | org | The pharmacy dispense code used for this order. |
| 16 | `RX_PAR_DOSES` | INTEGER |  | PRN par level number of doses |
| 17 | `CSN_FOR_ADD_REFILL` | NUMERIC |  | This item only applies to refill orders. It stores the contact serial numbers of the patient visits where the refill order was modified. |
| 18 | `SCHEDULED_DATE` | DATETIME |  | The date a standard ambulatory order is scheduled for. |
| 19 | `SCHEDULED_TIME` | DATETIME (Local) |  | The time a standard ambulatory order is scheduled for. |
| 20 | `PROCEDURE_NOTE_ID` | VARCHAR |  | This column contains the unique notes record identifier of the note that resulted the narrative for the order. |
| 21 | `PROCEDURE_NOTE_DT` | DATETIME |  | This is the date for the procedure note that resulted the order. |
| 22 | `ERFLL_REQ_RFL_PRN_C_NAME` | VARCHAR |  | This item stores the time period for refills requested in the erefill. |
| 23 | `ERFLL_APP_RFL_PRN_C_NAME` | VARCHAR |  | This item stores the time period for refills approved in the erefill. |
| 24 | `EREFILL_TO_PHM_ID` | VARCHAR |  | Stores the link to the general use notes record containing the action message to the pharmacy. |
| 25 | `WET_READS_C_NAME` | VARCHAR |  | Indicates whether this contact is created by Wet Reads. Used in ED Wet Reads pop-up form. |
| 26 | `ROUTING_OUTCOME_C_NAME` | VARCHAR | org | The category value of the outcome of results routing for each resulting contact of order associated with this row. |
| 27 | `ROUTING_RULE_LEVEL` | VARCHAR |  | The level at which the results routing rule used to determine recipients was specified. The possible levels are: Auth Prov, Auth Prov Primary Dept, Enc Dept, or System |
| 28 | `ROUTING_SCHEME_LINE` | VARCHAR |  | The line of the results routing scheme that was executed to determine recipients for this result. If no line was executed, the value of the column will be the string "DEFAULT". |
| 29 | `ROUTING_INST_TM` | DATETIME (Local) |  | The date and time the order was resulted and routed. |
| 30 | `ROUTING_USER_ID` | VARCHAR |  | The unique ID of the user the result was routed to for this row. |
| 31 | `ROUTING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 32 | `RIS_LET_TEMPLT_ID` | VARCHAR |  | The unique ID of the SmartText record for a mammography result letter associated with this order. |
| 33 | `RIS_LET_TEMPLT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 34 | `ROUTING_CURSTATUS_C_NAME` | VARCHAR | org | This item stores the current routing status for a resulting contact. |
| 35 | `MAM_LIFETIME_RISK` | NUMERIC |  | Patient's probability of getting breast cancer in a lifetime. Calculated using external formula. |
| 36 | `LAB_STATUS_C_NAME` | VARCHAR |  | Indicates the lab status value associated with each order contact. |
| 37 | `OVRL_BREAST_DENS_C_NAME` | VARCHAR | org | Overall breast density. Entered when reading a mammography study. |
| 38 | `RIGHT_BREAST_DENS_C_NAME` | VARCHAR |  | Right breast density. Entered when reading a mammography study. |
| 39 | `LEFT_BREAST_DENS_C_NAME` | VARCHAR |  | Left breast density. Entered when reading a mammography study. |
| 40 | `MOST_SIG_MAM_FIND_C_NAME` | VARCHAR | org | This stores the most significant mammography finding as documented by a radiologist. |
| 41 | `IMG_DOUBLE_READ_C_NAME` | VARCHAR | org | This tracks if a double read was performed while resulting an imaging study, and if so, what type of double read was it. |
| 42 | `CAD_USAGE_C_NAME` | VARCHAR | org | This stores whether CAD (Computer Aided Detection) was used while interpreting an imaging study. |
| 43 | `LAB_PATHOLOGIST_ID` | VARCHAR |  | The unique user ID of the pathologist that has responsibility for the current Anatomic Pathology order. |
| 44 | `LAB_PATHOLOGIST_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 45 | `RSLT_CNCT_INSTANT_DTTM` | DATETIME (UTC) |  | The instant in which a result contact is modified/filed to the system. Not to be confused with Result Date/Time, which is when the result was actually generated. |
| 46 | `RSLT_CNCT_USER_ID` | VARCHAR |  | The user filing the result contact. For interfaces or Beaker Result Filing background job, this might be a generic user. |
| 47 | `RSLT_CNCT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 48 | `RSLT_CNCT_SOURCE_C_NAME` | VARCHAR |  | Stores which entry point modified the result contact. |
| 49 | `IPROC_NOTE_ID` | VARCHAR |  | Stores the ID to the general use notes record of the Imaging and Procedures Resulting Note. |
| 50 | `IPROC_NOTE_CSN` | NUMERIC |  | Stores the contact serial number to the general use notes record of the Imaging and Procedures Resulting Note. |
| 51 | `RES_INTERPRETER_ID` | VARCHAR |  | The unique ID of the user who is the interpreter of the results for this order. |
| 52 | `RES_INTERPRETER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 53 | `RESPONS_AP_USER_ID` | VARCHAR |  | The unique ID of the lab user that has responsibility for the current anatomic pathology order. |
| 54 | `RESPONS_AP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 55 | `OVRL_TISSUE_COMP_C_NAME` | VARCHAR |  | Patient level tissue composition. Entered when reading a breast US. |
| 56 | `RIGHT_TISSUE_COMP_C_NAME` | VARCHAR |  | Right breast tissue composition. Entered when reading a breast US. |
| 57 | `LEFT_TISSUE_COMP_C_NAME` | VARCHAR |  | Left breast tissue composition. Entered when reading a breast US. |
| 58 | `OVRL_FGT_C_NAME` | VARCHAR |  | Patient level amount of fibroglandular tissue. Entered when reading a breast MR. |
| 59 | `RIGHT_FGT_C_NAME` | VARCHAR |  | Right breast amount of fibroglandular tissue. Entered when reading a breast MR. |
| 60 | `LEFT_FGT_C_NAME` | VARCHAR |  | Left breast amount of fibroglandular tissue. Entered when reading a breast MR. |
| 61 | `OVRL_BPE_C_NAME` | VARCHAR |  | Patient level background parenchymal enhancement. Entered when reading a breast MR. |
| 62 | `RIGHT_BPE_C_NAME` | VARCHAR |  | Right breast background parenchymal enhancement. Entered when reading a breast MR. |
| 63 | `LEFT_BPE_C_NAME` | VARCHAR |  | Left breast background parenchymal enhancement. Entered when reading a breast MR. |
| 64 | `SYMMETRIC_BPE_C_NAME` | VARCHAR |  | Symmetric flag for background parenchymal enhancement. Entered when reading a bilateral breast magnetic resonance (MR). |
| 65 | `LAB_CORR_TYPE_C_NAME` | VARCHAR |  | Stores the type of correction that was made to an anatomic pathology report. |
| 66 | `RESULT_DTTM` | DATETIME (Local) |  | The date and time the technician ran the tests for each order in calendar format. NOTE: Concatenates the result date (ORD 26) and result time (ORD 28) into a datetime format. If the time value is null, the query will return 12:00 AM for a time. |
| 67 | `LEFT_OVARY_SMALL_FOLLICLE_CNT` | INTEGER |  | The number of follicles in the left ovary at or below the minimum threshold as defined in system definitions (I LSD 53002). |
| 68 | `RIGHT_OVARY_SMALL_FOLLICLE_CNT` | INTEGER |  | The number of follicles in the right ovary at or below the minimum threshold as defined in system definitions (I LSD 53002). |
| 69 | `ENDOMETRIAL_STRIPE` | NUMERIC |  | The measurement of the endometrial stripe. |
| 70 | `OV_CYST_PRESENCE_C_NAME` | VARCHAR |  | Whether ovarian cysts are present in this ultrasound study. |
| 71 | `UTERINE_FIBROID_PRESENCE_C_NAME` | VARCHAR |  | Whether uterine fibroids are present in this ultrasound study. |
| 72 | `UTERINE_POLYP_PRESENCE_C_NAME` | VARCHAR |  | Whether uterine polyps are present in this ultrasound study. |
| 73 | `NARRATIVE_PERF_ORG_INFO` | INTEGER |  | This item stores the line number of the performing organization related group (ORD 1220) and acts as a pointer to the performing organization information of narrative of the result. |
| 74 | `IMPRESSION_PERF_ORG_INFO` | INTEGER |  | This item stores the line number of the preforming organization related group (ORD 1220) and acts as a pointer to the performing organization information of impression of the result. |
| 75 | `EXT_DISP_FILL_IDENT` | VARCHAR |  | Holds the unique identifier for a given fill used to identify the external dispense |
| 76 | `SR_VALID_STATUS_C_NAME` | VARCHAR |  | Indicates whether the study has been properly updated and validated for a particular order, and is ready for enhanced validation from outside of Study Review. Validated [1] means that the study is ready for enhanced validation. Not Validated [0] or blank means that it is not ready, usually because the study was modified from outside of Study Review, or has never been opened in Study Review. |
| 77 | `RESULT_PERF_ORG` | INTEGER |  | This item stores the line number of related group 1220 and acts as a pointer to the performing organization information of the result. |
| 78 | `LAB_RESULTING_METHOD` | VARCHAR |  | The main resulting method (either manual or a specific interface) that was used to result the order |
| 79 | `NLP_RESULT_ACTION_C_NAME` | VARCHAR |  | Flags which result contact was used to send the impression to Nebula for natural language processing. Used to determine if the impression changed since natural language processing ran. |
| 80 | `ROUTING_MOPS_ORDER_ID` | NUMERIC |  | The ID of the MOPS grouper order this order was routed with. |
| 81 | `ROUTING_MOPS_ORDER_DAT` | INTEGER |  | The DAT of the MOPS grouper order this order was routed with. |
| 82 | `NLP_UNVERIFIED_IB_ONLY_YN` | VARCHAR |  | Flag to restrict sending unverified NLP data to only In Basket. |
| 83 | `OVRL_AVG_VOL_BREAST_DENS` | NUMERIC |  | Overall average volumetric breast density. Stored as a percentage. |
| 84 | `RIGHT_VOL_BREAST_DENS` | NUMERIC |  | Right volumetric breast density. Stored as a percentage. |
| 85 | `LEFT_VOL_BREAST_DENS` | NUMERIC |  | Left Volumetric Breast Density. Stored as a percentage. |
| 86 | `BREAST_DENS_ALG` | VARCHAR |  | The algorithm used to determine breast composition and volumetric breast density |
| 87 | `BREAST_DENS_ALG_VER` | VARCHAR |  | The algorithm version used to determine breast composition and volumetric breast density |
| 88 | `OVRL_VOL_ASSOC_BREAST_DENS_C_NAME` | VARCHAR |  | Overall volumetric breast density's associated category. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `RESULTING_LAB_ID` | [CLARITY_LLB](CLARITY_LLB.md) | sole_pk | high |

