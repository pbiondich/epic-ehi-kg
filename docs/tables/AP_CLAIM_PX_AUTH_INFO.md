# AP_CLAIM_PX_AUTH_INFO

> This table contains information about the service-level authorizations used for the AP Claim's services.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUTH_ID` | NUMERIC | FK→ | The matching Authorization ID for the AP Claims procedure. |
| 4 | `OPERATIONAL_MATCH_YN` | VARCHAR |  | Whether the authorization is needed for the operational authorizations requirements. 'Y' indicates that this is needed to satisfy the operational authorizations requirements. 'N' or NULL indicate that it's not. |
| 5 | `BENEFIT_MATCH_YN` | VARCHAR |  | Whether the authorization is needed for the benefits authorizations requirements. 'Y' indicates that this is needed to satisfy the benefits authorizations requirements. 'N' or NULL indicate that it's not. |
| 6 | `VENDOR_CONTRACT_MATCH_YN` | VARCHAR |  | Whether the authorization is needed for the vendor contract. 'Y' indicates that this is needed for the vendor contract. 'N' or NULL indicate that it's not. |
| 7 | `COUNTS_USED` | INTEGER |  | The count used from this authorization. Note that this remains set even if the claim gets voided, or the service line is deleted. |
| 8 | `COUNTS_CALCULATED` | INTEGER |  | The count used that is calculated during AP claim adjudication. |
| 9 | `COUNTS_SHARED_C_NAME` | VARCHAR |  | Whether the service-level authorization count used is shared with a previously-adjudicated claim or service. |
| 10 | `AUTH_ATTACH_SOURCE_C_NAME` | VARCHAR |  | Whether the linked authorization was added manually or by the system. |
| 11 | `SUGGESTED_AUTH_YN` | VARCHAR |  | Whether the attached authorization was flagged and suggested as a potential authorization to a user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_ID` | [AUTHORIZATIONS](AUTHORIZATIONS.md) | overflow_master | medium |

