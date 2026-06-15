# SAR_SVC_LN_INFO

> The service line adjudication information for a specific case of a service authorization request (SAR). The associated administrative information for the case can be found in the SAR_INFO table with the same referral and coverage ID. Child tables SAR_SVC_LN_CODE, SAR_SVC_LN_CODE_MOD, SAR_SVC_LN_CODE_UNITS, SAR_SVC_LN_GROUP, SAR_SVC_LN_GROUP_UNITS, SAR_SVC_LN_RANGE, and SAR_SVC_LN_RANGE_UNITS contain multiple rows of additional information related to each row in this table. You can join to each of those tables on the REFERRAL_ID columns and SAR_SVC_LN_INFO.LINE = GROUP_LINE from those tables.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SAR_VALID_FROM_DATE` | DATETIME |  | The start date for the line of Service Authorization Request (SAR) adjudication info. |
| 4 | `SAR_VALID_TO_DATE` | DATETIME |  | The expiration date for the line of Service Authorization Request (SAR) adjudication info. |
| 5 | `SAR_STATUS_C_NAME` | VARCHAR | org | The status category for the line of Service Authorization Request (SAR) adjudication info. |
| 6 | `SAR_DESC` | VARCHAR |  | The description associated with the line of Service Authorization Request (SAR) adjudication info. |
| 7 | `SAR_SVC_LN_CVG_ID` | NUMERIC |  | The coverage associated with the line of Service Authorization Request (SAR) adjudication information. |
| 8 | `SAR_REASON` | VARCHAR |  | The reason associated with the line of Service Authorization Request (SAR) adjudication info. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

