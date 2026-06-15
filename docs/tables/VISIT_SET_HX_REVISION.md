# VISIT_SET_HX_REVISION

> The VISIT_SET_HX_REVISION table contains the user and instant that a visit set was modified. Information about specific items modified during the revision can be found in VISIT_SET_HX_CHANGE.

**Primary key:** `VISIT_SET_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VISIT_SET_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the visit set record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUDIT_TRAIL_USER_ID` | VARCHAR |  | The user responsible for this revision |
| 4 | `AUDIT_TRAIL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `AUDIT_TRAIL_INSTANT_DTTM` | DATETIME (UTC) |  | The instant at which this revision was filed |
| 6 | `AUDIT_TRAIL_VISIT_SET_CSN_ID` | NUMERIC |  | The version of the visit set for which this revision was made. Stores the CSN of the visit set version. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VISIT_SET_ID` | [VISIT_SET](VISIT_SET.md) | sole_pk | high |

