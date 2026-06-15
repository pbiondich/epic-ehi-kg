# REFERRAL_CROSS_ORG

> This table contains cross-organization referral information.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CROSS_ORG_RFL_STATUS_C_NAME` | VARCHAR |  | Track the status of a cross-organization referral. |
| 4 | `CROSS_ORG_RFL_ORGANIZATION_ID` | NUMERIC |  | Store the organization for a cross-organization referral. |
| 5 | `CROSS_ORG_RFL_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 6 | `CROSS_ORG_RFL_UNIQUE_IDENT` | VARCHAR |  | Store the unique ID of a cross-organization referral. |
| 7 | `CROSS_ORG_RFL_ASGN_AUTH_OID` | VARCHAR |  | Store the assigning authority OID of a cross-organization referral. |
| 8 | `CROSS_ORG_RFL_RSN_CNCL_RQST` | VARCHAR |  | The reason a cancellation was requested for this referral. |
| 9 | `CROSS_ORG_RFL_INST_UPDATE_DTTM` | DATETIME (UTC) |  | Instant the cross-organization status was last updated. |
| 10 | `CROSS_ORG_RFL_INACTIVE_YN` | VARCHAR |  | Indicates whether this line of cross organization referral information is inactive due to patient unlinking. 'Y' indicates that the information is not currently active. 'N' or NULL indicates that the information is active. |
| 11 | `CROSS_ORG_RFL_REASON_DECLINE` | VARCHAR |  | The reason the cross-organization referral was declined. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

