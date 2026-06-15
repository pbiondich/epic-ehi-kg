# MED_CVG_PAYER_INFO

> Stores payer information including the payer's source identifier, name, BIN, PCN, and group ID.

**Primary key:** `MED_ESTIMATE_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_ESTIMATE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the medication estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| 5 | `PAYER_SRC_IDENT` | VARCHAR |  | The identifier indicating who provided the payer associated with the Medication Estimate. |
| 6 | `PAYER_NAME` | VARCHAR |  | The name of the payer associated with this Medication Estimate. |
| 7 | `PAYER_BIN` | VARCHAR |  | The BIN number for the payer associated with this Medication Estimate. |
| 8 | `PAYER_PCN` | VARCHAR |  | The plan network ID (PCN) for the payer associated with this Medication Estimate. |
| 9 | `PAYER_GRP_IDENT` | VARCHAR |  | The group ID for the payer associated with this Medication Estimate. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MED_ESTIMATE_ID` | [MED_CVG_INFO](MED_CVG_INFO.md) | sole_pk | high |

