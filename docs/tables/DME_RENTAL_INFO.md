# DME_RENTAL_INFO

> This table contains durable medical equipment (DME) member rental tracking record information, such as the member, service, and the amount or number of cycles on the rental so far.

**Primary key:** `RECORD_ID`  
**Columns:** 20  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the rental record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status (hidden, soft-deleted, etc). |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique identifier of the member attached to this rental record. |
| 4 | `VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 5 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 6 | `STATUS_C_NAME` | VARCHAR |  | The status of this rental record. |
| 7 | `TOTAL_CYCLES` | INTEGER |  | The total number of cycles so far on this rental record. |
| 8 | `DME_PRICING_ID` | NUMERIC |  | The Durable Medical Equipment (DME) Pricing record attached to this rental record. |
| 9 | `DME_PRICING_ID_RECORD_NAME` | VARCHAR |  | The name of the pricing record. |
| 10 | `TOTAL_AMOUNT` | NUMERIC |  | The total amount paid so far on this rental record. |
| 11 | `RECORD_CREATION_DATE` | DATETIME |  | Stores the date the record was created. |
| 12 | `MAINT_TOTAL_AMOUNT` | NUMERIC |  | Tracks the total of all maintenance payments made for the rental. |
| 13 | `MAINT_TOTAL_CYCLES` | NUMERIC |  | Tracks the number of cycle payments made for the rental during the maintenance period. |
| 14 | `RENTAL_CLOSE_REASON_C_NAME` | VARCHAR | org | The reason for closing a rental manually. |
| 15 | `INITIAL_AMOUNT` | NUMERIC |  | The initial amount specified for the rental on manual rental creation. Prevents this amount from being overwritten during adjudication. |
| 16 | `INITIAL_CYCLES` | INTEGER |  | The initial number of cycles specified for the rental on manual rental creation. Prevents this number from being overwritten during adjudication. |
| 17 | `INITIAL_MAINT_AMOUNT` | NUMERIC |  | The initial maintenance amount specified for the rental on manual rental creation. Prevents this amount from being overwritten during adjudication. |
| 18 | `INITIAL_MAINT_CYCLES` | INTEGER |  | The initial number of maintenance cycles specified for the rental on manual rental creation. Prevents this number from being overwritten during adjudication. |
| 19 | `RENTAL_START_DATE` | DATETIME |  | This is the start date for the rental. Rental cycles will be calculated based off of this starting date. |
| 20 | `MAINT_START_DATE` | DATETIME |  | The start date for maintenance on the rental. Maintenance cycles are calculated based on this starting date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

