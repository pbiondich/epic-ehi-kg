# IP_FSD_TOTALS

> This table holds the daily total and hourly breakdown of I/O flowsheet rows.

**Primary key:** `ID`, `LINE`  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ID` | VARCHAR | PK FK→ | The unique ID of the flowsheet data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FLO_ID_FOR_ROW` | VARCHAR |  | ID of the flowsheet record for this line. |
| 4 | `ROW_TOTAL_DAILY` | NUMERIC |  | Daily total for this flowsheet. |
| 5 | `TOTAL_0000_0100` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 6 | `TOTAL_0100_0200` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 7 | `TOTAL_0200_0300` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 8 | `TOTAL_0300_0400` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 9 | `TOTAL_0400_0500` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 10 | `TOTAL_0500_0600` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 11 | `TOTAL_0600_0700` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 12 | `TOTAL_0700_0800` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 13 | `TOTAL_0800_0900` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 14 | `TOTAL_0900_1000` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 15 | `TOTAL_1000_1100` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 16 | `TOTAL_1100_1200` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 17 | `TOTAL_1200_1300` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 18 | `TOTAL_1300_1400` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 19 | `TOTAL_1400_1500` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 20 | `TOTAL_1500_1600` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 21 | `TOTAL_1600_1700` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 22 | `TOTAL_1700_1800` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 23 | `TOTAL_1800_1900` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 24 | `TOTAL_1900_2000` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 25 | `TOTAL_2000_2100` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 26 | `TOTAL_2100_2200` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 27 | `TOTAL_2200_2300` | NUMERIC |  | Hourly subtotal for this flowsheet. |
| 28 | `TOTAL_2300_0000` | NUMERIC |  | Hourly subtotal for this flowsheet. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ID` | [PROVTEAM_REC_INFO](PROVTEAM_REC_INFO.md) | sole_pk | high |

