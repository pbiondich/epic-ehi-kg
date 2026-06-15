# APPEAL_GRV_POST_APL_UPD

> This table stores the table of updates to authorizations that are the subject of an appeal that has not yet finalized its decision.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UPDATE_INST_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the appeal's subject was updated. |
| 4 | `UPDATE_REALTIME_TX_CSN_ID` | NUMERIC |  | The unique contact serial number (CSN) of the transaction. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 5 | `UPDATE_ACK_YN` | VARCHAR |  | Indicates whether the update to the appeal subject has been acknowledged by an appeal user. 'Y' means the update has been acknowledged. 'N' or NULL means the update has not been acknowledged. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

