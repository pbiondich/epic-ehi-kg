# REFERRAL_CVG

> The REFERRAL_CVG table contains coverage information for referrals.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique ID of the referral in database. |
| 2 | `LINE` | INTEGER | PK | A line number that is used to identify a group of coverage-related information. For example, if a referral has 2 valid coverages, line 1 of the coverage items contains the information about the first coverage, line 2 contains the information about the second coverage. |
| 3 | `CVG_ID` | NUMERIC | FK→ | The ID of a coverage that is valid for the referral. |
| 4 | `CVG_USED_YN` | VARCHAR |  | A yes/no flag that indicates whether or not the coverage should be considered available for the referral use in non-UM (utilization management) workflows. For UM workflows, consider using SUBMITTED_UM_AUTHS_YN. The coverage may be valid on the dates, but still inappropriate to use. Setting the flag to Yes means that the coverage is all right to use. |
| 5 | `AUTH_REQUIRED_YN` | VARCHAR |  | A flag to indicate whether the coverage requires external authorization to be received (as from an insurance carrier) for the services. |
| 6 | `CARRIER_AUTH_CMT` | VARCHAR |  | The carrier authorization number or comment, indicating that authorization was received. |
| 7 | `EFF_CVG_PRECERT_NUM` | VARCHAR |  | Precertification number associated with a coverage on a referral. |
| 8 | `EFF_CVG_AUTH_CMT` | VARCHAR |  | Comments regarding authorization specific to a coverage used on a referral. |
| 9 | `CVG_INVALID_FLAG` | VARCHAR |  | Flag for invalid coverage for non-UM (utilization management) workflows. |
| 10 | `CHARGE_COUNT_TYPE_C_NAME` | VARCHAR |  | Type of charges that this service level authorization record counts for professional, technical or all charges. |
| 11 | `USE_CHARGE_COUNT_YN` | VARCHAR |  | Flag to specify if the referral & coverage are using charge counting. |
| 12 | `CHARGE_COUNT_MTHD_C_NAME` | VARCHAR |  | Charge counting method for this service level authorization. |
| 13 | `CVG_SVC_TYPE_CODE_C_NAME` | VARCHAR |  | Specifies the service type at the coverage level. |
| 14 | `CVG_AUTH_STATUS_C_NAME` | VARCHAR |  | The authorization status category ID for the coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

