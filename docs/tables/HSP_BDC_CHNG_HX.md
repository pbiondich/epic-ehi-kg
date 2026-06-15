# HSP_BDC_CHNG_HX

> Change History for the Denial/Correspondence (BDC) record.

**Primary key:** `BDC_ID`, `LINE_COUNT`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the denial or correspondence record. |
| 2 | `LINE_COUNT` | INTEGER | PK | Line number of change history that is being extracted by enterprise reporting. |
| 3 | `CHNG_INSTANT` | DATETIME (Local) |  | Instant this change occurred |
| 4 | `CHNG_USER_ID` | VARCHAR |  | User who initiated the change |
| 5 | `CHNG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CHNG_TYPE_C_NAME` | VARCHAR |  | Type of change that occurred. |
| 7 | `CHNG_SOURCE_VAL` | VARCHAR |  | This column stores the source value before change. It can be the unique identifier for the liability bucket or the denial/correspondence type (I BDC 30) depending on the type of change. |
| 8 | `CHNG_TARGET_VAL` | VARCHAR |  | This column stores the target value after change. It can be the unique identifier for the liability bucket or the denial/correspondence type (I BDC 30) depending on the type of change. |
| 9 | `CHNG_FOLLOW_UP_DT` | DATETIME |  | The follow-up date associated with the change. |
| 10 | `CHNG_COMMENTS` | VARCHAR |  | Comments for change. |
| 11 | `BFH_ID` | NUMERIC | FK→ | Stores the Billing Follow-up History (BFH) record ID that contains the information about the billing activity that was performed on this BDC. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |
| `BFH_ID` | [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | sole_pk | high |

