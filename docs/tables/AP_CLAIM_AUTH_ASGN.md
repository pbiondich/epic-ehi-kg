# AP_CLAIM_AUTH_ASGN

> Services that have manually assigned authorizations, which are used to fulfill the services' authorization requirements before other authorizations. Please refer to the query below for how to associate manually assigned referrals and authorizations to services. Note that REFERRAL_ID will always be set, but AUTH_ID might be NULL if the assignment is at the referral level, rather than the service-level authorization. SELECT AP_CLAIM_AUTH_ASGN.CLAIM_ID, AP_CLAIM_AUTH_ASGN.TX_ID, AP_CLAIM_AUTH_ASGN.LINE ASSIGNED_ORDER, AP_CLAIM_AUTH_ASGN_RFLS.REFERRAL_ID, AP_CLAIM_AUTH_ASGN_AUTHS.AUTH_ID FROM AP_CLAIM_AUTH_ASGN INNER JOIN AP_CLAIM_AUTH_ASGN_RFLS ON AP_CLAIM_AUTH_ASGN.CLAIM_ID = AP_CLAIM_AUTH_ASGN_RFLS.CLAIM_ID AND AP_CLAIM_AUTH_ASGN.LINE = AP_CLAIM_AUTH_ASGN_RFLS.GROUP_LINE LEFT OUTER JOIN AP_CLAIM_AUTH_ASGN_AUTHS ON AP_CLAIM_AUTH_ASGN.CLAIM_ID = AP_CLAIM_AUTH_ASGN_AUTHS.CLAIM_ID AND AP_CLAIM_AUTH_ASGN.LINE = AP_CLAIM_AUTH_ASGN_AUTHS.GROUP_LINE AND AP_CLAIM_AUTH_ASGN_RFLS.VALUE_LINE = AP_CLAIM_AUTH_ASGN_AUTHS.VALUE_LINE

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TX_ID` | NUMERIC | shared | Services that have manually assigned authorizations, which will be used to fulfill the services' authorization requirements before other authorizations. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

