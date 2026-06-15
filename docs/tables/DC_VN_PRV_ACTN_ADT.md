# DC_VN_PRV_ACTN_ADT

> Table for discharge orders part of the ED navigator provider audit.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DC_VN_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `DC_VN_ACTION_C_NAME` | VARCHAR |  | The reason category ID for the action taken on an order record. |
| 5 | `DC_VN_ACT_REASON` | VARCHAR |  | The reason for the action taken on an order record. This is extracted as the category title. |
| 6 | `DC_VN_ACT_INST_DTTM` | DATETIME (Local) |  | Stores the instant an action was taken on discharge orders in an emergency department navigator. |
| 7 | `DC_VN_PAT_CSN` | NUMERIC | FK→ | The unique contact serial number for the contact where the discharge navigator was used. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DC_VN_PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

