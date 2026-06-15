# HSP_TX_AUTH_INFO

> This table contains the authorization information for each hospital transaction.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUTH_COVERAGE_ID` | NUMERIC |  | This item is the list of coverages the associated Authorization values are being applied to. |
| 4 | `AUTH_NUM` | VARCHAR |  | This item stores the list of authorization number overrides for a charge. This item cannot be set at the same time as Authorization ID (I HTR 833). |
| 5 | `AUTH_ID` | NUMERIC | FK→ | This item is the list of authorization records linked to a charge |
| 6 | `AUTH_SOURCE_C_NAME` | VARCHAR |  | This stores the source of the authorization link. |
| 7 | `AUTH_OVRIDE_USER_ID` | VARCHAR |  | This item stores the user who was responsible for the last authorization assignment. |
| 8 | `AUTH_OVRIDE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `AUTH_UPDATE_DTTM` | DATETIME (UTC) |  | This item stores the last time the authorization was updated either by the system or a user. |
| 10 | `INCL_IN_AUTH_CHG_CNT_YN` | VARCHAR |  | This column indicates whether the charge contributes to the used count of the authorization linked to it. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_ID` | [AUTHORIZATIONS](AUTHORIZATIONS.md) | overflow_master | medium |

