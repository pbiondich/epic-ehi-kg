# HH_VO_ADDL_PROV

> Verbal orders are sent to at least one primary signing provider. Certain verbal order types, such as hospice certificates of terminal illness, can be sent to additional signing providers. The additional signing providers are extracted to this table.

**Primary key:** `VERBAL_ORDER_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VERBAL_ORDER_ID` | VARCHAR | PK FK→ | The unique identifier for the verbal order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDL_PROV_ID` | VARCHAR |  | Providers to whom the verbal order was sent in addition to the provider in HH_VO_INFO.PROVIDER_ID. |
| 4 | `ADDL_PROV_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 5 | `ADD_PROV_LAST_EVT_C_NAME` | VARCHAR | org | Providers to whom the verbal order was sent in addition to the provider in HH_VO_INFO.PROVIDER_ID. This item stores the last event of each of the additional providers. It can be used to track the status of the different providers and to differentiate between orders that are signed electronically and manually. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VERBAL_ORDER_ID` | [HH_VO_INFO](HH_VO_INFO.md) | sole_pk | high |

