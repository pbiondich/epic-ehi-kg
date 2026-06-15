# V_PB_TX_DTL_SNAPSHOT

> This view pivots the information provided in PB_TX_DTL_SNAP_ITEM and PB_TX_DTL_SNAP_VALUE into a more human-readable format. It also joins the metadata provided in PB_TX_DTL_SNAP_META associated with each snapshot.

**Primary key:** `TRANSACTION_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSACTION_ID` | VARCHAR | PK FK→ | The unique ID for the premium billing detail transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SNAPSHOT_DATE` | DATETIME |  | The date when the snapshot was taken in UTC. |
| 4 | `SNAPSHOT_USER_ID` | VARCHAR |  | The user that triggered the snapshot. |
| 5 | `SNAPSHOT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `AMOUNT` | VARCHAR |  | The amount associated with the detail transaction record in the snapshot and is initially populated during the computation stage of premium billing. It is derived from the PB_TX_DTL_SNAP_ITEM table where the SNAPSHOT_ITEM column value is 110, joined on its matching row in the PB_TX_DTL_SNAP_VALUE table with the value in the SNAPSHOT_VALUE column. |
| 7 | `OUTSTANDING_AMOUNT` | VARCHAR |  | The outstanding amount associated with the detail transaction record in the snapshot and is initially populated during the invoicing stage of premium billing. It is derived from the PB_TX_DTL_SNAP_ITEM table where the SNAPSHOT_ITEM column value is 440, joined on its matching row in the PB_TX_DTL_SNAP_VALUE table with the value in the SNAPSHOT_VALUE column. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `TRANSACTION_ID` | [CAP_DTL_TX](CAP_DTL_TX.md) | sole_pk | high |

