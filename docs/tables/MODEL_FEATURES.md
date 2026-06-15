# MODEL_FEATURES

> This table contains the most recently saved predictive model feature data for a patient.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MET_ID` | NUMERIC | FK→ | The identifier associated with a piece of information consumed by a predictive model. This can be a report column (PAF) ID or an extension mnemonic. |
| 4 | `MET_ID_RECORD_NAME` | VARCHAR |  | Stores the name of the registry metric record. |
| 5 | `FEAT_VALUE` | VARCHAR |  | The most recent value of the associated feature when it was used by a predictive model. |
| 6 | `FEAT_CONTRIBUTION` | NUMERIC |  | This item stores how much the associated feature contributed to the overall predictive model score. Contributions are rounded up to one decimal place, so that fractionally miniscule contributions can be differentiated from zero contributions. |
| 7 | `FEAT_UNIT` | VARCHAR |  | The unit associated with the feature value on this line. |
| 8 | `FEAT_DISPLAY_VALUE` | VARCHAR |  | The display value associated with the feature on this line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MET_ID` | [REG_METRIC_CONFIG](REG_METRIC_CONFIG.md) | sole_pk | high |

