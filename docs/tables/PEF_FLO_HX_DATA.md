# PEF_FLO_HX_DATA

> This table contains historical data on PEF Flowsheet component information.

**Primary key:** `SUMMARY_BLOCK_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `PEF_HX_FLO_MEAS_ID` | VARCHAR |  | The historical values of the PEF flowsheet ID |
| 5 | `PEF_HX_FLO_MEAS_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |
| 6 | `PEF_MIN_HX_VAL` | NUMERIC |  | The historical values of the minimum allowable value for the PEF component |
| 7 | `PEF_MAX_HX_VAL` | NUMERIC |  | The historical values of the maximum allowable value for the PEF component |
| 8 | `PEF_SECONDARY_MIN_HX_VAL` | NUMERIC |  | The historical values of the minimum allowable secondary value for the PEF component (Minimum diastolic blood pressure). History item for HSB 32236. |
| 9 | `PEF_SECONDARY_MAX_HX_VAL` | NUMERIC |  | The historical values of the maximum allowable secondary value for the PEF component (Maximum diastolic blood pressure). History item for HSB 32241 |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

