# TAR_SVC_LN_INFO

> The service line adjudication information for a specific case of a Treatment Authorization Request (TAR). The associated administrative information for the case can be found in the TAR_INFO table with the same referral and coverage ID.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TAR_SERVICE_CODE` | VARCHAR |  | The service code for the line of Treatment Authorization Request (TAR) adjudication info. |
| 4 | `TAR_MODIFIER` | VARCHAR |  | The modifier for the line of Treatment Authorization Request (TAR) adjudication info. |
| 5 | `TAR_VALID_FROM_DATE` | DATETIME |  | The start date for the line of Treatment Authorization Request (TAR) adjudication info. |
| 6 | `TAR_VALID_TO_DATE` | DATETIME |  | The expiration date for the line of Treatment Authorization Request (TAR) adjudication info. |
| 7 | `TAR_UNITS` | INTEGER |  | The number of units for the line of Treatment Authorization Request (TAR) adjudication info. |
| 8 | `TAR_STATUS_C_NAME` | VARCHAR | org | The status for the line of Treatment Authorization Request (TAR) adjudication info. |
| 9 | `TAR_DESC` | VARCHAR |  | The free text description for the line of Treatment Authorization Request (TAR) adjudication info. |
| 10 | `TAR_RSN` | VARCHAR |  | The free text reason for the line of Treatment Authorization Request (TAR) adjudication info. |
| 11 | `TAR_SVC_LN_CVG_ID` | NUMERIC |  | The coverage associated with the line of Treatment Authorization Request (TAR) adjudication information. |
| 12 | `TAR_SVC_LN_CTL_NUM` | VARCHAR |  | The service line Treatment Authorization Request (TAR) control number. If this value exists, it should be used as a control number for this service line. If there is no value, the header level control number (TAR_CTL_NUM in table TAR_INFO) should be used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

