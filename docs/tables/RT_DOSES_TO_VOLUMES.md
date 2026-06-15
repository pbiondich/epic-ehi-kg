# RT_DOSES_TO_VOLUMES

> This table contains the body volumes being treated with radiation therapy, how many fractions planned/received, and the dose per fraction.

**Primary key:** `RT_SUMMARY_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RT_SUMMARY_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the radiotherapy summary record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `ORG_RECORD_ID` | NUMERIC | shared | Stores a referenced to a volume that is planned to receive or has received radiation therapy. |
| 5 | `TOTAL_DOSE_AMOUNT` | NUMERIC |  | Stores the total dose that was delivered or is planned to be delivered to the associated volume. |
| 6 | `TOTAL_RAD_THERAPY_DOSE_UNIT_C_NAME` | VARCHAR | org | Stores the unit of the associated total dose. |
| 7 | `FRACTION_DOSE_AMOUNT` | NUMERIC |  | Stores the dose delivered or planned to be delivered to the associated volume in each fraction. |
| 8 | `FRAC_RAD_THERAPY_DOSE_UNIT_C_NAME` | VARCHAR |  | Stores the unit of the associated fraction dose. |
| 9 | `NUM_FRACTIONS_TO_VOLUME` | INTEGER |  | Stores the number of fractions delivered or planned to be delivered to the associated volume. |
| 10 | `IS_UNIFORM_FRACTIONATION_YN` | VARCHAR |  | A flag indicating if the correspondence between the physical and biologically effective dose can be determined at the course level. If fractionation is not uniform, then the correspondence has to be determined at the phase level. |
| 11 | `IS_POINT_DOSE_YN` | VARCHAR |  | A flag indicating if the dose is determined at a single point. |
| 12 | `IS_PRIMARY_DOSE_YN` | VARCHAR |  | A flag indicating if the dose is the primary plan dose in a radiotherapy treatment plan. For a single treatment plan, the primary plan dose serves as the main dose value for tracking delviered vs. planned dose. In summaries over multiple treatment plans, the flag indicates that the dose is a primary plan dose in any of the summarized plans. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

