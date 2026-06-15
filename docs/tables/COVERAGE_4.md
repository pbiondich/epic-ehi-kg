# COVERAGE_4

> The COVERAGE_4 table contains high-level information on both managed care and indemnity coverage records in your system. This table also contains information related to Health Insurance Marketplace and Medicare Advantage coverages.

**Overflow of:** [COVERAGE](COVERAGE.md)  
**Primary key:** `CVG_ID`  
**Columns:** 72  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK | The unique identifier for the coverage record |
| 2 | `ALTR_ZIP` | VARCHAR |  | The alternate ZIP code to which claims submitted under this coverage can be sent. |
| 3 | `ALTR_CVG_COUNTY_C_NAME` | VARCHAR | org | The alternate county to which claims submitted under this coverage can be sent. |
| 4 | `ALTR_CVG_COUNTRY_C_NAME` | VARCHAR | org | The alternate country to which claims submitted under this coverage can be sent. |
| 5 | `ALTR_CVG_HOUSE_NUM` | VARCHAR |  | The alternate house number to which claims submitted under this coverage can be sent. |
| 6 | `ALTR_CVG_DISTRICT_C_NAME` | VARCHAR | org | The alternate district to which claims submitted under this coverage can be sent. |
| 7 | `ALTR_CVG_PHONE` | VARCHAR |  | The alternate phone number for claims submitted under this coverage. |
| 8 | `ALTR_CVG_FAX` | VARCHAR |  | The alternate fax number for claims submitted under this coverage. |
| 9 | `CVG_HEALTH_CENTER_C_NAME` | VARCHAR | org | The category number of the health center for this coverage. |
| 10 | `CVG_CREATOR_USER_ID` | VARCHAR |  | The unique ID of the user who created the coverage. This column is frequently used to link to the CLARITY_EMP table. |
| 11 | `CVG_CREATOR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `CVG_ISOLATED_YN` | VARCHAR |  | This flag is set if a coverage is isolated with regard to patient data restrictions. Coverages created from isolated patients or isolated guarantors are flagged as isolated coverages |
| 13 | `SELF_VERIF_DATE` | DATETIME |  | Stores the last self-verification date. Used by Welcome. |
| 14 | `CONT_FROM_CVG_ID` | NUMERIC |  | Points to a coverage that is logically the same coverage. This coverage record is continuing from the specified coverage record. |
| 15 | `HIX_POLICY_ID` | VARCHAR |  | The exchange policy identifier |
| 16 | `MA_WORKFLOW_STAT_C_NAME` | VARCHAR |  | Keeps track of what state of the workflow the Medicare Advantage process is in. |
| 17 | `NUM_UNCVRD_MO` | INTEGER |  | The incremental number of uncovered months (NUNCMO). This is determined from the later of the prior part D date, last LIS date, or the member's Initial Enrollment Period (IEP) date. To get the total NUNCMO add this amount to the existing NUNCMO. |
| 18 | `PPO_C_NAME` | VARCHAR |  | This value contains the premium payment option for a Medicare Advantage coverage. The premium payment option indicates whether the beneficiary has elected to withhold Part C and Part D premiums from their Social Security or Railroad Retirement Board (RRB) benefits, and if so, the type of withholding to use. After running deferred conversion 767822, this column will be obsolete. The premium payment option will be available in table MCARE_PREMIUM_PMT_OPT. |
| 19 | `PART_D_OPT_OUT_YN` | VARCHAR |  | This flag indicates that the beneficiary does not want Automated Enrollment in a Part D Plan. It applies to Low Income Subsidy beneficiaries who are subject to Automated Enrollment-Facilitated Enrollment into Part D. |
| 20 | `MMP_OPT_OUT_YN` | VARCHAR |  | This flag indicates the beneficiary does not want passive enrollment into a Medicare and Medicaid Plan (MMP). |
| 21 | `ESRD_OVRIDE_YN` | VARCHAR |  | This value indicates whether the End Stage Renal Disease (ESRD) override was used to enroll the beneficiary into a non-Prescription Drug Plan. |
| 22 | `CR_CVG_FLG_C_NAME` | VARCHAR |  | This value indicates whether the beneficiary has creditable drug coverage in the period prior to enrollment in this Part D Prescription Plan. It is also used to reset the number of uncovered months to zero due to a new initial enrollment period (IEP) or laboratory information system (LIS) change and to remove resets that were set in error. |
| 23 | `EMPR_SUB_ENROLL_YN` | VARCHAR |  | This value indicates that the beneficiary is currently in a plan receiving an employer subsidy, but still wants to enroll in a Part D plan |
| 24 | `ELECTION_TYP_C_NAME` | VARCHAR |  | This value tracks the election type associated with the enrollment. The election type is associated with a particular election period, and a particular type might be limited to a certain number of usages per member. This value is only applicable to Medicare Advantage coverages. |
| 25 | `ENROLL_SRC_C_NAME` | VARCHAR | org | This value indicates the source of enrollment, which is used only for Medicare Advantage coverages. |
| 26 | `BEQ_RESP_F_NAM` | VARCHAR |  | This item stores the first name of the member as received from the CMS eligibility response file. The system checks for mismatches between this name and the first name stored in the member record (EPT). |
| 27 | `BEQ_RESP_MID_INIT` | VARCHAR |  | This item stores the middle initial of the member as received from the CMS eligibility response file. The system checks for mismatches between this initial and the initial of the middle name stored in the member record (EPT). |
| 28 | `BEQ_RESP_L_NAM` | VARCHAR |  | This item stores the last name of the member as received from the CMS eligibility response file. The system checks for mismatches between this name and the last name stored in the member record (EPT). |
| 29 | `BEQ_RESP_GENDER_C_NAME` | VARCHAR | org | The gender category ID for the gender of the member as received from the CMS eligibility response file. The system checks for mismatches between this value and the sex stored in the member record (EPT). |
| 30 | `BEQ_RESP_DOB_DT` | DATETIME |  | This item stores the date of birth of the member as received from the CMS eligibility response file. The system checks for mismatches between this date and the date of birth stored in the member record (EPT). |
| 31 | `BEQ_RESP_DOD_DT` | DATETIME |  | This item stores the date of death of the member as received from the CMS eligibility response file. An error is flagged if this is populated, since a deceased member cannot receive benefits. |
| 32 | `PART_A_STAT_C_NAME` | VARCHAR |  | This column stores the status category ID for the current Medicare Part A eligibility status of the coverage. |
| 33 | `PART_B_STAT_C_NAME` | VARCHAR |  | This column stores the status category ID for the current Medicare Part B eligibility status of the coverage. |
| 34 | `PART_D_STAT_C_NAME` | VARCHAR |  | This column stores the status category ID for the current Medicare Part D eligibility status of the coverage. |
| 35 | `PART_D_ELIG_STRT_DT` | DATETIME |  | This column identifies the date on which the beneficiary became eligible for Part D benefits. |
| 36 | `PEND_PPO_EFF_DT` | DATETIME |  | This column holds a future expected date on which the Pending Premium Payment Option (CVG-18566) becomes the Premium Payment Option (CVG-18567). |
| 37 | `PEND_PPO_C_NAME` | VARCHAR |  | This column tracks what the new value for Premium Payment Option (see PPO_C) is expected to become as of the effective date given in PEND_PPO_EFF_DT. |
| 38 | `APCLM_CVG_VER_DATE` | DATETIME |  | Stores the date when the coverage was last verified. This data is only intended to be used when verification record (VRX) verification is used in an Accounts Payable (AP) Claims instance. |
| 39 | `DIS_ELECTION_TYP_C_NAME` | VARCHAR |  | This value tracks the election type associated with the disenrollment. The election type is associated with a particular election period, and a particular type might be limited to a certain number of usages per member. This value is only applicable to Medicare Advantage coverages. |
| 40 | `HIX_CSR_SRC_CVG_ID` | NUMERIC |  | This column is used to identify Cost Sharing Reduction (CSR) coverages and their corresponding source coverage (CVG) record. The value stored in this column is the ID of the source coverage of this CSR coverage. If the value is null, this coverage is not a CSR coverage. |
| 41 | `ADDR_CHG_USER_ID` | VARCHAR |  | The user who initiated the linked address changes. |
| 42 | `ADDR_CHG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 43 | `ADDR_CHG_INSTANT_DTTM` | DATETIME (Local) |  | The instant that the linked address changes were initiated. |
| 44 | `ADDR_CHG_SOURCE` | VARCHAR |  | The source record that initiated the linked address changes. |
| 45 | `ENROLL_GEO_VERIF_FAIL_YN` | VARCHAR |  | Tracks coverages that have failed service/geographic area verification. |
| 46 | `SUB_ADDR_IS_UNDELIV_YN` | VARCHAR |  | Indicates if subscriber home address is undeliverable. |
| 47 | `MA_WORKFLOW_STAT_RSN_C_NAME` | VARCHAR | org | The reason for the Medicare status pertaining to a coverage. |
| 48 | `IN_NON_PREFERRED_AREA_YN` | VARCHAR |  | If 'Y' then subscriber address associated with coverage was either only in a geographic area marked as "non-preferred" on the employer group or coverage was not in any geographic area linked to the employer group and employer group not configured to restrict enrollment by residency. If 'N' or NULL, the subscriber address is in a geographic area linked to the employer group that is not marked as "non-preferred" or geographic area verification has not been run for this coverage. |
| 49 | `GEO_TERM_TRACK_DATE` | DATETIME |  | The date that geographic area verification based termination tracking has started for a coverage. If not populated, coverage is not being tracked for termination. |
| 50 | `HIX_RENEW_COVERAGE_ID` | NUMERIC |  | Stores the coverage ID that this coverage is renewing. |
| 51 | `EFF_DT_CHNG_RSN_C_NAME` | VARCHAR | org | The effective date change reason at the coverage level. |
| 52 | `HIX_RENEWAL_TYPE_C_NAME` | VARCHAR |  | The exchange renewal type for the coverage. |
| 53 | `PAYMENT_TX_IDENT` | VARCHAR |  | The payment transaction ID for the coverage. |
| 54 | `CARRIER_TO_BILL_BINDER_PMT_YN` | VARCHAR |  | Indicates whether the carrier (exchange) is responsible for collecting the binder payment for this coverage. 'Y' indicates that the carrier is responsible for collecting the binder payment. 'N' or NULL indicate that the carrier is not responsible. |
| 55 | `HOUSEHOLD_IDENT` | VARCHAR |  | The household ID sent by the exchange for the coverage. |
| 56 | `MA_COVERAGE_TYPE_C_NAME` | VARCHAR |  | Stores the types of Medicare covered by the managed Medicare coverage. |
| 57 | `PLAN_CHANGE_VERIF_PREV_CVG_ID` | NUMERIC |  | The unique ID for the original coverage in the plan change. |
| 58 | `PLAN_CHANGE_VERIF_COMPLETE_YN` | VARCHAR |  | Indicates whether the plan change has completed execution for this coverage. 'Y' means the plan change has completed. 'N' means the plan change has not yet completed. NULL means this coverage is not the result of a plan change. |
| 59 | `ENTRY_DATE` | DATETIME |  | The date the coverage was created. |
| 60 | `EXISTING_NUNCMO` | INTEGER |  | The cumulative number of uncovered months (NUNCMO) as of the most recent prior Part D coverage. To get the total NUNCMO add the incremental NUNCMO to this amount. |
| 61 | `NUNCMO_SET_BY_C_NAME` | VARCHAR | org | Captures how the NUNCMO was set |
| 62 | `PRIOR_PART_D_DATE` | DATETIME |  | The end date of the Part D coverage prior to this enrollment. |
| 63 | `MA_ENROLL_SEP_RSN_C_NAME` | VARCHAR |  | The special election period reason used for enrollment on this coverage. This is required if the Enrollment Election Type is Other Special Election Period. This column can be linked to ZC_MA_ENROLL_SEP_RSN for additional information about the categories. |
| 64 | `MA_DISENROLL_SEP_RSN_C_NAME` | VARCHAR |  | The special election period reason used for disenrollment on this coverage. This is required if the Disenrollment Election Type is Other Special Election Period. This column can be linked to ZC_MA_ENROLL_SEP_RSN for additional information about the categories. |
| 65 | `MA_APPLICATION_CONFIRM_NUM` | VARCHAR |  | The confirmation number associated with the Online Enrollment Center (OEC) enrollment application. |
| 66 | `MA_PLAN_CHANGE_TYPE_C_NAME` | VARCHAR |  | The category ID for the type of plan change that led to the creation of this coverage. |
| 67 | `MA_PLAN_CHANGE_COVERAGE_ID` | NUMERIC |  | The unique ID of the previous coverage that this coverage was created as a plan change from. |
| 68 | `GEO_AREA_INVEST_START_DATE` | DATETIME |  | The date when the coverage begins geographic area investigation. |
| 69 | `GEO_AREA_TEMP_ADDR_START_DATE` | DATETIME |  | The subscriber temporary address start date for this coverage. |
| 70 | `REQ_TRM_DATE` | DATETIME |  | Stores the original termination date requested when the advanced logic is applied to the coverage's termination date. |
| 71 | `TRM_NTC_DATE` | DATETIME |  | Stores the date that notice of termination was given to be used for advanced term date logic. |
| 72 | `CVG_PHONE2` | VARCHAR |  | Payer phone number |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [COVERAGE](COVERAGE.md).

