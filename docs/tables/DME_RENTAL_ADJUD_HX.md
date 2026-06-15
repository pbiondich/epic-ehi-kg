# DME_RENTAL_ADJUD_HX

> This table is intended to track the order in which services were adjudicated against a rental. Services may be removed or added to the rental due to readjudication and retroadjudication, and the adjudication time will represent the last time the claim was adjudicated against the rental.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the rental record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLAIM_ID` | NUMERIC | FK→ | Contains the claim that was adjudicated using this rental. |
| 4 | `TX_ID` | NUMERIC | shared | This column contains the procedure that was adjudicated using this rental. |
| 5 | `ADJUD_UTC_DTTM` | DATETIME (UTC) |  | Contains the instant when a claim procedure was most recently adjudicated and saved using this rental. |
| 6 | `ALLOWED_AMT` | NUMERIC |  | This column contains the allowed amount for the procedure that was adjudicated using this rental. If the allowed amount was overridden, then the override amount will be returned by this column |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

