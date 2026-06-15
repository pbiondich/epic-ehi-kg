# PR_EST_INFO_3

> General information about the price estimate. Split from PR_EST_INFO.

**Overflow of:** [PR_EST_INFO](PR_EST_INFO.md)  
**Primary key:** `ESTIMATE_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `EST_USED_LOB_ID` | VARCHAR |  | The line of business on the benefit plan that was effective for the employer group at the time the estimate was created. This item will not change and is used in reporting. |
| 3 | `EST_USED_LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 4 | `EST_USED_CARRIER_ID` | VARCHAR |  | The carrier that was on the benefit plan that was effective for the employer group at the time the estimate was created. This item will not change and is used in reporting. |
| 5 | `EST_USED_CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 6 | `REFERRAL_ID` | NUMERIC | FK→ | Referral record used to find templates for the search in Cost Calculator. |
| 7 | `AUTH_REQUEST_ID` | NUMERIC | FK→ | Authorization request used to find templates for the search in Cost Calculator. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

