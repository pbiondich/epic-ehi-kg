# OR_LNLG_LASER_SETS

> Laser settings can change throughout its use on a procedure. The table contains the different changes of the laser settings made. Each row in this table represents a combination of laser settings used while the laser is operated during the procedure.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LASER_PULSE_FREQ` | NUMERIC |  | A specific pulse frequency setting used while the laser was operated during the procedure. Other columns in this row represent settings that were used in conjunction with this one. |
| 4 | `LASER_PWR_SETTING` | NUMERIC |  | A specific power setting used while the laser was operated during the procedure. Other columns in this row represent settings that were used in conjunction with this one. |
| 5 | `LASER_PULSE_WIDTH` | NUMERIC |  | A specific pulse width setting used while the laser was operated during the procedure. Other columns in this row represent settings that were used in conjunction with this one. |
| 6 | `LASER_PULSE_WIDTH_C_NAME` | VARCHAR | org | The unit that was used to measure the pulse width column. |
| 7 | `LASER_COOL_METHOD_C_NAME` | VARCHAR | org | The cooling method used before the laser pulse. |
| 8 | `LASER_COOL_DURATION` | INTEGER |  | The amount of time (in ms) the cooling method was applied before the laser pulse. |
| 9 | `LASER_COOL_DELAY` | INTEGER |  | The amount of time (in ms) between the spray burst and the laser pulse. |
| 10 | `LASER_PEDAL_MODE_C_NAME` | VARCHAR | org | In relation to other laser settings, this is the laser pedal mode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

