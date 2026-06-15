# BED_PLAN_HX

> This table contains information about edits that occurred on pending event records.

**Primary key:** `PEND_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PEND_ID` | VARCHAR | PK FK→ | The unique identifier for the pending action record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UPDATE_INST` | DATETIME (UTC) |  | The instant when the pending action record was updated. |
| 4 | `ORD_ID` | NUMERIC |  | The linked order ID (I PND 560) at the time that the pending event was updated, |
| 5 | `LOA_REASON_C_NAME` | VARCHAR | org | The leave of absence reason category ID for the bed planning event history. |
| 6 | `HX_BED_TYPE_C_NAME` | VARCHAR | org | History item for requested bed type. |
| 7 | `UPDATE_INST_LOCAL_DTTM` | DATETIME (Local) |  | The local instant when the pending event was updated. For UTC, use BED_PLAN_HX.UPDATE_INST. |
| 8 | `ORIGIN_GROUP_C_NAME` | VARCHAR | org | The request origin group that the request belonged to at the time of this update. |
| 9 | `DEFAULT_ORIGIN_GROUP_C_NAME` | VARCHAR |  | The default request origin group that the request belonged to at the time of this update. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PEND_ID` | [PEND_ACTION](PEND_ACTION.md) | sole_pk | high |

