# OTP_INFO_1

> This table is a continuation of related table OTP_INFO. It stores additional information about a treatment plan order, such as verbal signing information, inpatient medication information, etc.

**Overflow of:** [OTP_INFO](OTP_INFO.md)  
**Primary key:** `OTP_ID`  
**Columns:** 59  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK | The unique identifier for the patient order template record. |
| 2 | `TRANSPORTATION_C_NAME` | VARCHAR | org | The transportation type associated with the order template in this row. |
| 3 | `IP_DISC_INTERVAL_ID` | VARCHAR |  | The discrete interval associated with the order template in this row. |
| 4 | `IP_DISC_INTERVAL_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 5 | `IP_STANDING_COUNT` | NUMERIC |  | The standing count associated with the order template in this row. |
| 6 | `IP_STAND_CNT_TYPE_C_NAME` | VARCHAR |  | The inpatient standing count type (Dose/Days/etc) associated with the order template in this row. |
| 7 | `IP_INCLUDE_NOW_C_NAME` | VARCHAR |  | The frequency associated with the order template in this row, for example, "Include Now", "As Scheduled", "At Nurse Discretion." |
| 8 | `SCHED_EXTRA_DOSE_TM` | DATETIME (Local) |  | The time at which to schedule the first occurrence of the associated order template in this row. |
| 9 | `COST_CENTER_ID` | NUMERIC |  | The unique identifier for the cost center associated with the order template in this row. |
| 10 | `COST_CENTER_ID_COST_CENTER_NAME` | VARCHAR |  | The name of the cost center. |
| 11 | `ORDERING_MODE_C_NAME` | VARCHAR |  | The ordering mode (inpatient or outpatient) of the order template in this row. |
| 12 | `SELF_ADMIN_YN` | VARCHAR |  | Indicates whether the order template in this row is self-administered. ‘Y’ indicates that the order template in this row is self-administered. ‘N’ or NULL indicate that the order template in this row is not self-administered. |
| 13 | `PAT_SUPP_MED_YN` | VARCHAR |  | Indicates whether the order template in this row is a patient supplied medication. ‘Y’ indicates that the order template in this row is a patient supplied medication. ‘N’ or NULL indicate that the order template in this row is not a patient supplied medication. |
| 14 | `PAT_SUPPLIED_DOSES` | NUMERIC |  | The number of patient supplied doses. |
| 15 | `CALC_DOSE_AMOUNT` | VARCHAR |  | The calculated dose to administer for the order template in this row. |
| 16 | `CALC_DOSE_UNIT_C_NAME` | VARCHAR | org | The units for the calculated dose to administer for the order template in this row. |
| 17 | `DOSE_CALC_INFO` | VARCHAR |  | The dose calculation information for the order template in this row. |
| 18 | `ADMIN_DOSE` | VARCHAR |  | The amount to administer for the medication in this order template. |
| 19 | `ADMIN_UNIT_C_NAME` | VARCHAR |  | The units to use with the amount to administer for the medication in this order template. |
| 20 | `VERB_ORD_TYPE_C_NAME` | VARCHAR | org | The verbal order type for the order template in this row. For example, Ordering, Cosign, or Discontinuing. |
| 21 | `VERB_ORD_COMM_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 22 | `VERB_ORD_SIGNER_ID` | VARCHAR |  | The user ID of the verbal order signer for the order template in this row. |
| 23 | `VERB_ORD_SIGNER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 24 | `VERB_ORD_MSGRCP_ID` | VARCHAR |  | The user ID of the verbal order message recipient for the order template in this row. |
| 25 | `VERB_ORD_MSGRCP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 26 | `VERB_ORD_MSG_ID` | VARCHAR |  | The ID of the verbal order message. |
| 27 | `VERB_ORD_SIGN_INST` | DATETIME (Attached) |  | The date/time in external format when the verbal order was signed. |
| 28 | `VERB_ORD_MODE_C_NAME` | VARCHAR | org | The verbal order mode of the order template in this row. |
| 29 | `ORD_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 30 | `AUTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 31 | `CALC_RATE_FRM_VD_YN` | VARCHAR |  | Indicated whether or not to calculate rate given volume and duration. "Y" indicates that the rate will be calculated. "N" indicates that rate will not be calculated. |
| 32 | `CONDITION_FLAG` | NUMERIC |  | The condition flag for the order template in this row. |
| 33 | `MED_DOSE_PP_DESC` | VARCHAR |  | The free text description of the dose calculation for the order template in this row. |
| 34 | `OTP_ISOLATION_C_NAME` | VARCHAR | org | The isolation category for the order template in this row. |
| 35 | `OTP_CODESTATUS_C_NAME` | VARCHAR | org | The code status for the order template in this row. |
| 36 | `CODESTATUS_COMMENT` | VARCHAR |  | The code status comments for the order template in this row. |
| 37 | `DIET_C_NAME` | VARCHAR | org | The diet specified in the order template in this row. |
| 38 | `DIET_COMMENTS` | VARCHAR |  | The diet comments in the order template in this row. |
| 39 | `DOSE_ADJ_TYPE_C_NAME` | VARCHAR |  | This contains the type of dose adjustment - maximum, minimum, or standardized. |
| 40 | `DOSE_ADJ_OVERRID_YN` | VARCHAR |  | Indicates whether dose adjustment in I OTP 34180 was overridden. "Y" indicates that dose adjustment was overridden. "N" indicates that dose adjustment was not overridden. |
| 41 | `EFQ_OVRD_DAY_TYPE` | INTEGER |  | If column EFQ_OVRD_REL_DAYS in table OTP_FREQ_OV_REL_D is populated, this item specifies what the numeric values in that item represent. If this item's value is 1, then column EFQ_OVRD_CYCL_LEN stores relative days, otherwise OTP_FREQ_OV_REL_D stores weekdays. |
| 42 | `EFQ_OVRD_CYCL_LEN` | INTEGER |  | If EFQ_OVRD_DAY_TYPE is 1 (meaning the override times stored in the record are relative cycles), then this item stores the length of the cycle. |
| 43 | `ORX_ID` | NUMERIC |  | Networked Order Lookup Index Panel ID of an order template record applied to a patient. |
| 44 | `ORX_ID_ORDER_LOOKUP_NAME` | VARCHAR |  | The name (.2 item) for the order panel record. |
| 45 | `CSGN_CREATE_DTTM` | DATETIME (UTC) |  | When the cosign requirement was created (UTC Time). |
| 46 | `DFI_ID` | NUMERIC |  | The unique identifier for the Deficiency Instance record associated with the cosignature requirement for this order. |
| 47 | `CSGN_RQRD_C_NAME` | VARCHAR |  | Stores a yes/no flag for if an action requires a cosign (I OTP 34856). |
| 48 | `MEDS_ACTION_VERB_C_NAME` | VARCHAR | org | Action verb which is used in patient sig of the order. |
| 49 | `PRIOR_AUTH_NEEDED_YN` | VARCHAR |  | Stores if an order needs prior authorization. |
| 50 | `UNROUNDED_DOSE_MIN` | NUMERIC |  | The unrounded dose of this order. If the dose has a range (e.g. 1-2 mg), this is the lower end of the range. If the dose does not have a range, then this will store the dose. |
| 51 | `UNROUNDED_DOSE_MAX` | NUMERIC |  | The unrounded dose of this order. If the dose has a range (e.g. 1-2 mg), this is the upper end of the range. Otherwise, this is null. |
| 52 | `UNROUND_DOSE_UNIT_C_NAME` | VARCHAR |  | The dose unit category ID for the unrounded dose of this order. |
| 53 | `TO_PHARMACY_ID` | NUMERIC |  | The pharmacy that the order will be sent to. |
| 54 | `TO_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 55 | `MLSIG_SIGTYPE_C_NAME` | VARCHAR |  | The type of sig being used. |
| 56 | `COLLECTED_BY_USER_ID` | VARCHAR |  | This is the user who collected the specimen. |
| 57 | `COLLECTED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 58 | `COUNT_RANGE` | VARCHAR |  | This item stores a ranged value for the count of the order that goes along with the standing count type, indicating the number of hours, days, weeks, or occurrences for which the order will take place. Currently only available in Finland. |
| 59 | `COUNT_RANGE_STND_TP_C_NAME` | VARCHAR |  | This ranged count type goes along with the count from OTP-34042 to indicate the number of days, weeks, months, years, or occurrences for which the order will take place. Currently only available in Finland. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [OTP_INFO](OTP_INFO.md).

