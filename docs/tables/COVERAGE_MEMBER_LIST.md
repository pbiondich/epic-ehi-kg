# COVERAGE_MEMBER_LIST

> The COVERAGE_MEMBER_LIST table contains information about the members associated with each coverage record. Since one coverage record can have multiple members, each row in the table corresponds to one member and is noted by the coverage ID and the line number.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 69  
**Org-specific columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each member of a coverage record. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID assigned to the patient record (EPT .1). |
| 4 | `MEM_COVERED_YN` | VARCHAR |  | The member’s covered status for the coverage, such as Y – the coverage is verified and in effect, or N – the coverage was invalidated manually. Note: 3 – Pending (not verified, but in effect), 4 – In Question (was verified, but recent carrier information omitted this coverage), 5 – Invalid (never verified, not effective). |
| 5 | `MEM_REL_TO_SUB_C_NAME` | VARCHAR | org | Stores the category identifier of the member's relationship to the subscriber. This column is commonly used to join to ZC_MEM_REL_TO_SUB. |
| 6 | `MEM_REL_TO_GUAR_C_NAME` | VARCHAR |  | The category value associated with the relationship of the patient to the guarantor. |
| 7 | `DEPENDENT_TYPE_C_NAME` | VARCHAR |  | For members whose relationship to the subscriber is unclear, this column specifies how the member is covered by the subscriber. |
| 8 | `COURT_DECREE_C_NAME` | VARCHAR | org | For members that are children involved in divorce scenarios, if a court has decreed exactly which of the parents is responsible for the child's medical expenses, then this column specifies how this subscriber is involved in that court decree. |
| 9 | `CUSTODY_C_NAME` | VARCHAR | org | For members that are children involved in divorce scenarios, this column specifies what type of custody the subscriber has over the child member. |
| 10 | `MEM_PAYOR_NAME` | VARCHAR |  | Stores the patient name as known to the Payor. This item is used to keep the name that is stored in the Patient master file separate from the name that the Payor is expecting. |
| 11 | `MEM_VERIFICATION_ID` | NUMERIC |  | The verification record for the coverage member. |
| 12 | `MEM_NUMBER` | VARCHAR |  | The identification number assigned to the member for the coverage. |
| 13 | `MEM_PERSON_CODE` | VARCHAR |  | This contains the person code for a member ID on a coverage. For a member ID of 12345-01, the person code would be "01". |
| 14 | `ELIGIBILITY_CLAR_C_NAME` | VARCHAR |  | Clarifies the eligibility of the patient when sending an Rx Adjudication message (i.e. Student). This item is populated in ambulatory pharmacy. |
| 15 | `MEM_APP_DATE` | DATETIME |  | The date on which the member applied for coverage. |
| 16 | `MEM_APP_TIME` | DATETIME (Local) |  | The time on which the member applied for coverage. |
| 17 | `MEM_EFF_FROM_DATE` | DATETIME |  | The date on which the coverage goes into effect for the member. |
| 18 | `MEM_STUDENT_YN` | VARCHAR |  | If the member is a full time student this column contains the value “Y”. If the member is not a full time student, as determined by the member’s Employment Status, this column contains the value “N”. |
| 19 | `MEM_MEDICARE_NUM` | VARCHAR |  | Stores the patient's Medicare number from the patient record, if applicable. This stored value may be a HICN or a MBI. This data is used primarily for Registration and will match PATIENT_4.LEGACY_HICN. However, it may be different from MEM_MEDICARE_NUM_COVERAGE, which is maintained through Enrollment and Eligibility infrastructure (preferred for managed care scenarios). |
| 20 | `MEM_ENROLL_RSN_C_NAME` | VARCHAR | org | The member's reason for enrollment. |
| 21 | `HIX_EN_ADDL_MAINT_RSN_C_NAME` | VARCHAR | org | This item stores the additional maintenance reason from an incoming ANSI 834 enrollment file. |
| 22 | `MEM_EFF_TO_DATE` | DATETIME |  | The date after which the coverage is no longer in effect for the member and the member becomes ineligible for benefits. |
| 23 | `MEM_TERM_REASON_C_NAME` | VARCHAR | org | The reason the member was terminated from the coverage. |
| 24 | `MEM_SCHED_DISCON_DT` | DATETIME |  | The member scheduled discontinuation date. |
| 25 | `MEM_LATE_ENROLL_YN` | VARCHAR |  | Y – the member applied for coverage after open enrollment. N – the member did not apply for the coverage after the open enrollment period. |
| 26 | `MEM_VERIF_STAT_C_NAME` | VARCHAR | org | The last saved value of the member's verification status. |
| 27 | `LAST_VERIF_DATE` | DATETIME |  | The date the member on the coverage was last verified. |
| 28 | `PCN_OVERRIDE` | VARCHAR |  | The processor control number (PCN) for this member. This PCN overrides the PCN at the plan or payor level for this member only. |
| 29 | `MEMBER_VERF_USER_ID` | VARCHAR |  | The ID of the user who last verified this member's status. |
| 30 | `MEMBER_VERF_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 31 | `MEMBER_ID_FROM_FILE` | VARCHAR |  | The member ID received on the source file for the member on the coverage. |
| 32 | `CARRIER_IDENTIFIER` | VARCHAR |  | Used for prescription adjudication in ambulatory pharmacy. Carrier code assigned in Workers' Compensation Program (327-CR). |
| 33 | `CLAIM_IDENTIFIER` | VARCHAR |  | Used for prescription adjudication in ambulatory pharmacy. Identifies the claim number assigned by Workers' Compensation Program (435-DZ). |
| 34 | `FACILITY_IDENTIFIER` | VARCHAR |  | Used for prescription adjudication in ambulatory pharmacy. ID assigned to the patient's clinic/host party (336-8C). |
| 35 | `HOME_PLAN` | VARCHAR |  | Used for prescription adjudication in ambulatory pharmacy. Code identifying the Blue Cross or Blue Shield plan ID which indicates where the member's coverage has been designated. Usually where the member lives or purchased their coverage (314-CE). |
| 36 | `PLAN_IDENTIFIER` | VARCHAR |  | Used for prescription adjudication in ambulatory pharmacy. Assigned by the processor to identify a set of parameters, benefits, or coverage criteria used to adjudicate a claim (524-FO). |
| 37 | `RX_BILLING_INFO_ID` | INTEGER |  | Contains the default prescription billing information on this coverage like default values to send during claim adjudication. |
| 38 | `HIX_APP_ID` | VARCHAR |  | The application ID of exchange coverages. |
| 39 | `HIX_ORIGIN` | VARCHAR |  | The origin type of exchange coverages. |
| 40 | `MEM_MAIL_CITY` | VARCHAR |  | The member's mailing city. |
| 41 | `MEM_MAIL_STATE_C_NAME` | VARCHAR | org | The member's mailing state. |
| 42 | `MEM_MAIL_ZIP` | VARCHAR |  | The member's mailing ZIP code. |
| 43 | `MEM_MAIL_COUNTY_C_NAME` | VARCHAR | org | The member's mailing county. |
| 44 | `MEM_MAIL_COUNTRY_C_NAME` | VARCHAR | org | The member's mailing country. |
| 45 | `MEM_MAIL_ADDR_LN_1` | VARCHAR |  | This item contains line one of the member's mailing address (the entirety of which is stored in CVG-18930). The purpose of this item is to provide the ability for reporting administrators to retrieve line one of the address without having to join the member address table. |
| 46 | `MEM_MAIL_ADDR_LN_2` | VARCHAR |  | This item contains line two of the member's mailing address (the entirety of which is stored in CVG-18930). The purpose of this item is to provide the ability for reporting administrators to retrieve line two of the address without having to join the member address table. |
| 47 | `MEM_CUSTO_NAME` | VARCHAR |  | The name of the member's custodial parent. |
| 48 | `MEM_CUSTO_CITY` | VARCHAR |  | The city of the member's custodial parent. |
| 49 | `MEM_CUSTO_STATE_C_NAME` | VARCHAR |  | The state of the member's custodial parent. |
| 50 | `MEM_CUSTO_ZIP` | VARCHAR |  | The ZIP code of the member's custodial parent. |
| 51 | `MEM_CUSTO_COUNTY_C_NAME` | VARCHAR |  | The county of the member's custodial parent. |
| 52 | `MEM_CUSTO_COUNTRY_C_NAME` | VARCHAR |  | The country of the member's custodial parent. |
| 53 | `MEM_CUSTO_EMAIL` | VARCHAR |  | The e-mail address of the member's custodial parent. |
| 54 | `MEM_CUSTO_ADDR_LN_1` | VARCHAR |  | This item contains line one of the member's custodial parent address (the entirety of which is stored in CVG-18962). The purpose of this item is to provide the ability for reporting administrators to retrieve line one of the address without having to join the member custodial parent address table. |
| 55 | `MEM_CUSTO_ADDR_LN_2` | VARCHAR |  | This item contains line two of the member's custodial parent address (the entirety of which is stored in CVG-18962). The purpose of this item is to provide the ability for reporting administrators to retrieve line two of the address without having to join the member custodial parent address table. |
| 56 | `MEM_COVERED_C_NAME` | VARCHAR |  | Stores the category identifier of member's covered status, such as whether their coverage is currently valid or in question. This column is commonly used to join to ZC_COVERED_STATUS. |
| 57 | `MEM_APPL_DTTM` | DATETIME (Local) |  | The date and time on which the member applied for coverage. |
| 58 | `MEM_PAYOR_SEX_C_NAME` | VARCHAR | org | The member's sex as it is recorded in the payor's system. |
| 59 | `MEM_MEDICARE_NUM_COVERAGE` | VARCHAR |  | Stores the member's Medicare number from the coverage, if applicable. This stored value may be a HICN or a MBI. This data is maintained through the standard Enrollment and Eligibility infrastructure (i.e. should be accurate for managed care scenarios). The number stored on the patient's record (MEM_MEDICARE_NUM or PATIENT.MEDICARE_NUM) may be different since it is used primarily for Registration. |
| 60 | `MEM_LEGACY_HICN_COVERAGE` | VARCHAR |  | If there is a HICN available for the member (e.g. known prior to receiving their MBI), this column stores the HICN from the coverage. This data is maintained through the standard Enrollment and Eligibility infrastructure (i.e. should be accurate for managed care scenarios). The number stored on the patient's record (PATIENT_4.LEGACY_HICN) may be different since it is used primarily for Registration. |
| 61 | `MEM_MAIL_HOUSE_NUM` | VARCHAR |  | The house number of the member's mailing address. |
| 62 | `MEM_MAIL_DISTRICT_C_NAME` | VARCHAR | org | The district category ID of the member's mailing address. |
| 63 | `MEM_CUSTO_HOUSE_NUM` | VARCHAR |  | The house number of the member's custodial parent's address. |
| 64 | `MEM_CUSTO_DISTRICT_C_NAME` | VARCHAR |  | The district category ID of the member's custodial parent's address. |
| 65 | `MEM_ADDR_IS_UNDELIV_YN` | VARCHAR |  | Indicates if member mailing address is undeliverable. |
| 66 | `MEM_MEDICAID_NUM` | VARCHAR |  | The Medicaid Number for a member on a given coverage. |
| 67 | `MEM_EFF_DT_CHNG_RSN_C_NAME` | VARCHAR | org | The effective date change reason at the member level. |
| 68 | `MEMBER_PAYER_BIRTH_DATE` | DATETIME |  | This item stores the member's date of birth as it is recorded in the payer's system. |
| 69 | `MEM_ALT_IDENT` | VARCHAR |  | The alternate card identification number assigned to the member for the coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

