# COMPILED_ATTRIBUTION_DATA

> This table holds the External Identifier Bundles and attributed providers for which attribution data was compiled.

**Primary key:** `ASGN_DATA_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ASGN_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the assignment data record record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| 5 | `ATTR_PROV_TYPE_C_NAME` | VARCHAR | org | The type of the attributed provider for this compiled attribution period. |
| 6 | `ATTRIBUTED_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 7 | `ATTRIBUTION_PERIOD_EFF_DATE` | DATETIME |  | The start date of the compiled provider attribution period. |
| 8 | `ATTRIBUTION_PERIOD_TERM_DATE` | DATETIME |  | The end date of the compiled provider attribution period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ASGN_DATA_ID` | [ASSIGNMENT_DATA](ASSIGNMENT_DATA.md) | sole_pk | high |

