# V_EHI_FLO_MEAS_VALUE

> This view converts the MEAS_VALUE column in IP_FLWSHT_MEAS into an external-facing format for EHI Export. This table should be used in tandem with IP_FLWSHT_MEAS, using the FSD_ID and LINE columns to join the two together.

**Primary key:** `FSD_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FSD_ID` | VARCHAR | PK FK→ | The unique ID for the flowsheet data record. |
| 2 | `LINE` | INTEGER | PK | The line count for the item. |
| 3 | `MEAS_VALUE_EXTERNAL` | VARCHAR |  | The actual value of the flowsheet reading. This value is converted to an external format, depending on the value type (I FLO 825). For category values, this column will contain the category title. For date values, this column will contain a date string in Mon D YYYY HH:MMAM/PM format (e.g., Jan 1 2015 12:01AM). For time values, this column will contain a timestamp string in HH24:MM:SS format (e.g., 15:05:31 for 3:05 PM). For all other value types, the value matches what is stored in IP_FLWSHT_MEAS__MEAS_VALUE. |
| 4 | `UNITS` | VARCHAR |  | The units associated with the flowsheet value. For temperature flowsheet rows, this column contains '°F'. For height flowsheet rows, this column contains 'inches'. For weight flowsheet rows, this column contains 'ounces'. Otherwise, this column contains the unit value (I FLO 835) for the associated flowsheet row. |
| 5 | `VALUE_TYPE_C_NAME` | VARCHAR |  | The type of data in the record (i.e. numeric, string, temperature, etc.). |
| 6 | `FLO_MEAS_ID` | VARCHAR | FK→ | The unique ID of the flowsheet group/row. |
| 7 | `FLO_MEAS_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FLO_MEAS_ID` | [IP_FLO_GP_DATA](IP_FLO_GP_DATA.md) | sole_pk | high |
| `FSD_ID` | [IP_FLWSHT_REC](IP_FLWSHT_REC.md) | sole_pk | high |

