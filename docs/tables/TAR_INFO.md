# TAR_INFO

> The general/administrative information for a specific case of a TAR (Treatment Authorization Request). The associated service line adjudication information can be found in the TAR_SVC_LN_INFO table with the same referral and coverage ID.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TAR_CVG_ID` | NUMERIC |  | The coverage associated with the line of Treatment Authorization Request (TAR) adjudication information. |
| 4 | `TAR_NUM` | VARCHAR |  | The Treatment Authorization Request (TAR) control number for the Treatment Authorization Request (TAR) adjudication information. |
| 5 | `TAR_PROV_NUM` | VARCHAR |  | The Treatment Authorization Request (TAR) provider number (NPI) for the Treatment Authorization Request (TAR) adjudication information. |
| 6 | `TAR_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `TAR_TAX_ID_NUM` | VARCHAR |  | The tax ID number for the Treatment Authorization Request (TAR) adjudication information. |
| 8 | `TAR_COMMENTS` | VARCHAR |  | The comments for the Treatment Authorization Request (TAR) adjudication info. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

