# MPM_ATTRIB_PROV

> This table contains data about providers attributed to patients for My Panel Metrics.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `MEASURE_GROUP_C_NAME` | VARCHAR | org | Measure groups attributed to providers for this patient for the purpose of My Panel Metrics. |
| 5 | `ATTRIB_RULE_LIST` | VARCHAR |  | A comma-delimited list of attribution rules that attributed the provider to the measure group. |
| 6 | `ATTRIB_SPEC_C_NAME` | VARCHAR | org | Primary specialty for the attributed provider. |
| 7 | `ATTRIBUTED_GROUP_ID` | NUMERIC | FK→ | Attributed Provider Groups for the provider attributed to the patient for the purpose of My Panel Metrics. |
| 8 | `ATTRIBUTED_GROUP_ID_PROV_GROUP_NAME` | VARCHAR |  | Record name |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ATTRIBUTED_GROUP_ID` | [ATTRIBUTED_PROV_GROUP](ATTRIBUTED_PROV_GROUP.md) | sole_pk | high |

