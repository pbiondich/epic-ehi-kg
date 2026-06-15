# PAT_ADDL_TEMP_ADDR_DETAIL

> The PAT_ADDL_TEMP_ADDR_DETAIL table contains patient temporary address geo location data like latitude and longitude.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TEMP_ADDR_GEO_KEY_C_NAME` | VARCHAR |  | The geolocation identifier for the row's value stored in TEMP_ADDR_GEO_VAL. TEMP_ADDR_GEO_KEY_C identifies the type of data stored in the value; for instance: latitude and longitude. |
| 4 | `TEMP_ADDR_GEO_VAL` | VARCHAR |  | The geolocation value for the row. The type of geolocation value is determined by the TEMP_ADDR_GEO_KEY_C column. Latitude and Longitude are limited to 6 decimals of accuracy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

