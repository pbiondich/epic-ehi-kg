# AP_CLAIMS_BUNDLE_LEDGER

> This table is used to represent bundled episode ledgers which contain information about the services linked to episodes.

**Primary key:** `EPISODE_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK FK→ | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BND_AMOUNT` | NUMERIC |  | The amount by which a transaction updated the bundle ledger. This could be either a contribution or an adjustment. |
| 4 | `BND_SOURCE_TYPE_C_NAME` | VARCHAR |  | The source type of the bundle ledger transaction. |
| 5 | `BND_TX_ENTRY_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant that the bundle ledger transaction was logged in the UTC timezone. |
| 6 | `BND_SERVICE_DATE` | DATETIME |  | The service date of the transaction. |
| 7 | `BND_SOURCE_TX_ID` | NUMERIC |  | The unique identifier of the AP Claim service line that caused the transaction. |
| 8 | `BND_REVERSAL_OF_LN` | INTEGER |  | The bundle ledger line that was reversed by this transaction. |
| 9 | `BND_TX_ENTRY_INST_LOCAL_DTTM` | DATETIME (Local) |  | The instant that the bundle ledger transaction was logged in the local time zone. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |

