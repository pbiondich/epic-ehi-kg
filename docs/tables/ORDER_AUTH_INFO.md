# ORDER_AUTH_INFO

> This table holds information about prior authorization for medications in certain workflows. It is currently only used when communicating with eClaimLink for authorizations.

**Primary key:** `ORDER_ID`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `MED_AUTH_RESULT_C_NAME` | VARCHAR |  | Holds the medication authorization result. |
| 3 | `MED_AUTH_NUM` | VARCHAR |  | Holds the authorization ID returned by the payer. |
| 4 | `AUTH_DENY_RSN_ID` | NUMERIC |  | Holds the authorization denial reason. |
| 5 | `AUTH_DENY_RSN_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 6 | `AUTH_START_UTC_DTTM` | DATETIME (UTC) |  | This item holds the instant the authorization is valid from. |
| 7 | `AUTH_END_UTC_DTTM` | DATETIME (UTC) |  | This item holds the instant the authorization is valid to. |
| 8 | `AUTH_LIMIT` | NUMERIC |  | Holds the medication authorization limit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

