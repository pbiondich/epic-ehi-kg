# DOCS_RCVD_VTLS

> This table stores discrete vitals information received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `VTL_REF_ID` | VARCHAR |  | The unique reference identifier associated with the vital reading. |
| 6 | `VTL_DATETIME` | DATETIME (Local) |  | This item stores the date and time when the vital data were measured by the external system. |
| 7 | `VTL_HEIGHT` | NUMERIC |  | The patient height for the vital reading in centimeters. |
| 8 | `VTL_WEIGHT` | NUMERIC |  | This item stores the patient weight for the vital (unit is kg). |
| 9 | `VTL_CIRCUM` | NUMERIC |  | The patient head circumference for the vital measurement in centimeters. |
| 10 | `VTL_DXR_CSN` | NUMERIC |  | This item will store the contact serial number (CSN) of the Document Received record that owns the instance of this vital. |
| 11 | `VTL_HEIGHT_SRC_VALUE` | NUMERIC |  | Raw value of the height measurement in the document. |
| 12 | `VTL_HEIGHT_SRC_UNIT` | VARCHAR |  | Unit used for the height measurement in the document. |
| 13 | `VTL_WEIGHT_SRC_VALUE` | NUMERIC |  | Raw value of the weight measurement in the document. |
| 14 | `VTL_WEIGHT_SRC_UNIT` | VARCHAR |  | Unit used for the weight measurement in the document. |
| 15 | `VTL_CIRCUM_SRC_VALUE` | NUMERIC |  | Raw value of the head circumference measurement in the document. |
| 16 | `VTL_CIRCUM_SRC_UNIT` | VARCHAR |  | Unit used for the head circumference measurement in the document. |
| 17 | `VTL_PULSE` | INTEGER |  | The pulse reading of the vital reading in beats per minute. |
| 18 | `VTL_SYSTOLIC_BP` | INTEGER |  | This item stores the systolic blood pressure reading for the vital in the document (unit is mm[Hg]). |
| 19 | `VTL_DIASTOLIC_BP` | INTEGER |  | This item stores the diastolic blood pressure reading for the vital in the document (unit is mm[Hg]). |
| 20 | `VTL_BMI` | NUMERIC |  | The body mass index for the vital measurement in kilograms per square meter. |
| 21 | `VTL_LST_UPD_INST_DTTM` | DATETIME (UTC) |  | Stores the last update instant of the vital in UTC. |
| 22 | `VTL_TEMP` | NUMERIC |  | This item stores the patient temperature vital in Celsius. |
| 23 | `VTL_RESP` | INTEGER |  | This item stores the patient's respirations per minute vital. |
| 24 | `VTL_SPO2` | INTEGER |  | The pulse oximetry of the vital reading in percent. |
| 25 | `VTL_SRC_VALUE` | VARCHAR |  | The source value of the received vital reading before it is converted to a number. |
| 26 | `VTL_SRC_UNIT` | VARCHAR |  | The source unit of the received vital reading before it is converted. |
| 27 | `VTL_EVENT_IDENT` | VARCHAR |  | Universally unique identifier for the encounter document associated with this vital reading. In cases where there are multiple encounters that link to a vital reading, the earliest encounter is represented here. |
| 28 | `VTL_ORGANIZER` | VARCHAR |  | Identifier that groups vitals that should be associated together. |
| 29 | `VTL_LAST_KNOWN_HEIGHT` | NUMERIC |  | The item stores the patient's lookback height (cm). If the height for the current set of vitals is not filled out, it will look for the most recent height while the patient is over the age of 18. |
| 30 | `VTL_CALC_BMI` | NUMERIC |  | This item stores the Calculated BMI vital measurement in kg/m2 from the received document. |
| 31 | `VTL_BULK_STAT_C_NAME` | VARCHAR |  | The status of this data element within DINE. |
| 32 | `VTL_BULK_INCL_DATE` | DATETIME |  | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

