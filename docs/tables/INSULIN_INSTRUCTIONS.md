# INSULIN_INSTRUCTIONS

> This table contains dosing instructions for insulin injections and insulin pump settings.

**Primary key:** `DISCRETE_PAT_INSTR_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DISCRETE_PAT_INSTR_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the instructions name record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `DOSE_TM` | DATETIME (Local) |  | Time period for specific time-based instructions |
| 6 | `INSTRUCTIONS_NAME` | VARCHAR |  | The mealtime name for the insulin injections instructions. |
| 7 | `BASAL_RATE` | NUMERIC |  | Basal rate for this time period |
| 8 | `LOW_GLUCOSE_TARGET` | INTEGER |  | Low glucose target for time period |
| 9 | `HIGH_GLUCOSE_TARGET` | INTEGER |  | The high blood glucose target. When tested above this level, the patient may need to take insulin to adjust. |
| 10 | `CARB_RATIO` | NUMERIC |  | The carbohydrate to insulin ratio |
| 11 | `INSULIN_CORRECTION_FACTOR` | INTEGER |  | Insulin correction factor; the amount one unit of insulin will reduce the blood glucose level. |
| 12 | `FIXED_DOSE` | NUMERIC |  | The fixed dose of insulin to take at this time. |
| 13 | `FIXED_MEALTIME_DOSE` | NUMERIC |  | The fixed dose of insulin to take with this meal. |
| 14 | `UNITS_PER_CARB_SERV` | NUMERIC |  | The number of units of insulin to take for each carb serving (~15g, 8-21g) eaten during this meal. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DISCRETE_PAT_INSTR_ID` | [DISCRETE_PAT_INSTRUCTIONS](DISCRETE_PAT_INSTRUCTIONS.md) | sole_pk | high |

