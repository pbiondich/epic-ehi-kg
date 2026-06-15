# QM_GEN_INFO

> This table contains general information about the quality measure associated with registry data records.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique ID of the registry data record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 3 | `ACUITY_SYSTEM_ID` | NUMERIC | FK→ | This item stores the scoring system record ID from which the scores are calculated and stored, if applicable. This item is populated when the RDI record is created. |
| 4 | `ACUITY_SYSTEM_ID_ACUITY_SYSTEM_NAME` | VARCHAR |  | The name of this HDA record. |
| 5 | `ORDER_ID` | NUMERIC | shared | The associated order ID. |
| 6 | `PARENT_REGISTRY_DATA_ID` | NUMERIC |  | Parent registry data record. Only populated if this is a repeating group record. |
| 7 | `QM_EXT_IDENT_BUNDLE_ID` | NUMERIC |  | The associated QRDA-I external ID bundle's RQG .1 |
| 8 | `REGISTRY_LOCATION_SETTING_ID` | NUMERIC |  | A unique identifier of the setting that defines the location submitting the data assocaited with this row. |
| 9 | `REGISTRY_LOCATION_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACUITY_SYSTEM_ID` | [ACUITY_CONFIG](ACUITY_CONFIG.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

