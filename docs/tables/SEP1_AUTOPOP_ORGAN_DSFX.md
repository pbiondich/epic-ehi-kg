# SEP1_AUTOPOP_ORGAN_DSFX

> This table contains autopopulation data source information for evidence of organ dysfunction, which is one of the clinical criteria considered to determine the sepsis presentation date and time for the CMS SEP-1 core measure.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_ID` | NUMERIC | shared | The ID of the order for the latest lab to identify organ dysfunction. |
| 4 | `FLO_MEAS_ID` | VARCHAR | FK→ | The ID of the latest flowsheet row to identify organ dysfunction. |
| 5 | `FLO_MEAS_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FLO_MEAS_ID` | [IP_FLO_GP_DATA](IP_FLO_GP_DATA.md) | sole_pk | high |

