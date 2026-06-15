# EPT_OR_PAT_SURG_PREORD

> This table stores data for all of a patient's pre-ordered specimens.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `ORD_SPEC_PREORDER_ID` | NUMERIC |  | Stores pre-existing, releasable specimen orders. |
| 4 | `ORD_SPEC_PREORD_COLLECT_C_NAME` | VARCHAR |  | Stores whether or not related specimen orders were collected. |
| 5 | `ORD_SPEC_PREORD_NC` | VARCHAR |  | Stores comments for specimen pre-orders that have been documented as "Not Collected" in EPT 88401. |
| 6 | `ORD_SPEC_PREORD_IB_MSG_ID` | VARCHAR |  | Stores the In Basket message ID for required pre-order specimens that has not been collected. |
| 7 | `ORD_SPEC_FL_LPP_ID` | NUMERIC |  | Search extension ID that the related order failed, even though it was still shown in the Specimens section |
| 8 | `ORD_SPEC_FL_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

