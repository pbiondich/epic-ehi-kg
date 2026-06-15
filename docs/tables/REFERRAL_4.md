# REFERRAL_4

> The REFERRAL_4 table is a continuation of the REFERRAL_3 which is continuation of the REFERRAL_2 table. These tables are the primary tables for referral information stored in the system.

**Overflow of:** [REFERRAL](REFERRAL.md)  
**Primary key:** `REFERRAL_ID`  
**Columns:** 37  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK | The referral ID for the referral record. |
| 2 | `ATTEND_PROV_ADDR_ID` | VARCHAR |  | This item stores the address ID of the attending provider. The format is as follows: SerID-AddressID. AddressID is the line number of the multiple response address items in the Provider (SER) master file. It can be used to print the correct address in a report or letter, for example. |
| 3 | `RFL_NET_LVL_C_NAME` | VARCHAR | org | Store the referral's network status |
| 4 | `GEOGRAPHIC_AREA_ID_AREA_NAME` | VARCHAR |  | The name of the geograpic region |
| 5 | `IN_OUT_OF_AREA_C_NAME` | VARCHAR |  | In or out-of-area classification from ZIP code mapping. |
| 6 | `GEN_RFL_SEC_SINCE_MIDNIGHT_1` | NUMERIC |  | Referral-level generic time item for general use. |
| 7 | `GEN_RFL_SEC_SINCE_MIDNIGHT_2` | NUMERIC |  | Referral-level generic time item for general use. |
| 8 | `GEN_RFL_SEC_SINCE_MIDNIGHT_3` | NUMERIC |  | Referral-level generic time item for general use. |
| 9 | `GEN_RFL_SEC_SINCE_MIDNIGHT_4` | NUMERIC |  | Referral-level generic time item for general use. |
| 10 | `GEN_RFL_SEC_SINCE_MIDNIGHT_5` | NUMERIC |  | Referral-level generic time item for general use. |
| 11 | `AUDIT_REF_TO_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 12 | `AUDIT_REF_TO_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 13 | `AUDIT_REFG_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 14 | `AUDIT_REFG_PROV_ADDR` | VARCHAR |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the original text for the referring provider address ID. |
| 15 | `AUDIT_REF_TO_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 16 | `AUDIT_REF_TO_PROV_ADDR` | VARCHAR |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the original text for the referred-to provider address ID. |
| 17 | `AUDIT_RFL_SRC_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 18 | `RFL_DIRECTION_C_NAME` | VARCHAR |  | The referral direction, as calculated by logic for transitions of care |
| 19 | `REFD_TO_LINK_PROV_YN` | VARCHAR |  | Is the referred to provider an EpicCare Link provider |
| 20 | `REFD_TO_LINK_LOC_YN` | VARCHAR |  | Is the referred to location an EpicCare Link location |
| 21 | `IS_LEAKED_YN` | VARCHAR |  | Holds whether the referral is considered leaked |
| 22 | `TRIAGE_REMIND_DATE` | DATETIME |  | A date in the future when the user should be reminded of this referral. |
| 23 | `TRIAGE_INFO_RECPNT_C_NAME` | VARCHAR |  | The recipient of a request for more information. This item holds which item should be looked to for routing purposes. |
| 24 | `CE_DISCONNECT_YN` | VARCHAR |  | Indicates that this referral is disconnected from the sending organization for Care Everywhere referrals. |
| 25 | `RECENT_AUTH_RSN_C_NAME` | VARCHAR | org | This item holds the most recent non-empty authorization reason for the referral. If this item is null, it means the referral was never authorized. If value is added/updated to the authorization code (I RFL 73), same value is copied into this item. But if authorization code (I RFL 73) is cleared, then this item is not updated. |
| 26 | `RECENT_DENY_RSN_C_NAME` | VARCHAR | org | This item holds the most recent non-empty denial reason for the referral. If this item is null, it means the referral was never denied. If value is added/updated to the reason for denial (I RFL 18007), same value is copied into this item. But if reason for denial (I RFL 18007) is cleared, then this item is not updated. |
| 27 | `TRIAGE_UNACCEPT_REASON_C_NAME` | VARCHAR | org | The unaccept reason that was specified when the triage decision changed from accept to no decision. |
| 28 | `ADMITTING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 29 | `EXPECTED_DISCHARGE_DATE` | DATETIME |  | The expected discharge date documented on the referral bed days form of referral entry. |
| 30 | `GEN_RFL_DATE_6_DT` | DATETIME |  | This contains information from generic referral date item 6. |
| 31 | `GEN_RFL_DATE_7_DT` | DATETIME |  | This contains information from generic referral date item 7. |
| 32 | `GEN_RFL_DATE_8_DT` | DATETIME |  | This contains information from generic referral date item 8. |
| 33 | `GEN_RFL_DATE_9_DT` | DATETIME |  | This contains information from generic referral date item 9. |
| 34 | `GEN_RFL_DATE_10_DT` | DATETIME |  | This contains information from generic referral date item 10. |
| 35 | `GEN_RFL_SEC_SINCE_MIDNIGHT_6` | NUMERIC |  | This contains information from generic referral time item 6. |
| 36 | `RFL_SVC_TYPE_CODE_C_NAME` | VARCHAR |  | Specifies the service type that applies to the entire referral. |
| 37 | `INT_RFL_TYPE_C_NAME` | VARCHAR |  | The internal referral type for the referral. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [REFERRAL](REFERRAL.md).

