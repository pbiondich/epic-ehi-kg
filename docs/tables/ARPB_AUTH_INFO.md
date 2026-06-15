# ARPB_AUTH_INFO

> Stores authorization information for a charge transaction.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OVRD_AUTH_CVG_ID` | NUMERIC |  | Lists all the coverages on the guarantor account for this transaction. |
| 4 | `OVRD_AUTH_NUM` | VARCHAR |  | Stores the authorization number received from payor. This item is never automatically populated by the system. Users have to manually enter. |
| 5 | `AUTH_SOURCE_C_NAME` | VARCHAR |  | The authorization source type category ID of the authorization source for the transaction. |
| 6 | `AUTH_ID` | NUMERIC | FK→ | List of linked Authorization records based on coverages. |
| 7 | `AUTH_OVRIDE_USER_ID` | VARCHAR |  | This stores the user that was responsible for the last authorization assignment. |
| 8 | `AUTH_OVRIDE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `AUTH_UPDATE_DTTM` | DATETIME (UTC) |  | This stores the last time an authorization was assigned. |
| 10 | `INCL_IN_AUTH_CHG_CNT_YN` | VARCHAR |  | This column indicates whether the charge contributes to the used count of the authorization linked to it. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_ID` | [AUTHORIZATIONS](AUTHORIZATIONS.md) | overflow_master | medium |

