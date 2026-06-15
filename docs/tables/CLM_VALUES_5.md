# CLM_VALUES_5

> All values associated with a claim are stored in the Claim External Value record. The CLM_VALUES_5 table holds claim-level values set by the system during claims processing or by user edits.

**Overflow of:** [CLM_VALUES](CLM_VALUES.md)  
**Primary key:** `RECORD_ID`  
**Columns:** 56

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim value record |
| 2 | `FHIR_GROUP_IDENTIFIER` | VARCHAR |  | The bulk FHIR group ID for which the claim was received. |
| 3 | `DEPT_ALT_CODE` | VARCHAR |  | This item stores the alternate code for the department. The alternate code comes from MPI. For Norway, this item stores the IK44 code. |
| 4 | `PAYER_ENTERPRISE_IDENTIFIER` | VARCHAR |  | Patient's enterprise ID assigned by the payer. |
| 5 | `ATT_PROV_SPECIALTY` | VARCHAR |  | The specialty of the attending provider. |
| 6 | `NON_PAYMENT_RSN_DESC` | VARCHAR |  | Claim level denial reason code description. |
| 7 | `CARRIER_PAYMENT_DNL_CD` | VARCHAR |  | Carrier claim payment denial code. |
| 8 | `NON_PAYMENT_RSN_CD` | VARCHAR |  | Claim level denial reason code. |
| 9 | `CARRIER_PAYMENT_DNL_DESC` | VARCHAR |  | Carrier claim payment denial code description. |
| 10 | `BCDA_GROUP_IDENT` | VARCHAR |  | Claim Group Identifier provided by Beneficiary Claims Data API |
| 11 | `PRIMARY_PAYER_CD` | VARCHAR |  | Code used to determine if Medicare was the primary payer of this claim. |
| 12 | `BIL_PROV_SPEC_CODE_SET` | VARCHAR |  | Stores the code set for the Billing Provider Specialty Code. |
| 13 | `OPER_PROV_TAXONOMY` | VARCHAR |  | Holds the Operating Provider Taxonomy Code for a claim. |
| 14 | `PREDETERMIN_IDENT` | VARCHAR |  | This is the predetermination of benefits identifier for the claim. |
| 15 | `ADJ_TO_CLAIM_ID` | VARCHAR |  | Holds the adjustment to claim ID for the claim received from raw data |
| 16 | `REV_TO_CLAIM_ID` | VARCHAR |  | Holds the reversal to claim ID for the claim received from raw data |
| 17 | `ADJ_SEQUENCE` | VARCHAR |  | Holds the adjustment sequence for the claim received from raw data |
| 18 | `PLAN_NAME` | VARCHAR |  | The plan name from raw claims data. |
| 19 | `CORPORATION_NAME` | VARCHAR |  | Corporation name from raw claims data. |
| 20 | `NETWORK_LEVEL` | VARCHAR |  | Specifies the network level of the claim. |
| 21 | `REGION_NAME` | VARCHAR |  | The name of the region associated with the claim. |
| 22 | `LINE_OF_BUSINESS_NAME` | VARCHAR |  | The name of the line of business associated with the claim. |
| 23 | `SVC_PROV_IN_NETWORK` | VARCHAR |  | This value indicates if the service provider / pharmacy is in-network. |
| 24 | `MEDICARE_DRUG_CVG_CODE` | VARCHAR |  | Identifies if a claim was processed under the Medicare Part B benefit or Part D benefit. |
| 25 | `SVC_FAC_CCN` | VARCHAR |  | Centers for Medicare and Medicaid Services Certification Number (CCN) for the service facility location. |
| 26 | `PCP_REF_PROV_NAM_LAST` | VARCHAR |  | This item holds the PCP referring provider's last name (NM1*P3). |
| 27 | `PCP_REF_PROV_NAM_FIRST` | VARCHAR |  | This item holds the PCP referring provider's first name (NM1*P3). |
| 28 | `PCP_REF_PROV_NAM_MID` | VARCHAR |  | This item holds the PCP referring provider's middle name (NM1*P3). |
| 29 | `PCP_REF_PROV_NAM_SUF` | VARCHAR |  | This item holds the PCP referring provider's suffix (NM1*P3). |
| 30 | `PCP_REF_PROV_NPI` | VARCHAR |  | This item holds the PCP referring provider's NPI (NM1*P3). |
| 31 | `PCP_REF_PROV_TAXONOMY` | VARCHAR |  | This item holds the referring provider's taxonomy code. |
| 32 | `REF_PROV_FROM_LINE_YN` | VARCHAR |  | Identifies whether the referring provider was received at the header level, or rolled up from the line level. |
| 33 | `REN_PROV_FROM_LINE_YN` | VARCHAR |  | Identifies whether the rendering provider was received at the header level, or rolled up from the line level. |
| 34 | `OPER_PROV_FROM_LINE_YN` | VARCHAR |  | Identifies whether the operating provider was received at the header level, or rolled up from the line level. |
| 35 | `OTHOP_PROV_FROM_LINE_YN` | VARCHAR |  | Identifies whether the other operating provider was received at the header level, or rolled up from the line level. |
| 36 | `PAT_RESIDENCE_CODE` | VARCHAR |  | The code identifying the patient's place of residence. This data is only populated for Pharmacy claims. |
| 37 | `SVC_FAC_CMS_PARTD_FLAG` | VARCHAR |  | Indicates whether the patient resides in a facility that qualifies for the CMS Part D benefit. This data is only populated for Pharmacy claims. |
| 38 | `BANK_IDENT_NUM` | VARCHAR |  | The card issuer ID or bank ID number used for network routing. This data is only populated for Pharmacy claims. |
| 39 | `PROCESSOR_CTL_NUM` | VARCHAR |  | The number assigned by the processor. This data is only populated for Pharmacy claims. |
| 40 | `RX_PRIOR_AUTH_TYPE` | VARCHAR |  | The code clarifying the prior authorization number submitted or benefit/plan exemption. |
| 41 | `PRESCRIBER_LAST_NAME` | VARCHAR |  | The last name of the prescribing provider. This data is only populated for Pharmacy claims. |
| 42 | `SNAPSHOT_CEV_YN` | VARCHAR |  | Contains a flag for whether or not the CEV respresents a snapshot of the data sent on an outgoing 837. Snapshot CEV records are created for rejected Tapestry claims that are added to Claim Export workqueues. |
| 43 | `SNAPSHOT_CEV_RECORD_ID` | NUMERIC |  | Contains the ID, if one exists, of the CEV containing the data sent on an outgoing 837 for an editable CEV record. |
| 44 | `PICK_UP_CNTY` | VARCHAR |  | Stores the Ambulance Pick-Up Location County |
| 45 | `DROP_OFF_CNTY` | VARCHAR |  | Stores the Ambulance Drop-Off Location County |
| 46 | `LAST_SRP_DATE` | DATETIME |  | The Last Scaling and Root Planing Procedure Date for the claim. |
| 47 | `NCH_CLAIM_TYPE` | VARCHAR |  | The CMS National Claims History (NCH) code indicating the type of claim submitted. |
| 48 | `CMS_ADJSTMT_DLTN_CD` | VARCHAR |  | The CMS Adjustment Deletion Code for the claim. This value distinguishes an adjusted or deleted PDE claim from an original. |
| 49 | `CLAIM_TYPE_OUT_IN` | VARCHAR |  | Claim type for use on Canadian claims |
| 50 | `COVERAGE_EXPIRY_DATE` | DATETIME |  | Expiry date of the plan registration number, for use with Canadian Claims |
| 51 | `DECEASED_INDICATOR` | VARCHAR |  | Deceased indicator, for use with Canadian Claims |
| 52 | `CLAIM_NET_AMOUNT` | NUMERIC |  | The net amount of the claim expected to be paid by the payer to the provider. |
| 53 | `VALUE_ADDED_TAX` | NUMERIC |  | The total Value Added Tax (VAT) charged on a claim. |
| 54 | `ENC_TYPE` | VARCHAR |  | The encounter type for a claim. Also known as Admitting Category. |
| 55 | `ENC_TRANSFER_SOURCE` | VARCHAR |  | The transfer source location for the encounter on the claim. Also known as Point of Origin. |
| 56 | `ENC_TRANSFER_DEST` | VARCHAR |  | The transfer destination for the encounter on the claim. Also known as Discharge Destination. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

