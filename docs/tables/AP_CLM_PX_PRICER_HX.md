# AP_CLM_PX_PRICER_HX

> This table contains historical information for adjudications that invoked the Epic Pricer.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASSOC_CONTRACT_ID` | NUMERIC |  | The vendor contract associated with Epic Pricer message record. |
| 4 | `ASSOC_CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 5 | `USED_FOR_PRICE_YN` | VARCHAR |  | This value is set to Yes if the associated Epic Pricer message record was used to price the service. When comparing contracts, the Epic Pricer message record may not have been used for the final pricing of the service. |
| 6 | `PRICER_INVOKED_UTC_DTTM` | DATETIME (UTC) |  | The recorded timestamp of when the Epic Pricer was invoked by adjudication. |
| 7 | `PRICER_MSG_ID` | NUMERIC | shared | The unique identifier for the Epic Pricer message record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

