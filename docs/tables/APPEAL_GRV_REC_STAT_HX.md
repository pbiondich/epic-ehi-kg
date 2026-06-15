# APPEAL_GRV_REC_STAT_HX

> This table contains information about changes to the Chronicles record status/soft-delete flag (SDFL item) of the appeal/grievance record. Only records that have had their record status changed will be included in this table.

**Primary key:** `APPEAL_GRV_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `APPEAL_GRV_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the appeal/grievance record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `SDFL_EDIT_INSTANT_DTTM` | DATETIME (Attached) |  | Stores the instant that the record status was changed |
| 5 | `SDFL_EDIT_USER_ID` | VARCHAR |  | Stores the user who changed the record status |
| 6 | `SDFL_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `SDFL_EDIT_ACTI_C_NAME` | VARCHAR |  | Stores the action that was applied to the record status |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPEAL_GRV_ID` | [APPEAL_GRV](APPEAL_GRV.md) | sole_pk | high |

