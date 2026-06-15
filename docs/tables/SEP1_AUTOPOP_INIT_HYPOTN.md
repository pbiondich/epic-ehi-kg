# SEP1_AUTOPOP_INIT_HYPOTN

> This table contains autopopulation data source information for the initial hypotension presentation data element in the CMS SEP-1 core measure.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HYPOTN_YN` | VARCHAR |  | The value (either 0-No or 1-Yes) to indicate the presence of initial hypotension within six hours before to six hours following the Severe Sepsis Presentation Instant and prior to the completion of the target ordered volume of crystalloid fluids. |
| 4 | `FLO_MEAS_ID` | VARCHAR | FK→ | The flowsheet row (FLO) ID where the initial hypotension is documented. |
| 5 | `FLO_MEAS_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FLO_MEAS_ID` | [IP_FLO_GP_DATA](IP_FLO_GP_DATA.md) | sole_pk | high |

