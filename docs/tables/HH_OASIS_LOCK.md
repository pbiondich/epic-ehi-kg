# HH_OASIS_LOCK

> Contains information on the locked status of Home Health Outcome and Assessment Information Set (OASIS) data sets.

**Primary key:** `OASIS_SET_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OASIS_SET_ID` | NUMERIC | PK FK→ | Unique identifier for the OASIS data set. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | Unique identifier for this contact for this patient. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 4 | `OASIS_LOCK_STAT_C_NAME` | VARCHAR |  | OASIS data set locked status, locked or unlocked. Links to category table ZC_OASIS_LOCK_STAT. |
| 5 | `OASIS_LOCK_USER_ID` | VARCHAR |  | User ID of the user who locked the OASIS data set. Links to table CLARITY_EMP. |
| 6 | `OASIS_LOCK_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `OASIS_LOCK_INSTANT` | DATETIME (Attached) |  | Instant at which the OASIS data set was locked. |
| 8 | `OASIS_SNAPSHOT_DAT` | VARCHAR |  | The contact pointer to the OASIS snapshot data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OASIS_SET_ID` | [HH_OASIS_INFO](HH_OASIS_INFO.md) | sole_pk | high |

