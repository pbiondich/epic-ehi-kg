# ODC_BASIC

> The ODC_BASIC table contains the basic information for the order context record. These include record status, logical/physical owner, record type, status, etc.

**Primary key:** `ORDER_CONTEXT_ID`  
**Columns:** 10  
**Org-specific columns:** 1  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_CONTEXT_ID` | NUMERIC | PK | The unique identifier for the order context record, which contains information about when orders are intended to be used. |
| 2 | `ODC_RECORD_TYPE_C_NAME` | VARCHAR |  | The type category number for the order context record. |
| 3 | `ODC_STATUS_C_NAME` | VARCHAR |  | The status category number for the order context record. |
| 4 | `ODC_PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 5 | `PAT_VISIT_CSN` | NUMERIC |  | This item stores the contact serial number (CSN) of the visit that the order context is linked to. |
| 6 | `HOLDING_REASON_C_NAME` | VARCHAR | org | The pend reason category ID for the order context record, which indicates the reason the record was created. |
| 7 | `LAST_ORDER_ADDED_DT` | DATETIME |  | The most recent date when an order was associated with the order context record. |
| 8 | `LAST_ORDER_RLSD_DT` | DATETIME |  | The most recent date when an order associated with this order context record was activated. |
| 9 | `OVERRIDE_START_DT` | DATETIME |  | The date the original surgical visit associated with this order context record was cancelled. |
| 10 | `INACTIVE_DT` | DATETIME |  | The date the context record was set to an inactive status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ODC_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [ODC_CTX_COMMENTS](ODC_CTX_COMMENTS.md) | `ORDER_CONTEXT_ID` | high |
| [ODC_REC_STATUS_HX](ODC_REC_STATUS_HX.md) | `ORDER_CONTEXT_ID` | high |
| [ODC_USER_CTX_OWNER](ODC_USER_CTX_OWNER.md) | `ORDER_CONTEXT_ID` | high |
| [ORDER_MED_4](ORDER_MED_4.md) | `ORDER_CONTEXT_ID` | high |

