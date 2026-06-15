# PAT_LIFETIME_MAX

> The PAT_LIFETIME_MAX table contains information regarding patients' amounts credited toward lifetime maximum benefits (assuming the benefit plan is properly configured for tracking lifetime maximum benefits).

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number within a multiple response or over time item |
| 3 | `LIFEMAX_CARRIER_ID` | VARCHAR |  | The unique ID of the carrier for which this set of lifetime maximum buckets is counting. |
| 4 | `LIFEMAX_CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 5 | `LIFEMAX_FLAG_C_NAME` | VARCHAR |  | Indicates if the patient has approached or exceeded the lifetime maximum limit for the carrier |
| 6 | `LIFEMAX_BKT_MAN_IN` | NUMERIC |  | Allows manual override of the lifetime maximum in-plan accumulated amount |
| 7 | `LIFEMAXBKT_MAN_OUT` | NUMERIC |  | Allows manual override of the lifetime maximum out-of-plan accumulated amount |
| 8 | `LIFEMAXBKT_MAN_ALL` | NUMERIC |  | Allows manual override of the lifetime maximum total accumulated amount |
| 9 | `LIFEMAXAPPR_CLM_ID` | NUMERIC |  | The unique identifier of the accounts payable claim record which caused the "approaching" flag to be set |
| 10 | `LIFEMAX_APP_DATE` | DATETIME |  | The date on which the approaching lifetime maximum flag was set |
| 11 | `LIFEMAX_BKT_IN` | NUMERIC |  | The accumulated in-plan amount for claims paid under this carrier |
| 12 | `LIFEMAX_BUCKET_OUT` | NUMERIC |  | The accumulated out-of-plan amount for claims paid under this carrier |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

